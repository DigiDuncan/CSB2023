import renpy.exports as renpy
import renpy.config as config

import renpy.defaultstore as store

"""renpy
init python:
"""
from pathlib import Path
import renpy.revertable as revertable
import pprint
import types
import re
import datetime

def dump_stores():
    images = renpy.display.image.images.keys()
    path = Path(config.basedir) / "dump.txt"

    BLACKLIST = ["chart_enemy", "chart_player", "line_list", "enemy_json_data", "player_json_data",
                 "enemy_chart_data", "player_chart_data", "bgm_list", "bg_list", "gui_theme_map", "j",
                 "ucn_bg_list", "ucn_remove"]
    STARTSWITH_BLACKLIST = ["_", "brunoais"]
    ENDSWITH_BLACKLIST = ["_af"]

    output_string = ""

    def _write_kv(k: str, *, store = None, v = None, indent = 0, newline = "\n"):
        nonlocal output_string

        k = str(k)

        if re.match(r"^[A-Z_]+$", k):
            return
        
        if k in BLACKLIST:
            return
        
        for s in STARTSWITH_BLACKLIST:
            if k.startswith(s):
                return
            
        for e in ENDSWITH_BLACKLIST:
            if k.endswith(e):
                return
        
        if v is None:
            if isinstance(k, dict):
                v = store[k]
            else:
                v = getattr(store, k)

        type_check = str(type(v))

        if isinstance(v, revertable.RevertableSet) or "set" in type_check:
            if v:
                output_string += f"{' ' * indent}{k}: {{\n"
                for i in v:
                    _write(i, indent = indent + 2)
                output_string += f"{' ' * indent}}}{newline}"
            else:
                output_string += f"{' ' * indent}{k}: {{}}{newline}"
        elif isinstance(v, revertable.RevertableDict) or "dict" in type_check:
            if v:
                output_string += f"{' ' * indent}{k}: {{\n"
                for i, ii in v.items():
                    _write_kv(k = i, v = ii, indent = indent + 2)
                output_string += f"{' ' * indent}}}{newline}"
            else:
                output_string += f"{' ' * indent}{k}: {{}}{newline}"
        elif isinstance(v, revertable.RevertableList) or "list" in type_check:
            if v:
                output_string += f"{' ' * indent}{k}: [\n"
                for i in v:
                    _write(i, indent = indent + 2)
                output_string += f"{' ' * indent}]{newline}"
            else:
                output_string += f"{' ' * indent}{k}: []{newline}"
        elif isinstance(v, types.FunctionType):
            return
        else:
            if isinstance(v, str):
                write_v = f"\"{v}\""
            if "Character" in str(type(v)):
                write_v = f"<Character {v}>"
            else:
                write_v = str(v)

            if write_v.startswith("<class") or write_v.startswith("<renpy") or write_v.startswith("<store") or \
                write_v.startswith("typing.") or write_v.startswith("<partial") or write_v.startswith("<module") \
                    or write_v.startswith("<enum") or write_v.startswith("<bound") or write_v.startswith("<built-in"):
                # If we don't have a good representation for it, it's probably garbage.
                return

            output_string += f"{' ' * indent}{k}: {write_v}{newline}"

    def _write(s: str, indent = 0, newline = "\n"):
        nonlocal output_string
        output_string += f"{' ' * indent}{s}{newline}"

    _write(f"{config.name} {config.version}")
    _write(f"{datetime.datetime.now()}")

    _write("=== STORE ===")
    for k in dir(store):
        v = getattr(store, k)
        if "Character" not in str(type(v)):
            _write_kv(k, store = store)
    _write("\n=== CHARACTERS ===")
    for k in dir(store):
        v = getattr(store, k)
        if "Character" in str(type(v)):
            _write_kv(k, store = store)
    _write("\n=== AUDIO ===")
    _write("== MUSIC ==")
    for k in dir(audio):
        if "sfx_" not in k:
            _write_kv(k, store = audio)
    _write("\n== SFX ==")
    for k in dir(audio):
        if "sfx_" in k:
            _write_kv(k, store = audio)
    _write("\n=== IMAGES ===")
    for k in images:
        img = renpy.get_registered_image(k)
        _write_kv(k, v = img)
    _write("\n=== PERSISTENT ===")
    for k, v in persistent.__dict__.items():
        _write_kv(k, v = v)

    with path.open(mode = "w") as f:
        f.write(output_string)
