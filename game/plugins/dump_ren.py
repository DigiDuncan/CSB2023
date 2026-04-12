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

def dump_stores():
    images = renpy.list_images()
    path = Path(config.basedir) / "dump.txt"

    output_string = ""

    def _write_kv(k: str, *, store = None, v = None, indent = 0, newline = "\n"):
        nonlocal output_string
        if k.startswith("_"):
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
            else:
                write_v = str(v)

            if write_v.startswith("<class") or write_v.startswith("<renpy") or write_v.startswith("<store") or \
                write_v.startswith("typing.") or write_v.startswith("<partial") or write_v.startswith("<module"):
                # If we don't have a good representation for it, it's probably garbage.
                return

            output_string += f"{' ' * indent}{k}: {write_v}{newline}"

    def _write(s: str, indent = 0, newline = "\n"):
        nonlocal output_string
        output_string += f"{' ' * indent}{s}{newline}"

    _write("=== STORE ===")
    for k in dir(store):
        _write_kv(k, store = store)
    _write("\n=== AUDIO ===")
    for k in dir(audio):
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
