#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COLUMN_USERNAME_SIZE 32
#define COLUMN_EMAIL_SIZE 255

void print_prompt(){
	printf("db > ");
}


typedef struct {
  char* buffer;
  size_t buffer_length;
  ssize_t input_length;
} InputBuffer;

typedef struct{
	char id[2];
	char name[COLUMN_USERNAME_SIZE];
	char email[COLUMN_EMAIL_SIZE];
} Row;


InputBuffer* get_inputbuffer(){
	InputBuffer* input_buffer = NULL;
	input_buffer = malloc(sizeof(InputBuffer));
	input_buffer->buffer = NULL;
	input_buffer->buffer_length = 0;
	input_buffer->input_length = 0;
	return input_buffer;
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

int process_sql_statements(char* statement){
	if (strncmp(statement, "insert", 6) == 0){
		printf("Insert statement will be processed\n");
		Row* row = get_row();	
		int index = 7;
		int length = strlen(statement);
		char c[length];
		int i = 0;
		int counter = 0;
		while (index < length){
			if (statement[index] == ' '){
				if (counter == 0){
					strcpy(row->id, c);
					i = 0;
					counter += 1;
				}
				else if (counter == 1){
					strcpy(row->name, c);
					i = 0;
					counter += 1;
				}
				else{
					printf("%d\n", counter);
					printf("Select statement is syntactically incorrect\n");
					printf("%s\n", row->id);
					return EXIT_FAILURE;
				}
				index += 1;
			}
			else{
				c[i] = statement[index];
				i += 1;
				c[i] = '\0';
				index += 1;
			}
		}
		strcpy(row->email, c);
		printf("%s\n", row->email);
		return EXIT_SUCCESS;
	}
	else if(strncmp(statement, "select", 6) == 0){
		printf("Select statement will be processed\n");
		return EXIT_SUCCESS;
	}
	else{
		return EXIT_FAILURE;
	}
}



int main(void)
{
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
					exit(EXIT_SUCCESS);
			}
			else{
				printf("Unknown statement\n");
				continue;
			}
		}
		else{
			if (process_sql_statements(input_buffer->buffer) == EXIT_SUCCESS){
					continue;
			}
			else{
				printf("Unknown statement\n");
				continue;
			}
		}
		free_buffer(input_buffer);
	}
	return 0;
}