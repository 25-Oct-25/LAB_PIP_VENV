from art import text2art, tprint
from colorama import init, Fore, Style

init(autoreset=True)

#__Task1___

belive_art = text2art("BELIEVE AND ACHIEVE", font="block")
print(Fore.YELLOW + belive_art)

tprint("HELLO",font="sub-zero")

#__bonus___

print(Fore.CYAN + text2art("KEEP GOING!", font="standard"))

print(Fore.MAGENTA + text2art("SUCCESS", font="italic"))
