#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COLUMN_USERNAME_SIZE 32
#define COLUMN_EMAIL_SIZE 255


// Error codes.
 enum PrepareResult_t {
   PREPARE_SUCCESS,
   PREPARE_NEGATIVE_ID,
   PREPARE_STRING_TOO_LONG,
   PREPARE_SYNTAX_ERROR,
   PREPARE_UNRECOGNIZED_STATEMENT,
   MAXIMUM_PAGES_REACHED
  };


// Reading the Table and Pager Information from File.

// This structure defines a datastructure to store the data from file.
typedef struct
{
    short page_number;
    void* page;
} Pager;


void print_prompt(){
    printf("db > ");
}


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




const int ID_SIZE = sizeof(((Row*)0)->id);
const int NAME_SIZE = sizeof(((Row*)0)->name);
const int EMAIL_SIZE = sizeof(((Row*)0)->email);
const int ROW_SIZE = ID_SIZE + NAME_SIZE + EMAIL_SIZE;

const int id_offset = 0;
const int name_offset = id_offset + ID_SIZE;
const int email_offset = name_offset + NAME_SIZE;

// Initialising page size with 4 bytes.
const int page_size = 4096;
const int max_pages = 100;
const int max_rows_per_page = page_size/ROW_SIZE;



typedef struct{
    short rows_inserted;
    short pages_used;
    Pager* pager;
} Table;

Table* initialise_tabel(){
    Table* table = malloc(sizeof((Table*)0));
    table->rows_inserted = -1;
    table->pages_used = -1;
    Pager* pager = malloc(sizeof((Pager*)0));
    pager->page_number = -1;
    pager->page = NULL;
    table->pager = pager;
    return table;
}

InputBuffer* get_inputbuffer(){
    InputBuffer* input_buffer = NULL;
    input_buffer = malloc(sizeof(InputBuffer));
    input_buffer->buffer = NULL;
    input_buffer->buffer_length = 0;
    input_buffer->input_length = 0;
    return input_buffer;
}


void set_filepointer_to_start_of_data(Table* table, FILE* fptr){
    fseek(fptr, 0, SEEK_SET);
    // Moving pointer to start of page data after
    fseek(fptr, sizeof(table->rows_inserted) * 2, SEEK_SET);
}

void free_object(void* object){
    free(object);
}

void free_buffer(InputBuffer* input_buffer){
    free(input_buffer->buffer);
    free(input_buffer);
}

void read_input_buffer(InputBuffer* input_buffer){
    input_buffer->input_length = getline(&(input_buffer->buffer), &(input_buffer->buffer_length),  stdin);
    // Strip()
    input_buffer->buffer[input_buffer->input_length - 1] = 0;
    input_buffer->input_length -= 1;
}


int process_non_sql_statements(char* statement){
    if (strcmp(statement, ".exit") == 0){
            printf("Closing DB connection");
            return EXIT_SUCCESS;
        }
    return EXIT_FAILURE;
}

Row* get_row(){
    Row* row = NULL;
    row = malloc(sizeof(Row));
    return row;
}

void serialize(Row* source, void* destination){
    /*
    This function serialises data. Copies data from source which is of type row 
    to destination address starting with destination.
    */
    memcpy(destination+id_offset, &(source->id), ID_SIZE);
    memcpy(destination+name_offset, source->name, NAME_SIZE);
    memcpy(destination+email_offset, source->email, EMAIL_SIZE);
}

