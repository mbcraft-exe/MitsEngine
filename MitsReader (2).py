import colorama
import os
os.system("pip install Mits-Engine")
import engine

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

version = "Reader v1.0"
date = "2022"
out = ""

print(Fore.YELLOW + "Mits Reader")
print(Fore.YELLOW + f"© MB INC {date} | {version}")

while out != "broke;":
    out = input(">>> ")
    if out == "[update] - Mits":
        os.system("pip install --upgrade Mits-Engine")
    engine.code(out)