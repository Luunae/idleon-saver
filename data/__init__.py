from itertools import chain

skill_names = [
    "Character",
    "Mining",
    "Smithing",
    "Choppin'",
    "Fishing",
    "Alchemy",
    "Catching",
    "Trapping",
    "Construction",
    "Worship",
]

statue_names = [
    "Power Statue",
    "Speed Statue",
    "Mining Statue",
    "Feasty Statue",
    "Health Statue",
    "Kachow Statue",
    "Lumberbob Statue",
    "Thicc Skin Statue",
    "Oceanman Statue",
    "Ol Reliable Statue",
    "Exp Book Statue",
    "Anvil Statue",
    "Cauldron Statue",
    "Beholder Statue",
    "Bullseye Statue",
    "Box Statue",
    "Twosoul Statue",
    "EhExPee Statue",
    "Seesaw Statue",
]

card_names = {
    "mushG": "Green Mushroom",
    "mushR": "Red Mushroom",
    "frogG": "Frog",
    "beanG": "Bored Bean",
    "slimeG": "Slime",
    "snakeG": "Baby Boa",
    "carrotO": "Carrotman",
    "goblinG": "Glublin",
    "plank": "Wode Board",
    "frogBIG": "Gigafrog",
    "poopSmall": "Poop",
    "ratB": "Rat",
    "branch": "Walking Stick",
    "acorn": "Nutto",
    "Crystal0": "Crystal Carrot",
    "mushW": "Wood Mushroom",
    "jarSand": "Sandy Pot",
    "mimicA": "Mimic",
    "crabcake": "Crabcake",
    "coconut": "Mafioso",
    "sandcastle": "Sand Castle",
    "pincermin": "Pincermin",
    "potato": "Mashed Potato",
    "steak": "Tyson",
    "moonman": "Moonmoon",
    "sandgiant": "Sand Giant",
    "snailZ": "Snelbie",
    "shovelR": "Dig Doug",
    "Crystal1": "Crystal Crabal",
    "Bandit_Bob": "Bandit Bob",
    "Copper": "Copper Ore",
    "Iron": "Iron Ore",
    "Gold": "Gold Ore",
    "ForgeA": "Fire Forge",
    "OakTree": "Oak Logs",
    "BirchTree": "Bleach Logs",
    "JungleTree": "Jungle Logs",
    "ForestTree": "Forest Fibres",
    "Fish1": "Goldfish",
    "Fish2": "Hermit Can",
    "Fish3": "Jellyfish",
    "Bug1": "Fly",
    "Bug2": "Butterfly",
    "Plat": "Platinum Ore",
    "Dementia": "Dementia Ore",
    "Void": "Void Ore",
    "ForgeB": "Cinder Forge",
    "PalmTree": "Tropilogs",
    "ToiletTree": "Potty Rolls",
    "StumpTree": "Veiny Logs",
    "Fish4": "Bloach",
    "Bug3": "Sentient Cereal",
    "Bug4": "Fruitfly",
    "SoulCard1": "Forest Soul",
    "SoulCard2": "Dune Soul",
    "CritterCard1": "Froge",
    "CritterCard2": "Crabbo",
    "CritterCard3": "Scorpie",
    "sheep": "Sheepie",
    "flake": "Frost Flake",
    "stache": "Sir Stache",
    "bloque": "Bloque",
    "mamoth": "Mamooth",
    "snowball": "Snowman",
    "penguin": "Penguin",
    "thermostat": "Thermister",
    "glass": "Quenchie",
    "snakeB": "Cryosnake",
    "speaker": "Bop Box",
    "eye": "Neyeptune",
    "ram": "Dedotated Ram",
    "skele": "Xylobone",
    "skele2": "Bloodbone",
    "Crystal2": "Crystal Cattle",
    "Tree7": "Wispy Lumber",
    "SoulCard3": "Rooted Soul",
    "SoulCard4": "Frigid Soul",
    "SoulCard5": "Squiddy Soul",
    "CritterCard4": "Mousey",
    "CritterCard5": "Owlio",
    "CritterCard6": "Pingy",
    "CritterCard7": "Bunny",
    "Lustre": "Lustre Ore",
    "SaharanFoal": "Tundra Logs",
    "Bug5": "Mosquisnow",
    "Bug6": "Flycicle",
    "babayaga": "Baba Yaga",
    "poopBig": "Dr. Defecaus",
    "poopD": "Boop",
    "wolfA": "Normal Amarok",
    "wolfB": "Chaotic Amarok",
    "babaHour": "Biggie Hours",
    "babaMummy": "King Doot",
    "Boss2A": "Normal Efaunt",
    "Boss2B": "Chaotic Efaunt",
    "Boss3A": "Chizoar",
    "Boss3B": "Chaotic Chizoar",
    "ghost": "Ghost",
    "xmasEvent": "Giftmas Blobulyte",
    "xmasEvent2": "Meaning of Giftmas",
    "slimeR": "Valentslime",
    "loveEvent": "Loveulyte",
    "loveEvent2": "Choco Box",
    "sheepB": "Floofie",
    "snakeY": "Shell Snake",
    "EasterEvent1": "Egggulyte",
    "EasterEvent2": "Egg Capsule",
    "SummerEvent1": "Coastiolyte",
    "SummerEvent2": "Summer Spirit",
    "shovelY": "Plasti Doug",
    "crabcakeB": "Mr Blueberry",
}

