#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"


#################
###  IMPORTS  ###
#################
import os
import sys
import argparse
from pathlib import Path


#################
###  GLOBALS  ###
#################

current_script_path = os.path.dirname(os.path.realpath(__file__))

# parser = argparse.ArgumentParser()
# parser.parse_args()

todo_list_path = "./todo_list.txt" if current_script_path == "/Users/bradley/Desktop/Personal Projects/todo" else "/Users/bradley/bin/todo_list.txt"

all_args = sys.argv[1:]


#################
### FUNCTIONS ###
#################

def cleanup_list():
    with open(todo_list_path, 'r') as todo_list:
        all_items = todo_list.readlines()
    with open(todo_list_path, "w") as todo_list:
        for line in all_items:
            if line.strip():
                todo_list.write(line)

def create_todo_list():
    todo_list = Path(todo_list_path)
    if not todo_list.exists():
        file = open(todo_list_path, "w")
        file.close()

def remove_item(item_number):
    item_index = item_number - 1
    with open(todo_list_path, "r") as todo_list:
        all_items = todo_list.readlines()
    with open(todo_list_path, "w") as todo_list:
        for i, item in enumerate(all_items):
            if i != item_index and item.strip() != "":
                todo_list.write(item)

def show_todo_list():
    with open(todo_list_path, "r") as todo_list:
        print("\n#################\n### TODO LIST ###\n#################\n")
        all_items = todo_list.readlines()
        for i in range(len(all_items)):
            formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
            print(formatted_item)
        print("\n")

def create_list_item(all_args):
    item_args = list(filter(lambda item : item[0] != "-", all_args))
    todo_item = " ".join(item_args)
    if todo_item:
        with open(todo_list_path, "a") as todo_list:
            todo_list.write(todo_item + "\n")
            print("Item added to list: " + todo_item + ".")

def get_options(all_args):
    options = []
    for arg in all_args:
        if arg[0] == "-":
            options.append(arg);
        else:
            break
    return options

# options = array, command options
# options needs to be ["F", [12, 42, 5]] for example
# Make it so having multiple remove flags doesn't break shit
def parse_options(options):
    try:
        for option in options:
            letter = option[1]
            if letter == "r":
                line_number = int(option[2:])
                remove_item(line_number)
                print("Removed item " + str(line_number) + ".")
                show_todo_list()
    except:
        print("Invalid option given!")
        sys.exit()


#################
###  SCRIPT   ###
#################

create_todo_list()
cleanup_list()

if (len(all_args) == 0):
    show_todo_list()
    sys.exit()

options = get_options(all_args)
parse_options(options)

if (len(all_args) > 0):
    create_list_item(all_args)

sys.exit()
