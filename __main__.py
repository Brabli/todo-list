import sys
from src.Parser import Parser
from src.TodoList import TodoList

def main():
    args = Parser.parse_args(sys.argv[1:])
    TodoList.execute_args(args)
    TodoList.clean()
    TodoList.show()
    sys.exit()


if __name__ == '__main__':
  main()
