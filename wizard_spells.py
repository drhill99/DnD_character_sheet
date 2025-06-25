wizard_spells = {
    "cantrip": {
        "acid splash"
        "Evocation Cantrip (Sorcerer, Wizard)\n": 
            """
            Acid Splash\n
            Casting Time: Action
            Range: 60 feet
            Components: V, S
            Duration: Instantaneous\n
            You create an acidic bubble at a point within range,
            where it explodes in a 5-foot-radius Sphere. Each 
            creature in that Sphere must succeed on a Dexterity
            saving throw or take 1d6 Acid damage.
                Cantrip Upgrade. The damage increases by 1d6
            when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6)
            """,
        "blade ward": """
        """,
        "chill touch": """
        """,
        "dancing lights": """
        """,
        "elementalism": """
        """,
        "fire bolt": """
        """,
        "friends": """
        """,
        "light": """
        """,
        "mage hand": """
        """,
        "mending": """
        """,
        "message": """
        """,
        "mind sliver": """
        """,
        "minor illusion": """
        """,
        "poison spray": """
        """,
        "prestidigitation": """
        """,
        "ray of frost": """
        """,
        "shocking grasp": """
        """,
        "thunderclap": """
        """,
        "toll the dead": """
        """,
        "true strike": """
        """,
    },
    "1": {
        "alarm": 
            """
            Alarm
            Level 1 Abjuration (Ranger, Wizard)\n
            Casting Time: 1 minute or Ritual
            Range: 30 feet
            Components: V, S, M (a bell and silver wire)
            Duration: 8 hours\n
            You set an alarm against intursion. Choose a door,
            a window, or an area within range that is no larger
            than a 20-foot Cube. Until the spell ends, an alarm 
            alerts you whenever a creature touches or enters 
            the warded area. When you cast the spell, you can
            designatre creates that won't set off the alarm. You
            also choose whether the alarm is audible or mental:\n
            Audible Alarm. The alarm produces the sound of 
                a handbell for 10 seconds within 60 feet
                of the warded area.
            Mental Alarm. You are alerted by a mental ping
                if you are within 1 mile of the warded area.
                This ping awakens you if you are asleep.

            """,
        "burning hands": """
        """,
        "charm person": """
        """,
        "chromatic spray": """
        """,
        "color spray": """
        """,
        "comprehend languages": """
        """,
        "detect magic": """
        """,
        "disguise self": """
        """,
        "expeditious retreat": """
        """,
        "false life": """
        """,
        "feather fall": """
        """,
        "find familiar": """
        """,
        "fog cloud": """
        """,
        "grease": """
        """,
        "iceknife": """
        """,
        "identify": """
        """,
        "illusory script": """
        """,
        "jump": """
        """,
        "longstrider": """
        """,
        "magearmor": """
        """,
        "magic missile": 
            """
            Magic Missile
            level 1 Evocation (Sorcerer, Wizard)\n
            Casting time: Action
            Range: 120 feet
            Component: V, S 
            Duration: Instantaneous\n
            You create three glowing darts of magical force.
            Each dart strikes a creature of your choice that 
            you can see within range. A dart deals 1d4 + 1 Force 
            damage to its target. The darts all strike simultane-
            ously, and you can direct them to hit one creature 
            or several.\n
                Using a higher-level spell slot: The spell creates one 
            more dart for each spell slot level above 1.
            """,
        "protection from evil and good": """
        """,
        "ray of sickness": """
        """,
        "shield": """
        """,
        "silent image": """
        """,
        "sleep": """
        """,
        "tashas hideous laughter": """
        """,
        "tensers floating disk": """
        """,
        "thunderwave": """
        """,
        "unseen servant": """
        """,
        "witch bolt": """
        """,
    },
    "2": {

    },
    "3": {

    },
    "4": {

    },
    "5": {

    },
    "6": {

    },
    "7": {

    },
    "8": {

    },
    "9": {

    }
}

def search_by(d, spell):
    if isinstance(d, dict):
        for key, value in d.items():
            match = 0
            for word in spell:
                if key.__contains__(word):
                    match += 1
            if match == len(spell):
                return value
            result = search_by(value, spell)
            if result is not None:
                return result

def details():
    pass

def parse_arguments(inc_arguments):
    # idx 0 = command
    # idx 1 = spell name
    # arguments = inc_arguments.split(' ')
    # command = arguments[0].lower()
    # spell = arguments[2:]
    print(inc_arguments)
    # if command == "details":
    print(search_by(wizard_spells, inc_arguments))

parse_arguments("details for magic missile")


    