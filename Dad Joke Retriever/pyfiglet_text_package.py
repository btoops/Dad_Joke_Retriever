import pyfiglet  # makes the text look like block letters
import colorama  # allows the color to display in terminal
from termcolor import colored  # gives the color value to text

colorama.init()
msg = input("Input text: ")
clr = input("Pick a color: ")
text = pyfiglet.figlet_format(msg)
colored_message = colored(text, color=clr)

print(colored_message)