void desrialise(void* source, Row* destination){
    /*
    This function Copies data from address location starting with source to Row* 
    */
    memcpy(&(destination->id), source+id_offset, ID_SIZE);
    memcpy(&(destination->name), source+name_offset, NAME_SIZE);
    memcpy(&(destination->email), source+email_offset, EMAIL_SIZE);

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

    // if (row->id < 0){
    //  printf("%s\n", "ID should be greater than zero.");
    //  return PREPARE_NEGATIVE_ID;
    // }
    table->rows_inserted += 1;
    int row_number = table->rows_inserted;
    int page_number = row_number/max_rows_per_page;

    if(page_number >= max_pages){
        printf("%s\n", "Maximum Pages reached");
        return MAXIMUM_PAGES_REACHED;
    }
    // Checking if we need to create a new page.
    void *page = table->pager->page;
    page = table->pager->page = malloc(page_size);
    if (page_number > table->pages_used){
        table->pages_used += 1;
    }
    else{
        // We have to load page from the File.
        printf("%s\n", "Here");
        fseek(fptr, page_number*page_size, SEEK_CUR);
        fread(page, page_size, 1, fptr);
        set_filepointer_to_start_of_data(table, fptr);
    }

    table->pager->page_number = page_number;

    // Required number of the row in a page.
    int row_number_in_page = row_number%max_rows_per_page;
    uint32_t row_number_address = (row_number_in_page * ROW_SIZE);
    serialize(row, page + row_number_address);
    printf("%s:%d\n", "Row inserted", row_number);
    return EXIT_SUCCESS;
    // Freeing space occupuied by row.
}


void fetch_row_from_table(int id, Row* row, Table* table){
    /*
    This function uses the row id to fetch particular row.
    */
    int page_number = id/max_rows_per_page;
    int row_number_in_page = id%max_rows_per_page;
    uint32_t row_number_address = (row_number_in_page * ROW_SIZE);
    desrialise(table->pager->page+row_number_address,row);
    printf("%s\n", row->email);
}

void print_all_rows(Row* row, Table* table){
    int start_row;
    for(start_row=0; start_row <= table->rows_inserted;start_row++){
        int page_number = start_row/max_rows_per_page;
        int row_number_in_page = start_row%max_rows_per_page;
        uint32_t row_number_address = (row_number_in_page * ROW_SIZE);
        desrialise(table->pager->page+row_number_address,row);
        printf("%d,%s,%s\n", row->id, row->name, row->email);
    }
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
        // if(insert_row_into_table(row, table) == EXIT_FAILURE){
        //  printf("%s\n", "Maximum pages have been stored.");
        //  return EXIT_FAILURE;
        // }
        free_object(row);
        return EXIT_SUCCESS;

    }
    // Adding support to print all the rows
    else if(strncmp(statement, "select_all", 10) == 0){
        Row* row = get_row();
        print_all_rows(row, table);
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




// Write a function to close the file pointers, free the memory of objects.


int main(void)
{
    FILE *fptr;
    fptr = fopen("Database.db", "ab+");
    if (fptr == NULL){
        printf("%s\n", "Cannot open database file");
        return 0;
    }
    int len;
    fseek(fptr, 0, SEEK_END);  
    int len_of_file = ftell(fptr);  

    InputBuffer* input_buffer = NULL;
    input_buffer = get_inputbuffer();

    // Initialise the table with default parameters.
    // Initialise the pager also.
    Table* table = initialise_tabel();
    if (len_of_file != 0){
        // Checking if there is some data data in DB or not.
        // Moving fptr to start of the file.
        fseek(fptr, 0, SEEK_SET);
        // reading the rows_inserted and pages_used from the file.
        fread(&table->rows_inserted, sizeof(table->rows_inserted), 1, fptr);
        // Moving pointer to start of pages_used.
        fseek(fptr, sizeof(table->rows_inserted), SEEK_SET);
        fread(&table->pages_used, sizeof(table->pages_used), 1, fptr);
    }

    while(true){
        if (len_of_file != 0){
            set_filepointer_to_start_of_data(table, fptr);
        }

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
                    fseek(fptr, 0, SEEK_SET);
                    fwrite(&table->rows_inserted, sizeof(table->rows_inserted), 1, fptr);
                    // Moving pointer to start of pages_used.
                    fseek(fptr, sizeof(table->rows_inserted), SEEK_SET);
                    fwrite(&table->pages_used, sizeof(table->pages_used), 1, fptr);
                    
                    // Copying the Stored Page.
                    set_filepointer_to_start_of_data(table, fptr);
                    fseek(fptr, table->pager->page_number*page_size, SEEK_CUR);
                    fwrite(table->pager->page, page_size, 1, fptr);

                    // Writing the page.
                    free_object(table);
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
                printf("Unknown statement\n");
                continue;
            }
        }
        free_buffer(input_buffer);
    }
    fclose(fptr);  
    return 0;
}