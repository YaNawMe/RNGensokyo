import tkinter
import os

files = os.listdir("img")

if "game_logo.png" in files:
    files.remove("game_logo.png")

if "aya2.png" in files:
    files.remove("aya2.png")

files = [file[:-4] for file in files]

default_equip = {
    "slot": "weapon",
    "type": "wand",
    "name": "stick",
    "level": 1,
    "stats": {
        "hp": 0,
        "atk": 0,
        "def": 0
    }
}

default_stats = {
    "hp": 50,
    "atk": 10,
    "def": 40,
    "equips": {
        "weapon": default_equip,
        "armor": ...,
        "boots": ...,
        "hands": ...,
        "accessories": []
    }
}

char_data = {files[i]: default_stats for i in range(len(files))}

[print(key, value) for key, value in char_data.items()]

class GameEditor:
    def __init__(self):
        pass

if __name__ == '__main__':
    GameEditor()