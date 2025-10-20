from art import text2art
from colorama import Fore, Style, init


art1 = text2art("BELIEVE AND ACHIEVE", font='block')
art2 = text2art("HELLO", font='sub-zero')
art3 = text2art("NEVER GIVE UP", font='random')
art4 = text2art("SUCCESS", font='graffiti')


print(Fore.CYAN + art1)
print(Fore.MAGENTA + art2)
print(Fore.GREEN + art3)
print(Fore.YELLOW + art4)
