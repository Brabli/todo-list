#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"

import os
import sys
from datetime import datetime
from pathlib import Path

class TodoList:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    dev_script_path = "/Users/bradley/Desktop/Personal Projects/todo"
    dev_todo_list_path = "./todo_list.txt"
    live_todo_list_path = "/Users/bradley/bin/todo_list.txt"

    if current_script_path == dev_script_path:
        todo_list_path = dev_todo_list_path
    else:
        todo_list_path = live_todo_list_path

    if not Path(todo_list_path).exists():
        file = open(todo_list_path, "w")
        file.close()

    @classmethod
    def execute_args(cls, parsed_args):
        if len(parsed_args["r"]) > 0:
            cls.remove(parsed_args["r"])

        if len(parsed_args["a"]) != 0:
            cls.amend(parsed_args["a"][0], parsed_args["i"])
            return

        if parsed_args["i"] != "" and len(parsed_args["a"]) == 0:
            cls.add(args["i"])

    @classmethod
    def show(cls):
        with open(cls.todo_list_path, "r") as todo_list:
            print("\n#################\n### TODO LIST ###\n#################\n")
            all_items = todo_list.readlines()
            for i in range(len(all_items)):
                formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
                print(formatted_item)
            print("\n")

    @classmethod
    def clean(cls):
        with open(cls.todo_list_path, 'r') as todo_list:
            all_items = todo_list.readlines()
        with open(cls.todo_list_path, "w") as todo_list:
            for line in all_items:
                if line.strip():
                    todo_list.write(line)

    @classmethod
    def add(cls, item):
        """
        :param item: String, line to add to list.
        """
        with open(cls.todo_list_path, "a") as todo_list:
            todo_list.write(item + "\n")
            print("Item added to list: " + item + ".")
            History.add(item, "ADDED")

    @classmethod
    def amend(cls, item_index, amended_item):
        """
        :param item_index: Int, item index to add to list.
        :param amended_item: String, string to replace the current item.
        """
        with open(cls.todo_list_path, "r") as todo_list:
            all_items = todo_list.readlines()

        with open(cls.todo_list_path, "w") as todo_list:
            for i, current_item in enumerate(all_items):
                if (i != item_index):
                    item = current_item
                else:
                    item = amended_item + "\n"
                    History.add(amended_item, "AMENDED")
                todo_list.write(item)


    @classmethod
    def remove(cls, item_numbers):
        """
        :param item_number: Int, number of line to be removed.
        """
        for item_number in item_numbers:
            item_index = item_number
            with open(cls.todo_list_path, "r") as todo_list:
                all_items = todo_list.readlines()

            with open(cls.todo_list_path, "w") as todo_list:
                for i, item in enumerate(all_items):
                    if i != item_index and item.strip() != "":
                        todo_list.write(item)
                    else:
                        print(f"\nRemoved item {i + 1}: {item.strip()}")
                        History.add(item.strip(), "REMOVED")

class History:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    dev_script_path = "/Users/bradley/Desktop/Personal Projects/todo"
    dev_history_path = "./history.txt"
    live_history_path = "/Users/bradley/bin/history.txt"

    if current_script_path == dev_script_path:
        history_path = dev_history_path
    else:
        history_path = live_history_path

    if not Path(history_path).exists():
        file = open(history_path, "w")
        file.close()

    @classmethod
    def show(cls):
        with open(cls.history_path, "r") as todo_list:
            print("\n#################\n### HISTORY ###\n#################\n")
            all_items = todo_list.readlines()
            for i in range(len(all_items)):
                formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
                print(formatted_item)
            print("\n")

    @classmethod
    def clean(cls):
        with open(cls.history_path, 'r') as todo_list:
            all_items = todo_list.readlines()
        with open(cls.history_path, "w") as todo_list:
            for line in all_items:
                if line.strip():
                    todo_list.write(line)

    @classmethod
    def add(cls, item: str, action: str) -> None:
        """
        :param item: String, line to add to list.
        :param action: String, Action taken, ADDED, REMOVED, AMENDED.
        """
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(cls.history_path, "a") as todo_list:
            todo_list.write(action.upper() + " " + item + " " + dt_string + "\n")


class Parser:
    @classmethod
    def parse_args(cls, args: list) -> dict:
        """
        :param args: All args EXCEPT for first arg which is the filepath.
        """
        # Why do I need a hard coded args dict?
        parsed_args = { "r": [], "i": [], "a": [] }
        # r: remove, i: item, a: amend
        for arg in args:
            if arg[0] == "-":
                option = arg[1]

                if option == "r":
                    lines_to_remove = arg[2:].split(",")
                    for line_num in lines_to_remove:
                        item_index = int(line_num) - 1
                        parsed_args["r"].append(item_index)

                elif option == "a":
                    line_to_amend = arg[2:]
                    index_to_amend = int(line_to_amend) - 1
                    parsed_args["a"].append(index_to_amend)

                elif option == "h":
                    # Crude af will change this later
                    History.show()
                    sys.exit()

                elif option == "":
                    None

            else:
                parsed_args["i"].append(arg)

        parsed_args["r"].sort(reverse = True)
        parsed_args["i"] = cls.create_list_item(parsed_args["i"])

        return parsed_args

    @classmethod
    def create_list_item(cls, word_list):
        if len(word_list) != 0:
            word_list[0] = word_list[0].capitalize()
        todo_item = " ".join(word_list)
        return todo_item

args = Parser.parse_args(sys.argv[1:])
TodoList.execute_args(args)
TodoList.clean()
TodoList.show()
sys.exit()
