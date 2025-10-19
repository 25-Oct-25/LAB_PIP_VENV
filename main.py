from art import text2art

# Print the first phrase
art1 = text2art("BELIEVE AND ACHEIVE", font='block')
print(art1)

# Print the second phrase
art2 = text2art("HELLO", font='sub-zero')
print(art2)

from art import text2art
from colorama import Fore, Style

print(Fore.RED + text2art("BELIEVE AND ACHEIVE", font='block'))

print(Fore.CYAN + text2art("HELLO", font='sub-zero'))

print(Fore.GREEN + text2art("NEVER GIVE UP", font='tarty'))

print(Style.RESET_ALL)
