from colorama import Fore, Back, Style
from colorama import init
from art import text2art 
from art import *

init(autoreset=True)
print(Fore.LIGHTBLUE_EX +text2art('Hello Word',font='cybermedium'))
print(Fore.BLUE + 'My name is :')
tprint("Lama")
print(Back.CYAN + 'Graduted at computer Scince')
print(Style.DIM + 'Study web devlop by python')
print(Fore.LIGHTBLUE_EX +text2art('Thank you','rand'))


