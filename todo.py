#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"


#################
###  IMPORTS  ###
#################
import os
import sys
from pathlib import Path


#################
###  GLOBALS  ###
#################
current_script_path = os.path.dirname(os.path.realpath(__file__))

if current_script_path == "/Users/bradley/Desktop/Personal Projects/todo":
    todo_list_path = "./todo_list.txt"
else:
    todo_list_path = "/Users/bradley/bin/todo_list.txt"

# todo_list_path = "/Users/bradley/bin/todo_list.txt"
all_args = sys.argv[1:]

#################
### FUNCTIONS ###
#################
def create_todo_list():
    todo_list = Path(todo_list_path)
    if not todo_list.exists():
        file = open(todo_list_path, "w")
        file.close()

# args = array of strings to join
# This can be run after parse_options as all_args array will be updated
def create_list_item(args):
    with open(todo_list_path, "a") as todo_list:
        todo_item = " ".join(args)
        todo_list.write(todo_item + "\n")

# list_item = string, list item
def append_todo_item(list_item):
    with open(todo_list_path, "a") as todo_list:
        todo_list.write(list_item)

def show_todo_list():
    with open(todo_list_path, "r") as todo_list:
        print("\n#################\n### TODO LIST ###\n#################\n")
        all_items = todo_list.readlines()
        for i in range(len(all_items)):
            formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
            print(formatted_item)
        print("\n")

# args = array, global all_args
# Side effect: Removes option from all_args array.
def get_options(args):
    options = []
    for arg in args:
        if arg[0] == "-":
            options.append(arg);
            args.pop(0)
        else:
            break
    return options

# item_number = int, item number to remove
def remove_item(item_number):
    item_number = item_number - 1
    with open(todo_list_path, "r") as todo_list:
        all_items = todo_list.readlines()
    # Write mode removes contents of file, unlike append mode
    create_todo_list()
    with open(todo_list_path, "w") as todo_list:
        for i in range(len(all_items)):
            if i != item_number:
                todo_list.write(all_items[i])

# options = array, command options
def parse_options(all_args):
    try:
        for option in all_args:
            letter = option[1]
            # r = REMOVE
            if letter == "r":
                line_number = int(option[2:])
                remove_item(line_number)        
                print("Removed item " + str(line_number) + ".")      
    except:
        print("Invalid option given!")
        sys.exit()
    finally:
        pass
        #show_todo_list()


#################
###  SCRIPT   ###
#################
create_todo_list()

if (len(all_args) == 0):
    show_todo_list()
    sys.exit()

options = get_options(all_args)
parse_options(options)

if (len(all_args) > 0):
    create_list_item(all_args)

sys.exit()