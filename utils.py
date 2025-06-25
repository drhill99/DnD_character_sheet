import os
import platform
import pickle

def clear_terminal():
    # OS is Windows
    if platform.system() == "Windows":
        os.system('cls')
    # OS is Unix/Linux
    else:
        os.system('clear')

def save_character(active_character):
    if active_character is not None:
        with open(f"{active_character.char_name}.pkl", "wb") as file:
            pickle.dump(active_character, file)

def load_character():
    char_to_load = input("Enter character name to load: ")
    with open(f"{char_to_load}.pkl", "rb") as file:
        return pickle.load(file)