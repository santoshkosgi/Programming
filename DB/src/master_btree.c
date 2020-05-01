/*
This script contains c implementation of database using btrees.
*/

/*
Lets follow the following structure for writing this script.
1. All Libraries to be included
2. All Constants declaration.
3. All Struct definitions.
4. Functons.

*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COLUMN_USERNAME_SIZE 32
#define COLUMN_EMAIL_SIZE 255
typedef enum { NODE_INTERNAL, NODE_LEAF } NodeType;

// All constants would go here.
const int PAGE_SIZE = 4096;

// Defining sizes and offsets for different attributes of a page.
const uint32_t NODE_TYPE_SIZE = sizeof(((Pager*)0)->node_type);
const uint32_t IS_ROOT_SIZE = sizeof(((Pager*)0)->is_root);
const uint32_t NUM_OF_ROWS_SIZE = sizeof(((Pager*)0)->num_of_rows);
const uint32_t PARENT_POINTER_SIZE = sizeof(((Pager*)0)->parent_pagenumber);
const uint32_t PAGE_NUMBER_SIZE = sizeof(((Pager*)0)->page_number);

// OFFSETS
const uint32_t NODE_TYPE_OFFSET = 0;
const uint32_t IS_ROOT_OFFSET =  NODE_TYPE_OFFSET + NODE_TYPE_SIZE;
const uint32_t NUM_OF_ROWS_OFFSET = IS_ROOT_OFFSET + IS_ROOT_SIZE;
const uint32_t PARENT_POINTER_OFFSET = NUM_OF_ROWS_OFFSET + NUM_OF_ROWS_SIZE;
const uint32_t PAGE_NUMBER_OFFSET = PARENT_POINTER_OFFSET + PARENT_POINTER_SIZE;
const uint32_t SIZE_HEADER = NODE_TYPE_SIZE + IS_ROOT_SIZE + NUM_OF_ROWS_SIZE + PARENT_POINTER_OFFSET + PAGE_NUMBER_SIZE;
const uint32_t DATA_OFFSET = SIZE_HEADER;


typedef struct {
  char* buffer;
  size_t buffer_length;
  ssize_t input_length;
} InputBuffer;

typedef struct{
    uint32_t id;
    // Increasing length of name and email by one, so that it can accommodate the end of string charecter.
    char name[COLUMN_USERNAME_SIZE+1];
    char email[COLUMN_EMAIL_SIZE+1];
} Row;

typedef struct Pager
{
    void* page;
    uint8_t node_type;
    uint8_t is_root;
    size_t num_of_rows;
    short parent_pagenumber;
    short page_number;
} Pager;

typedef struct{
    short root_page_number;
    short number_of_rows_in_table;
    Pager* pager;
} Table;

typedef struct 
{   
    short row_number;
    short page_number;
    Table* table;
} Cursor;

Pager* initialise_pager(){
    Pager* page = malloc(sizeof((Pager*)0));
    page->page_number = -1;
    page->page = NULL;
    page->node_type = NODE_INTERNAL;
    page->is_root = 0;
    page->num_of_rows = 0;
    page->parent_pagenumber = -1;
    return page;
}

Table* initialise_table(){
    Table* table = malloc(sizeof((Table*)0));
    table->root_page_number = -1;
    table->pager = initialise_pager();
    return table;
}

Pager* loadpage(int page_number, FILE* fptr){
    // This function loads a page specific page number to memory and returns the page.
    // If page number is not present it creates a new one and returns it.
    int len;
    fseek(fptr, 0, SEEK_END);  
    int len_of_file = ftell(fptr);  
    // Assuming page numbers starts from 0. Subtracting 1 from number of pages.
    int number_of_pages_in_file = (len_of_file/PAGE_SIZE) - 1;

    // Checking if new page needs to be created. That too if required page number should be equal to last page's number
    // +1

    Pager* page = initialise_pager();
    page->page = malloc(PAGE_SIZE)
    page->page_number = page_number;

    if (page_number == number_of_pages_in_file + 1){
        return page;
    }

    // Moves Pointer to start of the req. Page number
    fseek(fptr, page_number*PAGE_SIZE, SEEK_SET);

    // Copies the data from file to page->page
    fread(page->page, PAGE_SIZE, 1, fptr);

    memcpy(page->node_type, page->page + NODE_TYPE_OFFSET, NODE_TYPE_SIZE);
    memcpy(page->is_root, page->page + IS_ROOT_OFFSET, IS_ROOT_SIZE);
    memcpy(page->num_of_rows, page->page + NUM_OF_ROWS_OFFSET, NUM_OF_ROWS_SIZE);
    memcpy(page->parent_pagenumber, page->page + PARENT_POINTER_OFFSET, PARENT_POINTER_SIZE);

    return page;
}

Cursor* table_start(Table* table){
    // This function initialises cursor to point to the root of the table.
    Cursor* cursor = malloc(sizeof((Cursor*)0));
    cursor->table = table;
    // Load the root page.
    cursor->page_number = table->root_page_number;
    cursor->row_number = 0;
    cursor->page_number = table->root_page_number;
    return cursor;
}

void* cursor_value(Cursor* cursor, FILE* fptr){
    
    // Checking if page is already loaded.
    if(cursor->page_number != cursor->table->pager->page_number){
        cursor->table->pager = loadpage(cursor->page_number);
    }
    // Else its already loaded.

    uint32_t row_number_address = DATA_OFFSET + (row_number * ROW_SIZE);

    uint32_t row_number_address = (row_number_in_page * ROW_SIZE);
    return cursor->table->pager->page+row_number_address;
}

Cursor* table_iterator(int key, Table* table, FILE* fptr){
    // This function iterates through the table and finds the correct position where key should be inserted and 
    // points the cursor accordingly.
    Cursor* cursor = malloc(sizeof((Cursor*)0));
    cursor->table = table;
    cursor->page_number = table->root_page_number;
    cursor->table->pager = loadpage(table->root_page_number);
    cursor->row_number = table->pager->num_of_rows + 1;
    return cursor;
}

InputBuffer* get_inputbuffer(){
    InputBuffer* input_buffer = NULL;
    input_buffer = malloc(sizeof(InputBuffer));
    input_buffer->buffer = NULL;
    input_buffer->buffer_length = 0;
    input_buffer->input_length = 0;
    return input_buffer;
}


void read_input_buffer(InputBuffer* input_buffer){
    input_buffer->input_length = getline(&(input_buffer->buffer), &(input_buffer->buffer_length),  stdin);
    // Strip()
    input_buffer->buffer[input_buffer->input_length - 1] = 0;
    input_buffer->input_length -= 1;
}


void print_prompt(){
    printf("db > ");
}

int process_non_sql_statements(char* statement){
    if (strcmp(statement, ".exit") == 0){
            printf("Closing DB connection");
            return EXIT_SUCCESS;
        }
    return EXIT_FAILURE;
}

int insert_row_into_table(Row* row, Table* table, FILE* fptr){
    /*
    This function finds the corresponding page and corresponding memory location in the page to copy the row data, using
    serialising function. This function also allocates memory to the page.
    */

    // Checking for errors.

    if (strlen(row->name) > COLUMN_USERNAME_SIZE || strlen(row->email) > COLUMN_EMAIL_SIZE){
        printf("%s\n", "Check the length of fields supplied for Name and Email columns.");
        return PREPARE_STRING_TOO_LONG;
    }

    Cursor* cursor = table_start(table);
    serialize(row, table_iterator(table, row->id, fptr));
    printf("%s:%d\n", "Row inserted", row_number);
    free_object(cursor);
    return EXIT_SUCCESS;
}


