

from art import *
from colorama import Fore, Back, Style

Art = text2art("BELIEVE\nAND\nACHIEVE",font='block',chr_ignore=True)
print(Art)

Art2 = text2art("HELLO", font = 'sub-zero')
print(Art2)

Art3 = text2art("WORLD", font = 'small')
print(Art3)

print(Back.LIGHTRED_EX + "I Love Python" + Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + "Hello World" + Style.RESET_ALL)