stamp_names = {
    0: "Sword Stamp",
    1: "Heart Stamp",
    2: "Mana Stamp",
    3: "Tomahawk Stamp",
    4: "Target Stamp",
    5: "Shield Stamp",
    6: "Longsword Stamp",
    7: "Kapow Stamp",
    8: "Fist Stamp",
    9: "Battleaxe Stamp",
    10: "Agile Stamp",
    11: "Vitality Stamp",
    12: "Book Stamp",
    13: "Manamoar Stamp",
    14: "Clover Stamp",
    15: "Scimitar Stamp",
    16: "Bullseye Stamp",
    17: "Feather Stamp",
    18: "Polearm Stamp",
    19: "Violence Stamp",
    20: "Buckler Stamp",
    21: "FILLER",
    22: "Sukka Foo",
    23: "Arcane Stamp",
    24: "FILLER",
    25: "Steve Sword",
    26: "Blover Stamp",
    27: "Stat Graph Stamp",
    28: "FILLER",
    29: "FILLER",
    30: "FILLER",
    31: "FILLER",
    1000: "Pickaxe Stamp",
    1001: "Hatchet Stamp",
    1002: "Anvil Zoomer Stamp",
    1003: "Lil' Mining Baggy Stamp",
    1004: "Twin Ores Stamp",
    1005: "Choppin' Bag Stamp",
    1006: "Duplogs Stamp",
    1007: "Matty Bag Stamp",
    1008: "Smart Dirt Stamp",
    1009: "Cool Diggy Tool Stamp",
    1010: "High IQ Lumber Stamp",
    1011: "Swag Swingy Tool Stamp",
    1012: "Alch Go Brrr Stamp",
    1013: "Brainstew Stamps",
    1014: "Drippy Drop Stamp",
    1015: "Droplots Stamp",
    1016: "Fishing Rod Stamp",
    1017: "Fishhead Stamp",
    1018: "Catch Net Stamp",
    1019: "Fly Intel Stamp",
    1020: "Bag o Heads Stamp",
    1021: "Holy Mackerel Stamp",
    1022: "Bugsack Stamp",
    1023: "Buzz Buzz Stamp",
    1024: "Hidey Box Stamp",
    1025: "Purp Froge Stamp",
    1026: "Spikemouth Stamp",
    1027: "Blank",
    1028: "Blank",
    1029: "Stample Stamp",
    1030: "Saw Stamp",
    1031: "Blank",
    1032: "Blank",
    1033: "Flowin Stamp",
    1034: "Blank",
    1035: "Banked Pts Stamp",
    2000: "Questin Stamp",
    2001: "Mason Jar Stamp",
    2002: "Crystallin",
    2003: "Blank",
    2004: "Apple Stamp",
    2005: "Potion Stamp",
    2006: "Golden Apple Stamp",
    2007: "Blank",
    2008: "Card Stamp",
    2009: "Blank",
    2010: "Blank",
    2011: "Blank",
    2012: "Talent I Stamp",
    2013: "Talent II Stamp",
    2014: "Talent III Stamp",
    2015: "Talent IV Stamp",
    2016: "Talent V Stamp",
    2017: "Talent S Stamp",
    2018: "Multikill Stamp",
    2019: "Biblio Stamp",
}

bag_names = {
    "InvBag1": "Inventory Bag A",
    "InvBag2": "Inventory Bag B",
    "InvBag3": "Inventory Bag C",
    "InvBag4": "Inventory Bag D",
    "InvBag5": "Inventory Bag E",
    "InvBag6": "Inventory Bag F",
    "InvBag7": "Inventory Bag G",
    "InvBag8": "Inventory Bag H",
    "InvBag9": "Inventory Bag I",
    "InvBag100": "Snakeskinventory Bag",
    "InvBag101": "Totally Normal And Not Fake Bag",
    "InvBag102": "Blunderbag",
    "InvBag103": "Sandy Satchel",
    "InvBag104": "Bummo Bag",
    "InvBag105": "Capitalist Case",
    "InvBag106": "Wealthy Wallet",
    "InvBag107": "Prosperous Pouch",
    "InvBag108": "Sack of Success",
    "InvBag109": "Shivering Sack",
    "InvBag110": "Mamooth Hide Bag",
}

