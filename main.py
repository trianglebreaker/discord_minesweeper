import sys
import argparse
import pyperclip
import minesweeper

DEFAULT_DIMENSIONS = [9, 9] # width, height
DEFAULT_MINES = 10
DEFAULT_BLANK_EMOJI = "white_large_square"
DEFAULT_MINE_EMOJI = "boom"


# argparse stuff
DESCRIPTION_PRE = (
    "Generate a Minesweeper puzzle formatted as a Discord message, and copies it to the clipboard."
)
DESCRIPTION_POST = (
    "The puzzle is guaranteed to have a blank spot in the center of the board. "
    "As a result, the width and height will be adjusted to be odd if necessary. "
    "The minimum settings for a puzzle are a 7 by 7 puzzle with 5 mines."
)

parser = argparse.ArgumentParser(description = DESCRIPTION_PRE, epilog = DESCRIPTION_POST)
parser.add_argument("-d", "-dim", nargs = 2, type = int, metavar = ("width", "height"), help = "set custom width and height for the puzzle", default = DEFAULT_DIMENSIONS)
parser.add_argument("-m", "-mines", nargs = 1, type = int, metavar = "mines", help = "set the number of mines", default = DEFAULT_MINES)
parser.add_argument("-be", "-blank-emoji", nargs = 1, type = str, metavar = "blank_emoji_name", help = f"set custom emoji code for blank squares (default = \"{DEFAULT_BLANK_EMOJI}\")", default = DEFAULT_BLANK_EMOJI)
parser.add_argument("-me", "-mine-emoji", nargs = 1, type = str, metavar = "mine_emoji_name", help = f"set custom emoji code for mines (default = \"{DEFAULT_MINE_EMOJI}\")", default = DEFAULT_MINE_EMOJI)
args = parser.parse_args()


def print_and_quit(message):
    print(message)
    quit()

def main():    
    if __name__ == "__main__":
        print("helo")
    
    else:
        print_and_quit("Run this as a script please")


main()
