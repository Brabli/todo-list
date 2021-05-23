#!/usr/local/bin/python3
import os
import sys
from pathlib import Path



filepath = sys.argv[0]
args = sys.argv[1:]

print(filepath)
print(args)

#sys.exit()

def create_todo_list():
    todo_list = Path("./todo_list.txt")
    if not todo_list.exists():
        print("Initialising todo list.")
        file = open("todo_list.txt", "w")
        file.write("TODO LIST\n################")
        file.close("todo_list.txt")