gem_bag_names = {
    "InvBag21": "Inventory Bag U",
    "InvBag22": "Inventory Bag V",
    "InvBag23": "Inventory Bag W",
    "InvBag24": "Inventory Bag X",
    "InvBag25": "Inventory Bag Y",
    "InvBag26": "Inventory Bag Z",
}

storage_names = {
    "InvStorage1": "Storage Chest 1",
    "InvStorage2": "Storage Chest 2",
    "InvStorage3": "Storage Chest 3",
    "InvStorage4": "Storage Chest 4",
    "InvStorage5": "Storage Chest 5",
    "InvStorage6": "Storage Chest 6",
    "InvStorage7": "Storage Chest 7",
    "InvStorage8": "Storage Chest 8",
    "InvStorage9": "Storage Chest 9",
    "InvStorage10": "Storage Chest 10",
    "InvStorage11": "Storage Chest 11",
    "InvStorage12": "Storage Chest 12",
    "InvStorage13": "Storage Chest 13",
    "InvStorage14": "Storage Chest 14",
    "InvStorage15": "Storage Chest 15",
    "InvStorage16": "Storage Chest 16",
    "InvStorage17": "Storage Chest 17",
    "InvStorage18": "Storage Chest 18",
    "InvStorage19": "Storage Chest 19",
    "InvStorage20": "Storage Chest 20",
    "InvStorage21": "Storage Chest 21",
    "InvStorage31": "Storage Chest 90",
    "InvStorage32": "Storage Chest 91",
    "InvStorage33": "Storage Chest 92",
    "InvStorage34": "Storage Chest 93",
    "InvStorage35": "Storage Chest 94",
    "InvStorage36": "Storage Chest 95",
    "InvStorage37": "Storage Chest 96",
    "InvStorage38": "Storage Chest 97",
    "InvStorage39": "Storage Chest 98",
    "InvStorage40": "Storage Chest 99",
    "InvStorage41": "Storage Chest 99B",
    "InvStorage42": "Storage Chest 99C",
    "InvStorageF": "Dank Paypay Chest",
}

pouch_names = {
    "Mining": "Mining",
    "Chopping": "Choppin",
    "Foods": "Food",
    "bCraft": "Materials",
    "Fishing": "Fish",
    "Bugs": "Bug",
    "Critters": "Critter",
    "Souls": "Soul",
}

pouch_sizes = {
    25: "Miniature",
    50: "Cramped",
    100: "Small",
    250: "Average",
    500: "Sizable",
    1000: "Big",
    2000: "Large",
}

starsign_ids = {
    "The_Book_Worm": "1",
    "The_Buff_Guy": "1a",
    "The_Fuzzy_Dice": "1b",
    "Flexo_Bendo": "2",
    "Dwarfo_Beardus": "3",
    "Hipster_Logger": "4",
    "Pie_Seas": "4a",
    "Miniature_Game": "4b",
    "Shoe_Fly": "4c",
    "Pack_Mule": "5",
    "Pirate_Booty": "6",
    "All_Rounder": "7",
    "Muscle_Man": "7a",
    "Fast_Frog": "7b",
    "Smart_Stooge": "7c",
    "Lucky_Larry": "7d",
    "Fatty_Doodoo": "8",
    "Robinhood": "9",
    "Blue_Hedgehog": "9a",
    "Ned_Kelly": "10",
    "The_Fallen_Titan": "10a",
    "Chronus_Cosmos": "CR",
    "Activelius": "11",
    "Gum_Drop": "11a",
    "Mount_Eaterest": "12",
    "Bob_Build_Guy": "13",
    "The_Big_Comatose": "14",
    "Sir_Savvy": "14a",
    "Silly_Snoozer": "15",
    "The_Big_Brain": "15a",
    "Grim_Reaper": "16",
    "The_Forsaken": "16a",
    "The_OG_Skiller": "17",
    "Mr_No_Sleep": "18",
}

constellation_names = list(
    chain.from_iterable([f"{c}-{i}" for i in range(1, 13)] for c in "AB")
)

cog_datas_map = {
    "a": "build_rate",
    "c": "flaggy_rate",
    "d": "exp_mult",
    "b": "exp_rate",
    "e": "build_rate_boost",
    "g": "flaggy_rate_boost",
    "k": "flaggy_speed",
    "f": "exp_rate_boost",
}

cog_boosts = "defg"

cog_type_map = {
    "ad": "Plus",
    "di": "X",
    "up": "Up",  # guess
    "do": "Down",
    "ri": "Right",
    "le": "Left",
    "ro": "Row",  # guess
    "co": "Col",  # guess
}
