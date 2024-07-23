import os
import random
import re

from rich.console import Console
from rich.prompt import IntPrompt, Prompt
from rich.progress import track
from rich.table import Table

from dataclasses import dataclass

class DigiPrompt(Prompt):
    prompt_suffix = " > "


class DigiIntPrompt(IntPrompt):
    prompt_suffix = " > "

console = Console()

RE_BG_IMAGE = r'image (.+)\s?=\s?"(bg.+)"'
RE_CHAR_IMAGE = r'^\s*?image (.+)\s?=\s?"(.*:?characters.+)"'
RE_PROP = r'image (.+)\s?=\s?"((?!.*:?characters|bg.+).+)"'
RE_CHARACTER = r'define (.+)\s?=\s?Character\("(.*)",\s?callback\s?=\s?(.*)\)'
RE_BGM = r'define audio\.(?!sfx)(.+)\s?=\s?"(.+)"'
RE_SFX = r'define audio\.(?=sfx)(.+)\s?=\s?"(.+)"'
RE_TRANSFORM = r'transform (.+):'

SCRAMBLE_BG_IMAGES = True
SCRAMBLE_CHAR_IMAGES = True
SCRAMBLE_PROPS = True
SCRAMBLE_CHAR_NAMES = True
SCRAMBLE_BGM = True
SCRAMBLE_SFX = True
SCRAMBLE_TRANSFORMS = True

@dataclass
class Replacement:
    line_num: int
    var_name: str
    replacement: str
    original_line: str
    callback: str = None
    indent_level: int = 0

def scramble():
    lines = []
    new_lines = []

    bg_images = []
    char_images = []
    prop_images = []
    char_names = []
    bgms = []
    sfxs = []
    transforms = []

    console.clear()
    console.print("[blue]Loading lines...")

    # Load the script_start
    with open("./script_start.rpy") as f:
        lines = f.readlines()
        new_lines = [None] * len(lines)

    console.print("[blue]Backing up old script...")

    # Rename the old script start
    os.rename("script_start.rpy", "script_start.rpybu")

    # Read lines
    for n, line in track(enumerate(lines), "[blue]Reading lines...", len(lines)):
        if (m := re.match(RE_BG_IMAGE, line)) and "Movie" not in line and "Window" not in line and SCRAMBLE_BG_IMAGES:
            bg_images.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_CHAR_IMAGE, line)) and "Movie" not in line and "Window" not in line and SCRAMBLE_CHAR_IMAGES:
            indent = (len(line) - len(line.lstrip())) // 4
            char_images.append(Replacement(n, m.group(1), m.group(2), line, indent_level = indent))
        elif (m := re.match(RE_PROP, line)) and "Movie" not in line and "Window" not in line and SCRAMBLE_PROPS:
            prop_images.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_CHARACTER, line)) and SCRAMBLE_CHAR_NAMES:
            char_names.append(Replacement(n, m.group(1), m.group(2), line, m.group(3)))
        elif (m := re.match(RE_BGM, line)) and SCRAMBLE_BGM:
            bgms.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_SFX, line)) and SCRAMBLE_SFX:
            sfxs.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_TRANSFORM, line)) and SCRAMBLE_TRANSFORMS:
            transforms.append(Replacement(n, m.group(1), m.group(1), line))
        else:
            new_lines[n] = line
    
    # Randomize values
    possible_bgs = [j.replacement for j in bg_images]
    possible_char_images = [j.replacement for j in char_images]
    possible_props = [j.replacement for j in prop_images]
    possible_char_names = [j.replacement for j in char_names]
    possible_bgms = [j.replacement for j in bgms]
    possible_sfxs = [j.replacement for j in sfxs]
    possible_transforms = [j.replacement for j in transforms]

    if SCRAMBLE_BG_IMAGES:
        console.print(f"[blue]Scrambling {len(bg_images)} BGs...")
        for i in bg_images:
            random_value = random.choice(possible_bgs)
            new_line = f"image {i.var_name} = \"{random_value}\"\n"
            new_lines[i.line_num] = new_line
            possible_bgs.remove(random_value)

    if SCRAMBLE_CHAR_IMAGES:
        console.print(f"[blue]Scrambling {len(char_images)} character sprites...")
        for i in char_images:
            random_value = random.choice(possible_char_images)
            new_line = f"image {i.var_name} = \"{random_value}\"\n"
            new_line = (" " * i.indent_level * 4) + new_line
            new_lines[i.line_num] = new_line
            possible_char_images.remove(random_value)

    if SCRAMBLE_PROPS:
        console.print(f"[blue]Scrambling {len(prop_images)} props...")
        for i in prop_images:
            random_value = random.choice(possible_props)
            new_line = f"image {i.var_name} = \"{random_value}\"\n"
            new_lines[i.line_num] = new_line
            possible_props.remove(random_value)

    if SCRAMBLE_CHAR_NAMES:
        console.print(f"[blue]Scrambling {len(char_names)} character names...")
        for i in char_names:
            random_value = random.choice(possible_char_names)
            new_line = f"define {i.var_name} = Character(\"{random_value}\", callback = {i.callback})\n"
            new_lines[i.line_num] = new_line
            possible_char_names.remove(random_value)

    if SCRAMBLE_BGM:
        console.print(f"[blue]Scrambling {len(bgms)} BGMs...")
        for i in bgms:
            random_value = random.choice(possible_bgms)
            new_line = f"define audio.{i.var_name} = \"{random_value}\"\n"
            new_lines[i.line_num] = new_line
            possible_bgms.remove(random_value)

    if SCRAMBLE_SFX:
        console.print(f"[blue]Scrambling {len(sfxs)} SFX...")
        for i in sfxs:
            random_value = random.choice(possible_sfxs)
            new_line = f"define audio.sfx{i.var_name} = \"{random_value}\"\n"
            new_lines[i.line_num] = new_line
            possible_sfxs.remove(random_value)

    if SCRAMBLE_TRANSFORMS:
        console.print(f"[blue]Scrambling {len(transforms)} transforms...")
        for i in transforms:
            random_value = random.choice(possible_transforms)
            new_line = f"transform {random_value}:\n"
            new_lines[i.line_num] = new_line
            possible_transforms.remove(random_value)

    console.print("[blue]Writing new script...")
    # Replace script_start
    with open("./script_start.rpy", "w") as f:
        f.writelines(new_lines)

    exit(0)

