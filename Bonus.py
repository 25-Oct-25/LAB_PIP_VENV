from art import *
from colorama import Fore, Style, Back, init

init(autoreset=True)

print(Fore.RED + text2art("BELIEVE", font="block"))
print(Fore.GREEN + text2art("ACHIEVE", font="cybermedium"))
print(Fore.BLUE + text2art("HELLO", font="sub-zero"))
print(Fore.MAGENTA + text2art("PYTHON", font="random"))
print(Fore.CYAN + text2art("TEXT ART", font="tarty1"))

print(Fore.YELLOW + "*" * 50)
print(Fore.YELLOW + text2art("WELCOME!", font="starwars"))
print(Fore.YELLOW + "*" * 50)
