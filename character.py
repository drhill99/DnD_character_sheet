from wizard_spell_table import display_spell_table, prepared_spells
from wizard_spells import parse_arguments
from stats import display_skill, display_stats
import random

class Character:
    def __init__(self):
        self.char_class = ""
        self.char_name = ""
        # self.stats = {
        #     "lvl": 6,
        #     "str": 9,
        #     "dex": 12,
        #     "con": 14,
        #     "int": 18,
        #     "wis": 11,
        #     "chr": 12
        # }
        self.stats = {
            "lvl": 1,
            "str": 0,
            "dex": 0,
            "con": 0,
            "int": 0,
            "wis": 0,
            "chr": 0
        }
        self.spell_list = []
        self.items = {
            "head": {
                "attuned": False,
                "item": None
                },
            "armor": {
                "attuned": False,
                "item": None
            },
            "belt": {
                "attuned": False,
                "item": None
            },
            "gloves": {
                "attuned": False,
                "item": None
            },
            "ring_1": {
                "attuned": False,
                "item": None
            },
            "ring_2": {
                "attuned": False,
                "item": None
            },
            "amulet": {
                "attuned": False,
                "item": None
            },
            "weapon": {
                "attuned": False
            }
        }
        self.build_character()

    def build_character(self):
        print("Building new character...")
        self.char_name = input("Character Name: ")
        self.char_class = input("Character Class: ")
        generate_stats = input("Roll or enter stats manually?: ")
        if generate_stats.lower() == "roll":
            keep_stats = "no"
            while keep_stats == "no":
                self.stats['str'] = random.randint(3,18)
                self.stats['dex'] = random.randint(3,18)
                self.stats['con'] = random.randint(3,18)
                self.stats['int'] = random.randint(3,18)
                self.stats['wis'] = random.randint(3,18)
                self.stats['chr'] = random.randint(3,18)
                for key, value in self.stats.items():
                    print(f"{key}: {value}")
                keep_stats = input("keep stats?: ")
        elif generate_stats.lower() == "manually":
            for key in self.stats.keys():
                self.stats[key] = int(input(f"enter {key}: "))
        if self.char_class == "Wizard":
            if len(self.spell_list) == 0:
                for i in range(prepared_spells(self.stats)):
                    self.spell_list.append(input("add spell: "))
            

    def print_character_sheet(self, stats):
        print("")
        print("Ability Checks")
        print("''''''''''''''")
        display_skill(stats)
        print("")
        print("Character Stats")
        print("'''''''''''''''")
        display_stats(stats)
        if self.char_class.lower() == "wizard":
            print("")
            print("Spell Stats")
            print("'''''''''''")
            display_spell_table(stats)
            print("Prepared spells:")
            for spell in self.spell_list:
                print(spell)
            
