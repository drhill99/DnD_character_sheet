# python packages
import os
# local imports
import utils
from wizard_spell_table import display_spell_table
from wizard_spells import parse_arguments
from stats import display_skill, display_stats

stats = {
    "lvl": 6,
    "str": 9,
    "dex": 12,
    "con": 14,
    "int": 18,
    "wis": 11,
    "chr": 12
}

utils.clear_terminal()

quit = None
while True:
    print("")
    print("Ability Checks")
    print("''''''''''''''")
    display_skill(stats)
    print("")
    print("Character Stats")
    print("'''''''''''''''")
    display_stats(stats)
    print("")
    print("Spell Stats")
    print("'''''''''''")
    display_spell_table(stats)
    user_command = input("enter a command: ")
    utils.clear_terminal()
    parse_arguments(user_command)
    if user_command.lower() == "quit":
        break
    elif user_command.lower() == "home":
        utils.clear_terminal()
        continue