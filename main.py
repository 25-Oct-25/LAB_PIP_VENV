from art import *
from colorama import Fore 



art_a=text2art("BELIEVE AND ACHEIVE",font='block',chr_ignore=True) 
print(Fore.RED + art_a)

art_b = text2art("HELLO", font="sub-zero")
print(Fore.GREEN + art_b)

art_c = text2art("SANA", font="rnd-xlarge")
print(Fore.BLUE + art_c)

tprint("PYTHON",font="rnd-small")