int process_sql_statements(char* statement, Table* table, FILE* fptr){
    if (strncmp(statement, "insert", 6) == 0){
        printf("Insert statement will be processed\n");
        Row* row = get_row();
        int args_assigned = sscanf(statement, "insert %d %s %s", &(row->id), row->name, row->email);

        if (args_assigned != 3){
            printf("Synatx Error\n");
            return PREPARE_SYNTAX_ERROR;
        }
        // Insert row into the table.
        insert_row_into_table(row, table, fptr);

        free_object(row);
        return EXIT_SUCCESS;

    }
    // Adding support to print all the rows
    else if(strncmp(statement, "select_all", 10) == 0){
        Row* row = get_row();
        print_all_rows(row, table, fptr);
        free_object(row);
        return EXIT_SUCCESS;
    }

    else if(strncmp(statement, "select", 6) == 0){
        printf("Select statement will be processed\n");
        Row* row = get_row();
        int id;
        int args_assigned = sscanf(statement, "select %d", &id);
        if(args_assigned != 1){
            printf("More or less number of arguments in the query statement\n");
            return EXIT_FAILURE;
        }
        fetch_row_from_table(id, row, table);
        free_object(row);
        return EXIT_SUCCESS;
    }
    else{
        return EXIT_FAILURE;
    }
}



int main(void)
{
    FILE *fptr;
    fptr = fopen("Database_btree.db", "r+");
    if (fptr == NULL)
    {
        fptr = fopen("Database_btree.db", "w+");
    }
    int len;
    fseek(fptr, 0, SEEK_END);  
    int len_of_file = ftell(fptr);  

    InputBuffer* input_buffer = NULL;
    input_buffer = get_inputbuffer();

    while(true){

        print_prompt();
        
        read_input_buffer(input_buffer);

        if (input_buffer->input_length == 0) {
            printf("Error reading input\n");
            free_buffer(input_buffer);
            continue;
        }

        if (input_buffer->buffer[0] ==  '.'){
            if (process_non_sql_statements(input_buffer->buffer) == EXIT_SUCCESS){
                    free_buffer(input_buffer);
                    // Write to File.
                    fclose(fptr);
                    exit(EXIT_SUCCESS);
            }
            else{
                printf("Unknown statement\n");
                continue;
            }
        }
        else{
            if (process_sql_statements(input_buffer->buffer, table, fptr) == EXIT_SUCCESS){
                    continue;
            }
            else{
                printf("Something Wrong\n");
                continue;
            }
        }
        free_buffer(input_buffer);


    }
    
    return 0;
}