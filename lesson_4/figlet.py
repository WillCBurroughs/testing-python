import sys
from pyfiglet import Figlet

def main():

    if len(sys.argv) == 1:
        randomize_font()
    
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit
        else:
            randomize_font(sys.argv[2])


def randomize_font(font_given = "slant"):
    text_given = input("Input: ")
    f = Figlet(font=font_given)
    ascii_art = f.renderText(text_given)
    print(ascii_art)


main()