#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"


#################
###  IMPORTS  ###
#################
import os
import sys
from pathlib import Path


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


TodoList.add("This is a new item!")
TodoList.remove(7)
TodoList.show()