def get_cs_names():
    c_names = ["Crappy", "Cool", "Crazy", "Cooky", "Candy", "Cheesy", "Creamy", "Cookie", "Compu", "Cheerful", "Chaotic", "Cash"]
    s_names = ["Streamer", "Sucker", "Server", "Serve", "Steamer", "Singer", "Sausage", "Saturday", "Sunday", "Steve", "Spender", "Stomper"]

    all_names = []
    for c in c_names:
        for s in s_names:
            all_names.append(c + s)
    
    all_names.extend(["CS", "cs", "cS", "Cs", "cs188creations", "cs188returns", "cs188streams", "C.S. One Hundred And Eighty Eight"])

    return all_names

def oops():
    lines = []
    new_lines = []

    char_images = []
    char_names = []

    console.clear()
    console.print("[blue]Loading lines...")

    # Load the script_start
    with open("./script_start.rpy") as f:
        lines = f.readlines()
        new_lines = [None] * len(lines)

    console.print("[blue]Backing up old script...")

    # Rename the old script start
    if not os.path.isfile("script_start.rpybu"):
        os.rename("script_start.rpy", "script_start.rpybu")

    # Read lines
    for n, line in track(enumerate(lines), "[blue]Reading lines...", len(lines)):
        if (m := re.match(RE_CHAR_IMAGE, line)) and "Movie" not in line and "Window" not in line:
            indent = (len(line) - len(line.lstrip())) // 4
            char_images.append(Replacement(n, m.group(1), m.group(2), line, indent_level = indent))
        elif (m := re.match(RE_CHARACTER, line)):
            char_names.append(Replacement(n, m.group(1), m.group(2), line, m.group(3)))
        else:
            new_lines[n] = line
    
    # Randomize values
    possible_char_images = [j.replacement for j in char_images if "cs" in j.replacement]
    possible_char_names = get_cs_names()

    console.print(f"[blue]CSing {len(char_images)} character sprites...")
    for i in char_images:
        random_value = random.choice(possible_char_images)
        new_line = f"image {i.var_name} = \"{random_value}\"\n"
        new_line = (" " * i.indent_level * 4) + new_line
        new_lines[i.line_num] = new_line

    console.print(f"[blue]CSing {len(char_names)} character names...")
    for i in char_names:
        if i.var_name.strip() == "cs":
            new_line = i.original_line
            new_lines[i.line_num] = new_line
        else:
            random_value = random.choice(possible_char_names)
            new_line = f"define {i.var_name} = Character(\"{random_value}\", callback = renpy.partial(char_callback, name = \"cs\", beep = \"cs\"))\n"
            new_lines[i.line_num] = new_line

    console.print("[blue]Writing new script...")
    # Replace script_start
    with open("./script_start.rpy", "w") as f:
        f.writelines(new_lines)

    exit(0)

