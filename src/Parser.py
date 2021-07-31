import sys
from .HistoryList import HistoryList
from .TodoList import TodoList
from .ColourString import ColourString as c
class Parser:
    @classmethod
    def parse_args(cls, args: list) -> dict:
        """
        :param args: All args EXCEPT for first arg which is the filepath.
        """
        # Why do I need a hard coded args dict?
        parsed_args = { "r": [], "i": [], "a": [] }
        # r: remove, i: item, a: amend, h: history

        try:
            for arg in args:
                if arg[0] == "-":
                    option = arg[1]
                    if option == "r":
                        lines_to_remove = arg[2:].split(",")
                        for line_num in lines_to_remove:
                            # if not isinstance(line_num, int):
                            #     raise ValueError("Must specify at least one integer argument for -r!")
                            if line_num == "0":
                                item_index = TodoList.get_num_items() - 1
                            else:
                                item_index = int(line_num) - 1
                            parsed_args["r"].append(item_index)

                    elif option == "a":
                        line_to_amend = arg[2:]
                        # if not isinstance(line_to_amend, int):
                        #     raise ValueError("Must specify an integer argument for -a!")
                        index_to_amend = int(line_to_amend) - 1
                        parsed_args["a"].append(index_to_amend)

                    elif option == "h":
                        # Crude af will change this later
                        HistoryList.show()
                        sys.exit()

                    elif option == "":
                        None

                else:
                    parsed_args["i"].append(arg)
        except ValueError as e:
            print()
            # print(c.colour("red", f"ERROR: {str(e)}"))
            print(c.colour("red", f"ERROR: Incorrect or no args found for given option/s!"))

        parsed_args["r"] = list(set(parsed_args["r"]))
        parsed_args["r"].sort(reverse = True)
        parsed_args["i"] = cls.create_list_item(parsed_args["i"])

        return parsed_args

    @classmethod
    def create_list_item(cls, word_list):
        if len(word_list) != 0:
            word_list[0] = word_list[0].capitalize()
        todo_item = " ".join(word_list)
        return todo_item
