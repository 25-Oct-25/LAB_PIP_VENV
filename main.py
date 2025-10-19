from art import text2art
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Print "BELIEVE AND ACHIEVE" in font 'block'
art1 = text2art("BELIEVE AND ACHIEVE", font="block")
print(Fore.CYAN + art1)

# Print "HELLO" in font 'sub-zero'
art2 = text2art("HELLO", font="sub-zero")
print(Fore.MAGENTA + art2)

# Bonus: your own phrase
art3 = text2art("NEVER GIVE UP", font="block")
print(Fore.YELLOW + art3)
