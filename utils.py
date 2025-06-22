import os
import platform

def clear_terminal():
    # OS is Windows
    if platform.system() == "Windows":
        os.system('cls')
    # OS is Unix/Linux
    else:
        os.system('clear')