def unscramble():
    console.clear()
    console.print("[blue]Reverting script_start...")
    # Remove the new script start
    os.remove("./script_start.rpy")

    # Rename the old script start
    os.rename("script_start.rpybu", "script_start.rpy")

    exit(0)

def get_current_options_table() -> Table:
    t = Table("Scramble?", "Y/N", "#", title = "What would you like scrambled?")
    t.add_row("Background Images", ":white_check_mark:" if SCRAMBLE_BG_IMAGES else ":x:", "1")
    t.add_row("Character Images", ":white_check_mark:" if SCRAMBLE_CHAR_IMAGES else ":x:", "2")
    t.add_row("Props", ":white_check_mark:" if SCRAMBLE_PROPS else ":x:", "3")
    t.add_row("Character Names", ":white_check_mark:" if SCRAMBLE_CHAR_NAMES else ":x:", "4")
    t.add_row("Music", ":white_check_mark:" if SCRAMBLE_BGM else ":x:", "5")
    t.add_row("Sound Effects", ":white_check_mark:" if SCRAMBLE_SFX else ":x:", "6")
    t.add_row("Transforms", ":white_check_mark:" if SCRAMBLE_TRANSFORMS else ":x:", "7")
    t.caption = "Choose a number to toggle."

    return t

def choose_scramble_options():
    global SCRAMBLE_BG_IMAGES, SCRAMBLE_BGM, SCRAMBLE_CHAR_IMAGES, SCRAMBLE_CHAR_NAMES, SCRAMBLE_SFX, SCRAMBLE_PROPS, SCRAMBLE_TRANSFORMS
    console.clear()

    if os.path.isfile("./script_start.rpybu"):
        console.print(":warning: [bold yellow]Your game is in a scrambled state. Please unscramble first.")
        exit()

    console.print(get_current_options_table())
    choice = DigiPrompt.ask("Choose a number, or hit ENTER to scramble!", choices = ["1", "2", "3", "4", "5", "6", "7", ""])
    if choice == "":
        scramble()
    elif choice == "1":
        SCRAMBLE_BG_IMAGES = not SCRAMBLE_BG_IMAGES
    elif choice == "2":
        SCRAMBLE_CHAR_IMAGES = not SCRAMBLE_CHAR_IMAGES
    elif choice == "3":
        SCRAMBLE_PROPS = not SCRAMBLE_PROPS
    elif choice == "4":
        SCRAMBLE_CHAR_NAMES = not SCRAMBLE_CHAR_NAMES
    elif choice == "5":
        SCRAMBLE_BGM = not SCRAMBLE_BGM
    elif choice == "6":
        SCRAMBLE_SFX = not SCRAMBLE_SFX
    elif choice == "7":
        SCRAMBLE_TRANSFORMS = not SCRAMBLE_TRANSFORMS
    else:
        console.print(":warning: [bold yellow]Invalid option.")
    choose_scramble_options()


def choose(clear = True):
    if clear:
        console.clear()
    choice = DigiIntPrompt.ask("Scramble (1) or unscramble (2)?\nOr, Oops, All CS! (3)?", choices = ["1", "2", "3"])
    if choice == 1:
        choose_scramble_options()
    elif choice == 2:
        unscramble()
    elif choice == 3:
        oops()
    else:
        console.print(":warning: [bold yellow]Invalid option.")
        choose(False)

def main():
    choose()

if __name__ == "__main__":
    main()
