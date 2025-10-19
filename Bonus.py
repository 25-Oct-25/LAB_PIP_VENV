from art import *
from colorama import Fore

first_word=decor("ball1")+decor("ball3") +decor("ball3",reverse=True)+decor("ball1") +"\n"+ text2art("        I", font='bulbhead')
second_word=decor("ball1")+decor("ball3") +decor("ball3",reverse=True)+decor("ball1") +"\n"+ text2art("   Love", font='bulbhead')
third_word=decor("ball1")+decor("ball3") +decor("ball3",reverse=True)+decor("ball1") +"\n"+ text2art("Basketball", font='bulbhead')+"\n"+decor("ball1")+decor("ball3") +decor("ball3",reverse=True)+decor("ball1")

print(Fore.BLUE + first_word)
print(Fore.CYAN + second_word)
print(Fore.BLUE + third_word)
