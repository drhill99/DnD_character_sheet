abil_mod_idx = 0
prof_idx = 1

modifiers = [
    [0, 2],  # 0
    [-5, 2], # 1
    [-4, 2], # 2
    [-4, 2], # 3
    [-3, 2], # 4
    [-3, 3], # 5
    [-2, 3], # 6
    [-2, 3], # 7
    [-1, 3], # 8
    [-1, 4], # 9
    [0, 4], # 10
    [0, 4], # 11
    [1, 4], # 12
    [1, 5], # 13
    [2, 5], # 14
    [2, 5], # 15
    [3, 5], # 16
    [3, 6], # 17
    [4, 6], # 18
    [4, 6], # 19
    [5, 6], # 20
    [5, 7], # 21
    [6, 7], # 22
    [6, 7], # 23
    [7, 7], # 24
    [7, 8], # 25
    [8, 8], # 26
    [8, 8], # 27
    [9, 8], # 28
    [9, 9], # 29
    [10, 9], # 30
    ]

def display_stats(stats):
    
    stats_display = []
    stats_header = ["LVL", "INIT", "SPELL DC", "SPELL ATK", "STR", "DEX", "CON", "INT", "WIS", "CHR"]
    stats_display.append(stats_header)
    stat_values = []
    for stat in stats_header:
        if stat == "INIT":
            stat_values.append(modifiers[stats['dex']][abil_mod_idx])
        elif stat == "SPELL DC":
            stat_values.append(modifiers[stats['int']][abil_mod_idx] + modifiers[stats['lvl']][prof_idx] + 8)
        elif stat == "SPELL ATK":
            stat_values.append(modifiers[stats['int']][abil_mod_idx])
        else:
            stat_values.append(stats[stat.lower()])
    widths = [len(item) + 2 for item in stats_header]
    total_width = sum(widths)
    stats_display.append("".join("'" for _ in range(total_width)))
    stats_display.append(stat_values)
    format_string = "".join(f"{{:^{w}}}" for w in widths)
    for i, row in enumerate(stats_display):
        if i == 1:
            print(row)
        else:
            print(format_string.format(*row))

def display_skill(stats):
    skill_display = []
    # skill_header = {
    #     "Acrobatics": "dex", 
    #     "Animal_Handling": "wis", 
    #     "Arcana": "int", 
    #     "Athletics": "str", 
    #     "Deception": "chr", 
    #     "History": "int", 
    #     "Insight": "wis", 
    #     "Intimidation": "chr", 
    #     "Investigation": "int", 
    #     "Medicine": "wis", 
    #     "Nature": "int", 
    #     "Perception": "wis", 
    #     "Performance": "chr", 
    #     "Persuasion": "chr", 
    #     "Religion": "int", 
    #     "Sleight_of_Hand": "dex", 
    #     "Stealth": "dex", 
    #     "Survival": "wis"
    # }
    skill_header = {
        "Acro": "dex", 
        "Anim_Hand": "wis", 
        "Arcana": "int", 
        "Athl": "str", 
        "Decep": "chr", 
        "History": "int", 
        "Insight": "wis", 
        "Intimi": "chr", 
        "Invest": "int", 
        "Medicine": "wis", 
        "Nature": "int", 
        "Percep": "wis", 
        "Perform": "chr", 
        "Persuasion": "chr", 
        "Religion": "int", 
        "Sleight_of_Hand": "dex", 
        "Stealth": "dex", 
        "Survival": "wis"
    }
    skill_display.append(skill_header.keys())
    skill_mod_sources = skill_header.values()
    widths = [len(item) + 2 for item in skill_header.keys()]
    total_widths = sum(widths)
    skill_display.append("".join("'" for _ in range(total_widths)))
    stat_values = [modifiers[stats[stat]][abil_mod_idx] + modifiers[stats['lvl']][prof_idx] for stat in skill_mod_sources]
    skill_display.append(stat_values)
    format_string = "".join(f"{{:^{w}}}" for w in widths)

    for i, row in enumerate(skill_display):
        if i == 1:
            print(row)
        else:
            print(format_string.format(*row))

characteristics = """
Darkvision. You can see in dim light within 120 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.


Gift of the Svirfneblin. Starting at 3rd level, you can cast the Disguise Self spell with this trait. Starting at 5th level, you can also cast the Nondetection spell with it, without requiring a material component. Once you cast either of these spells with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast these spells using spell slots you have of the appropriate level.
Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).
Gnomish Magic Resistance. You have advantage on Intelligence, Wisdom, and Charisma saving throws against spells.
Svirfneblin Camouflage. When you make a Dexterity (Stealth) check, you can make the check with advantage. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.
Languages. Your character can speak, read, and write Common and one other language that you and your DM agree is appropriate for the character. The Player’s Handbook offers a list of languages to choose from. The DM is free to modify that list for a campaign.
"""

