class ColourPrint:
    colours = {
        "red": "\33[91m",
        "green": "\33[92m",
        "orange": "\33[93m",
        "blue": "\33[94m",
        "purple": "\33[95m",
        "cyan": "\33[96m"
    }
    end_colour = "\033[0m"

    @classmethod
    def __test_colours(cls) -> None:
        x = 0
        for i in range(24):
            colors = ""
            for j in range(5):
                code = str(x+j)
                colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
            print(colors)
            x = x + 5

    @classmethod
    def print(cls, color: str, message: str) -> None:
        colour_code = cls.colours[color];
        end_colour = cls.end_colour
        coloured_string = colour_code + message + end_colour
        print(coloured_string)
