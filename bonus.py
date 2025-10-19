import art
from colorama import Fore, Back, Style
phrase1 = art.text2art("Hello there", font ='random', chr_ignore=True)
print(Fore.MAGENTA+ phrase1)

phrase2 = art.text2art("The Danger", font ="random", chr_ignore=True)

print(Style.BRIGHT +Fore.CYAN+ phrase2)