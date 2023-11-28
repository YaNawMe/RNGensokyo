import tkinter as tk
import os

class GameEditor:
    def __init__(self):
        # Initialize
        self.program = tk.Tk()
        self.program.title("Game Editor")
        self.program.resizable(0, 0)

        screen_width = self.program.winfo_screenwidth()
        screen_height = self.program.winfo_screenheight()
        program_width = screen_height // 2
        program_height = screen_height // 2
        offset_width = (screen_width - program_width) // 2
        offset_height = (screen_height - program_height) // 2

        self.program.geometry(f"{program_width}x{program_height}+{offset_width}+{offset_height}")

        # Image list
        self.collab_list: list[str]

        self.armor_images: list[list[str]] = []
        self.boots_images: list[list[str]] = []
        self.hand_images: list[list[str]] = []
        self.weapon_images: list[list[str]] = []
        self.material_images: list[list[str]] = []
        self.character_images: list[list[str]] = []

        # Data
        self.character_data: dict[str, dict[str, object]] = {}
        self.default_equip = {
            "slot": "weapon",
            "type": "wand",
            "name": "stick",
            "collab_name": "base",
            "level": 1,
            "stats": {
                "health": 0,
                "attack": 0,
                "defense": 0
            }
        }

        self.default_stats = {
            "health": 0,
            "attack": 0,
            "defense": 0,
            "collab_name": "base",
            "equips": {
                "weapon": self.default_equip,
                "armor": self.default_equip,
                "boots": self.default_equip,
                "hands": self.default_equip,
                "accessories": list[self.default_equip]
            }
        }

        # Preprocess
        self.read_data()

        # Start
        self.program.mainloop()


    def read_data(self):
        self.collab_list = [file for file in os.listdir("image") if "game" not in file]
        
        for collab in self.collab_list:
            for folder_type in os.listdir(f"image/{collab}"):
                files = [file[:-4] for file in os.listdir(f"image/{collab}/{folder_type}")]

                if folder_type == "armors":
                    self.armor_images.append(files)
                
                elif folder_type == "boots":
                    self.boots_images.append(files)
                
                elif folder_type == "hands":
                    self.hand_images.append(files)
                
                elif folder_type == "weapons":
                    self.weapon_images.append(files)
                
                elif folder_type == "materials":
                    self.material_images.append(files)
                
                elif folder_type == "characters":
                    self.character_images.append(files)


if __name__ == '__main__':
    # print(open(__file__).read())
    GameEditor()
