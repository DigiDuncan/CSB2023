import random
import re
from dataclasses import dataclass

SCRAMBLE_IMAGES = True
SCRAMBLE_CHARACTERS = True

RE_BG_IMAGE = r'image (.+)\s?=\s?"(bg.+)"'
RE_CHAR_IMAGE = r'image (.+)\s?=\s?"(characters.+)"'
RE_CHARACTER = r'define (.+)\s?=\s?Character\("([^"]+)".+\)'

@dataclass
class Image:
    line_num: int
    var_name: str
    path: str
    original_line: str

@dataclass
class Character:
    line_num: int
    var_name: str
    char_name: str
    original_line: str


def main():
    lines = []
    new_lines = []

    bg_images = []
    char_images = []

    # Load the script_start
    with open("./script_start.rpy") as f:
        lines = f.readlines()
        new_lines = [None] * len(lines)

    # Read lines
    for n, line in enumerate(lines):
        if (m := re.match(RE_BG_IMAGE, line)) and "Movie" not in line and "Window" not in line:
            bg_images.append(Image(n, m.group(1), m.group(2), line.rstrip()))
        elif (m := re.match(RE_CHAR_IMAGE, line)) and "Movie" not in line and "Window" not in line:
            char_images.append(Image(n, m.group(1), m.group(2), line.rstrip()))
        else:
            new_lines[n] = line.rstrip()
    
    # Randomize values
    possible_bgs = [j.path for j in bg_images]
    possible_chars = [j.path for j in char_images]
    
    for i in bg_images:
        random_value = random.choice(possible_bgs)
        new_line = f"image {i.var_name} = \"{random_value}\""
        new_lines[i.line_num] = new_line
        possible_bgs.remove(random_value)

    for i in char_images:
        random_value = random.choice(possible_chars)
        new_line = f"image {i.var_name} = \"{random_value}\""
        new_lines[i.line_num] = new_line
        possible_chars.remove(random_value)

    # Reappend new lines
    new_lines = [l + "\n" for l in new_lines]

    # Replace script_start
    with open("./random_script_start.rpy", "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    main()
