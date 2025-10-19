from colorama import Fore, Back, Style
from art import text2art
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + text2art("PYTHON", font="block"))
print(Fore.MAGENTA + text2art("IS FUN", font="sub-zero"))
print(Fore.YELLOW + text2art("KEEP GOING", font="bubble"))


