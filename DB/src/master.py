"""
This file contains pythonic implementation of sqllite db.
"""

import sys


INSERT_STATEMENT = "insert_statement"
SELECT_STATEMENT = "select_statement"

class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

        # __str__ is to print() the value

    def __str__(self):
        return (repr(self.value))


class Statement(object):
    """
    This class object stores the parsed statements.
    """
    def __init__(self):
        self.type = None
        self.statement = None


class Row(object):
    """
    This class stores the row of the database table.
    """

def check_valid_command(command):
    """
    This function checks if the entered command is valid or not.
    :param command:
    :return:
    """
    if len(command) == 0:
        return False


def handle_meta_commands(command):
    """
    This function handles the non-sql commands.
    :param command: entered command from the console
    :return: Recognised command or not.
    """
    if command == ".exit":
        sys.exit(0)
    else:
        try:
            raise MyError("Unrecognised Meta Command: '%s'" % command)
        except MyError as e:
            raise e


def prepare_statement(command, statement):
    """
    This function processes the sql commands.
    :param command: entered command from the console
    :return: valid command with correct syntax or not.
    """

    if command.startswith("select"):
        statement.type = SELECT_STATEMENT
        return "Its a select query"
    elif command.startswith("insert"):
        statement.type = INSERT_STATEMENT
        return "Its a select query"
    else:
        try:
            raise MyError("Unrecognised SQL statement: '%s'" % command)
        except MyError as e:
            raise e


def execute_statement(statement):
    """
    This function executes the statement
    :param statement: statement
    :return:
    """
    if statement.type == INSERT_STATEMENT:
        print("Insert statement will be executed")
    elif statement.type == SELECT_STATEMENT:
        print("Select statement will be executed")
    else:
        print("Something wrong with the statement")


if __name__ == '__main__':

    while True:
        command = input("db > ")
        if command[0] == ".":
            try:
                handle_meta_commands(command)
            except MyError as e:
                print(e.value)
        else:
            try:
                prepare_statement(command)
            except MyError as e:
                print(e.value)

    import ctypes
    print(ctypes.ARRAY(5))