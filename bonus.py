from art import *
from colorama import Fore, Back, Style




art = text2art("HELLO", font="letters")

colored_art = ""
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]

for i, line in enumerate(art.splitlines()): # Each line has a color
    colored_art += colors[i % len(colors)] + line + "\n"

print(colored_art)





art2 = text2art("HELLO",font='block')
colored_art = Back.CYAN + art2
print(colored_art)


#print(FONT_NAMES)