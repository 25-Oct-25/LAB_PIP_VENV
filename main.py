from art import *
from colorama import *

init(autoreset=True)

# Main phrases
art_1 = text2art("BELIEVE AND ACHIEVE", font="block")
art_2 = "HELLO"

print(art_1)
tprint(art_2, font="sub-zero")

# Bonus
print(Fore.CYAN + text2art("Hello World!", font="small"))
print(Fore.LIGHTBLACK_EX + text2art("Abdulrahman", font="fancy5"))