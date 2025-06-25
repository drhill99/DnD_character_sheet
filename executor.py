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
    user_command = input(
        """
        display character 
        load character
        new character
        spell <name>
        quit
        home
        enter a command: 
        """)
    # utils.clear_terminal()
    if user_command.lower() == "quit":
        utils.save_character(active_character)
        break
    elif user_command.lower() == "home":
        utils.clear_terminal()
        continue
    elif user_command.lower() == "new character":
        new_character = Character()
        if new_character is not None:
            active_character = new_character
            utils.save_character(active_character)
    elif user_command.lower().__contains__("spell"):
        parse_arguments(user_command.split(' ')[1:])
    elif user_command.lower() == "load character":
        active_character = utils.load_character()
    elif user_command.lower() == "display character":
        if active_character is not None:
            print("Printing character")
            print(active_character.stats)
            active_character.print_character_sheet(active_character.stats)
        
if active_character is not None:
    utils.save_character(active_character)

