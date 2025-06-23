# python packages
import os
# local imports
import utils
from wizard_spell_table import display_spell_table
from wizard_spells import parse_arguments
from stats import display_skill, display_stats
from character import Character

utils.clear_terminal()

active_character = None
quit = None


while True:
    user_command = input("enter a command: ")
    utils.clear_terminal()
    parse_arguments(user_command)
    if user_command.lower() == "quit":
        break
    elif user_command.lower() == "home":
        utils.clear_terminal()
        continue
    elif user_command.lower() == "new character":
        new_character = Character()
        if new_character is not None:
            active_character = new_character
    elif user_command.lower() == "load character":
        utils.load_character()
if active_character is not None:
    utils.save_character(active_character)

