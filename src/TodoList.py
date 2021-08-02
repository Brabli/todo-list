import os
from pathlib import Path
from typing import List
from .HistoryList import HistoryList
from .ColourString import ColourString as c

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

    messages = []

    @classmethod
    def execute_args(cls, parsed_args):
        if len(parsed_args["r"]) > 0:
            cls.remove(parsed_args["r"])

        if len(parsed_args["a"]) != 0:
            if (parsed_args["i"] == ""):
                cls.add_message(c.colour("blue", f"Nothing to amend to item {parsed_args['a'][0] + 1}!"))
            else:
                cls.amend(parsed_args["a"][0], parsed_args["i"])
            return

        if len(parsed_args["A"]) != 0:
            if (parsed_args["i"] == ""):
                cls.add_message(c.colour("blue", f"Nothing to append to item {parsed_args['A'][0] + 1}!"))
            else:
                cls.append(parsed_args["A"][0], parsed_args["i"])
            return

        if parsed_args["i"] != "" and len(parsed_args["a"]) == 0 and len(parsed_args["A"]) == 0:
            cls.add(parsed_args["i"])

    @classmethod
    def show(cls):
        print(c.colour("blue", "\n#################"))
        print(c.colour("orange", "    TODO LIST    "))
        print(c.colour("blue", "#################\n"))

        all_items = cls.__get_all_items()

        num_items = len(all_items)

        if num_items <= 0:
            print(c.colour("green", "You've done everything, wow!"))

        else:
            for i in range(num_items):
                # Not sure if I like the alternate colours, but we'll see how I feel later
                colour = "cyan" if i % 2 == 0 else "white"
                item_number = f"{str(i + 1)}. "
                item = all_items[i].strip()
                print(c.multicolour({
                    "orange": item_number,
                    colour: item
                }))

        print("")
        cls.show_messages()

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
            cls.add_message(c.colour("green", f"Item added to list: {item}."))
            HistoryList.add(item, "ADDED")

    @classmethod
    def amend(cls, item_index, amended_item):
        """
        :param item_index: Int, item index to be amended.
        :param amended_item: String, string to replace the current item.
        """
        all_items = cls.__get_all_items()
        with open(cls.todo_list_path, "w") as todo_list:
            for i, current_item in enumerate(all_items):
                if (i != item_index):
                    item = current_item
                else:
                    item = amended_item + "\n"
                    cls.add_message(c.colour("blue", f"Item {item_index + 1} amended to: {amended_item}."))
                    HistoryList.add(amended_item, "AMENDED")

                todo_list.write(item)

    @classmethod
    def append(cls, item_index, text_to_append):
        """
        :param item_index: Int, item index to have text appended.
        :param text_to_append: String, string to append to the current item.
        """
        all_items = cls.__get_all_items()
        with open(cls.todo_list_path, "w") as todo_list:
            for i, current_item in enumerate(all_items):
                if (i != item_index):
                    item = current_item
                else:
                    # Removes uppercased first letter
                    text_to_append = text_to_append[0].lower() + text_to_append[1:]
                    item = f"{current_item.strip()} {text_to_append}\n"
                    cls.add_message(c.colour("blue", f"Item {item_index + 1} appended to: {item.strip()}."))
                    HistoryList.add(text_to_append, "APPENDED")

                todo_list.write(item)

    @classmethod
    def remove(cls, indicies_to_remove: List):
        """
        :param indicies_to_remove: List, number of line to be removed.
        """
        for item_index in indicies_to_remove:
            all_items = cls.__get_all_items()
            with open(cls.todo_list_path, "w") as todo_list:
                for i, item in enumerate(all_items):
                    if i != item_index and item.strip() != "":
                        todo_list.write(item)
                    else:
                        cls.add_message(c.colour("red", f"Removed item {i + 1}: {item.strip()}"))
                        HistoryList.add(item.strip(), "REMOVED")

    @classmethod
    def __get_all_items(cls) -> List[str]:
        with open(cls.todo_list_path, "r") as todo_list:
            all_items = todo_list.readlines()
            return all_items

    @classmethod
    def get_num_items(cls) -> int:
        return len(cls.__get_all_items())

    @classmethod
    def add_message(cls, msg: str) -> None:
        msg = msg if msg.strip() == msg else msg.strip()
        cls.messages.append(msg)

    @classmethod
    def show_messages(cls) -> None:
        if (len(cls.messages)) > 0:
            for msg in cls.messages:
                print(msg)
            print("")

