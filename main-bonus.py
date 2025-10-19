from art import text2art  
from colorama import Back, Fore, Style 

art1 = text2art("BELIEVE AND ACHEIVE", font="block")
print(Style.DIM, Back.LIGHTBLACK_EX ,Fore.YELLOW + art1)
art2 = text2art("HELLO", font="sub-zero")
print(Back.RED, Style.BRIGHT, Fore.BLACK + art2)
art3 = text2art("KEEP LEARNING", font="big")
print(Fore.YELLOW + Style.BRIGHT + art3)
art4 = text2art("PYTHON IS FUN", font="slant")
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + art4)
art5 = text2art("NEVER GIVE UP", font="block2")
print(Fore.RED + Back.BLACK + Style.BRIGHT + art5)



