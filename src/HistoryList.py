import os
from datetime import datetime
from pathlib import Path

class HistoryList:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    dev_script_path = "/Users/bradley/Desktop/Personal Projects/todo/src"
    dev_history_path = "/Users/bradley/Desktop/Personal Projects/todo/resources/history.txt"
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
                formatted_item = all_items[i].strip()
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
            todo_list.write(dt_string + " " + action.upper() + " \"" + item + "\"\n")
