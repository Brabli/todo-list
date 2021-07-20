import os
from pathlib import Path
from typing import List
from .HistoryList import HistoryList
from .ColourString import ColourString

class TodoList:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    dev_script_path = "/Users/bradley/Personal Projects/todo/src"
    dev_todo_list_path = "./resources/todo_list.txt"
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
            cls.add(parsed_args["i"])

    @classmethod
    def show(cls):
        print(ColourString.colour("blue", "\n#################"))
        print(ColourString.colour("orange", "    TODO LIST    "))
        print(ColourString.colour("blue", "#################\n"))

        all_items = cls.__get_all_items()
        for i in range(len(all_items)):
            item_number = f"{str(i + 1)}. "
            item = all_items[i].strip()

            print(ColourString.multicolour({
                "orange": item_number,
                "none": item
            }))

        print("\n")

    @classmethod
    def clean(cls):
        all_items = cls.__get_all_items()
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
            print(ColourString.colour("green", f"Item added to list: {item}."))
            HistoryList.add(item, "ADDED")

    @classmethod
    def amend(cls, item_index, amended_item):
        """
        :param item_index: Int, item index to add to list.
        :param amended_item: String, string to replace the current item.
        """
        all_items = cls.__get_all_items()
        with open(cls.todo_list_path, "w") as todo_list:
            for i, current_item in enumerate(all_items):
                if (i != item_index):
                    item = current_item
                else:
                    item = amended_item + "\n"
                    HistoryList.add(amended_item, "AMENDED")
                todo_list.write(item)

    @classmethod
    def remove(cls, indicies_to_remove):
        """
        :param item_number: Int, number of line to be removed.
        """
        for item_index in indicies_to_remove:
            all_items = cls.__get_all_items()
            with open(cls.todo_list_path, "w") as todo_list:
                for i, item in enumerate(all_items):
                    if i != item_index and item.strip() != "":
                        todo_list.write(item)
                    else:
                        print(f"\nRemoved item {i + 1}: {item.strip()}")
                        HistoryList.add(item.strip(), "REMOVED")

    @classmethod
    def __get_all_items(cls) -> List[str]:
        with open(cls.todo_list_path, "r") as todo_list:
            all_items = todo_list.readlines()
            return all_items
