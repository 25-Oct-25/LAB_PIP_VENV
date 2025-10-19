from art import *
from colorama import init, Fore, Back, Style
init(autoreset=True)

tprint("BELIEVE AND ACHEIVE" , font="block")
tprint("HELLO", font="sub-zero")


tprint("MAHA SAUD", font="rand")

print(text2art('''python  
is 
great''', font="small"))

print("-"* 35)

print(Fore.GREEN + "BELIEVE AND ACHEIVE" + Style.RESET_ALL)
print(Back.LIGHTRED_EX + "HELLO" + Style.RESET_ALL)