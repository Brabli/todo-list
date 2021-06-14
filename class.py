#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"


import os
import sys
from pathlib import Path


all_args = sys.argv[1:]


class TodoList:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    path = "./todo_list.txt" if current_script_path == \
        "/Users/bradley/Desktop/Personal Projects/todo" else "/Users/bradley/bin/todo_list.txt"
    if not Path(path).exists():
        file = open(path, "w")
        file.close()

    @classmethod
    def show(cls):
        with open(cls.path, "r") as todo_list:
            print("\n#################\n### TODO LIST ###\n#################\n")
            all_items = todo_list.readlines()
            for i in range(len(all_items)):
                formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
                print(formatted_item)
            print("\n")

    @classmethod
    def clean(cls):
        with open(cls.path, 'r') as todo_list:
            all_items = todo_list.readlines()
        with open(cls.path, "w") as todo_list:
            for line in all_items:
                if line.strip():
                    todo_list.write(line)

    @classmethod
    def add(cls, item):
        """
        :param item: String, line to add to list.
        """
        with open(cls.path, "a") as todo_list:
            todo_list.write(item + "\n")
            print("Item added to list: " + item + ".")

    @classmethod
    def remove(cls, item_number):
        """
        :param item_number: Int, number of line to be removed.
        """
        item_index = item_number - 1
        with open(cls.path, "r") as todo_list:
            all_items = todo_list.readlines()
        with open(cls.path, "w") as todo_list:
            for i, item in enumerate(all_items):
                if i != item_index and item.strip() != "":
                    todo_list.write(item)


class Parser:

    @classmethod
    def parse(cls, args):
        """
        :param args: All args EXCEPT for first arg which is the filepath.
        """
        parsed_args = {
            "r": [],
            "i": []
        }
        for arg in args:
            if arg[0] == "-":
                if arg[1] == "r":
                    remove_numbers = arg[2:].split(",")
                    for number in remove_numbers:
                        parsed_args["r"].append(int(number))
            else:
                parsed_args["i"].append(arg)
        return parsed_args


    @classmethod
    def create_list_item(cls, all_args):
        item_args = list(filter(lambda item : item[0] != "-", all_args))
        todo_item = " ".join(item_args)
        return todo_item

    @classmethod
    def get_options(cls, all_args):
        options = []
        for arg in all_args:
            if arg[0] == "-":
                options.append(arg);
            else:
                break
        return options

    @classmethod
    def parse_options(cls, options):
        try:
            for option in options:
                letter = option[1]
                if letter == "r":
                    line_number = int(option[2:])
                    TodoList.remove(line_number)
                    print("Removed item " + str(line_number) + ".")
                    TodoList.show()
        except:
            print("Invalid option given!")
            sys.exit()



if (len(all_args) == 0):
    TodoList.show()
    sys.exit()

print(Parser.parse(all_args))

options = Parser.get_options(all_args)
Parser.parse_options(options)

if (len(all_args) > 0):
    item = Parser.create_list_item(all_args)
    TodoList.add(item)

sys.exit()


"""
Parser should split all the arguments into their own arrays
{
    r: [],
    item:
}

"""