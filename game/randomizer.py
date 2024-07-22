import os
import random
import re
import rich
from dataclasses import dataclass

SCRAMBLE_BG_IMAGES = True
SCRAMBLE_CHAR_IMAGES = True
SCRAMBLE_CHAR_NAMES = True
SCRAMBLE_BGM = True
SCRAMBLE_SFX = True

RE_BG_IMAGE = r'image (.+)\s?=\s?"(bg.+)"'
RE_CHAR_IMAGE = r'image (.+)\s?=\s?"(characters.+)"'
RE_CHARACTER = r'define (.+)\s?=\s?Character\("(.*)",\s?callback\s?=\s?(.*)\)'
RE_BGM = r'define audio\.(?!sfx)(.+)\s?=\s?"(.+)"'
RE_SFX = r'define audio\.(?=sfx)(.+)\s?=\s?"(.+)"'

@dataclass
class Replacement:
    line_num: int
    var_name: str
    replacement: str
    original_line: str
    callback: str = None


def scramble():
    lines = []
    new_lines = []

    bg_images = []
    char_images = []
    char_names = []
    bgms = []
    sfxs = []

    print("Loading lines...")

    # Load the script_start
    with open("./script_start.rpy") as f:
        lines = f.readlines()
        new_lines = [None] * len(lines)

    print("Backing up old script...")

    # Rename the old script start
    os.rename("script_start.rpy", "script_start.rpybu")

    print("Reading lines...")

    # Read lines
    for n, line in enumerate(lines):
        if (m := re.match(RE_BG_IMAGE, line)) and "Movie" not in line and "Window" not in line and SCRAMBLE_BG_IMAGES:
            bg_images.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_CHAR_IMAGE, line)) and "Movie" not in line and "Window" not in line and SCRAMBLE_CHAR_IMAGES:
            char_images.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_CHARACTER, line)) and SCRAMBLE_CHAR_NAMES:
            char_names.append(Replacement(n, m.group(1), m.group(2), line, m.group(3)))
        elif (m := re.match(RE_BGM, line)) and SCRAMBLE_BGM:
            bgms.append(Replacement(n, m.group(1), m.group(2), line))
        elif (m := re.match(RE_SFX, line)) and SCRAMBLE_SFX:
            sfxs.append(Replacement(n, m.group(1), m.group(2), line))
        else:
            new_lines[n] = line
    
    # Randomize values
    possible_bgs = [j.replacement for j in bg_images]
    possible_char_images = [j.replacement for j in char_images]
    possible_char_names = [j.replacement for j in char_names]
    possible_bgms = [j.replacement for j in bgms]
    possible_sfxs = [j.replacement for j in sfxs]

    print("Scrambling BGs...")
    for i in bg_images:
        random_value = random.choice(possible_bgs)
        new_line = f"image {i.var_name} = \"{random_value}\""
        new_lines[i.line_num] = new_line
        possible_bgs.remove(random_value)

    print("Scrambling character sprites...")
    for i in char_images:
        random_value = random.choice(possible_char_images)
        new_line = f"image {i.var_name} = \"{random_value}\""
        new_lines[i.line_num] = new_line
        possible_char_images.remove(random_value)

    print("Scrambling character names...")
    for i in char_names:
        random_value = random.choice(possible_char_names)
        new_line = f"define {i.var_name} = Character(\"{random_value}\", callback = {i.callback})"
        new_lines[i.line_num] = new_line
        possible_char_names.remove(random_value)

    print("Scrambling BGMs...")
    for i in bgms:
        random_value = random.choice(possible_bgms)
        new_line = f"define audio.{i.var_name} = \"{random_value}\""
        new_lines[i.line_num] = new_line
        possible_bgms.remove(random_value)

    print("Scrambling SFX...")
    for i in sfxs:
        random_value = random.choice(possible_sfxs)
        new_line = f"define audio.sfx{i.var_name} = \"{random_value}\""
        new_lines[i.line_num] = new_line
        possible_sfxs.remove(random_value)

    # Reappend new lines
    new_lines = [l + "\n" for l in new_lines]

    print("Writing new script...")
    # Replace script_start
    with open("./script_start.rpy", "w") as f:
        f.writelines(new_lines)

def main():
    scramble()

if __name__ == "__main__":
    main()
