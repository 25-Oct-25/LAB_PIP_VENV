from art import text2art
from colorama import Fore, Back, Style, init

init(autoreset=True)


phrase = text2art("BELIEVE AND ACHIEVE", font='block')
print(Fore.CYAN + phrase)


word = text2art("HELLO", font='sub-zero')
print(Back.WHITE + Fore.BLACK + word)


phrase1 = text2art("DON'T\nGIVE\nUP", font="random")
print(Fore.RED + phrase1)






