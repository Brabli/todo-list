import sys
from src.Parser import Parser
from src.TodoList import TodoList

def main():
    # Pass all cli arguments (excluding the first arg which is always a filepath)
    # into the parser to turn them into a dictionary.
    args = Parser.parse_args(sys.argv[1:])
    TodoList.execute_args(args)
    TodoList.clean()
    TodoList.show()
    sys.exit()

if __name__ == '__main__':
  main()
