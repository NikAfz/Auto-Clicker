import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset = True)

def tip():
  tips = Fore.WHITE + Back.RED + "you can stop the program by pressing the " + Back.MAGENTA + " S " + Fore.WHITE + Back.RED + " key"
  return tips
