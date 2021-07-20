from typing import Dict


class ColourString:
    colours = {
        "red": "\33[91m",
        "green": "\33[92m",
        "orange": "\33[93m",
        "blue": "\33[94m",
        "purple": "\33[95m",
        "cyan": "\33[96m",
        "white": "\33[37m",
        "none": ""
    }
    end_colour = "\033[0m"

    @classmethod
    def test_colours(cls) -> None:
        x = 0
        for i in range(24):
            colors = ""
            for j in range(5):
                code = str(x+j)
                colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
            print(colors)
            x = x + 5

    @classmethod
    def colour(cls, color: str, message: str) -> str:
        colour_code = cls.colours.get(color, "none");
        end_colour = cls.end_colour
        coloured_string = colour_code + message + end_colour
        return coloured_string

    @classmethod
    def multicolour(cls, format_dict: Dict):
        final_string = ""
        for colour, string in format_dict.items():
            final_string += cls.colour(colour, string)
        return final_string
