import renpy.exports as renpy
import renpy.config as config
import renpy.defaultstore as store

import logging
logger = logging.getLogger("csb")
"""renpy
init python:
"""
from pathlib import Path
import pprint
import types
import re
import datetime

import renpy.revertable as revertable
import renpy.display.im as im
import renpy.display.transform as transform
import renpy.text as text
import renpy.display.video as video
from renpy.display.layout import DynamicDisplayable


def dump_stores():
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

        if re.match(r"^[A-Z_][A-Z0-9_]+$", k):
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
            elif "Character" in str(type(v)):
                write_v = f"<Character {v}>"
            elif isinstance(v, im.Image):
                write_v = f"<Image {v.filename}>"
            elif isinstance(v, video.Movie):
                write_v = f"<Movie {v._original_play}>"
            elif isinstance(v, (transform.Transform, transform.ATLTransform)):
                return
            elif isinstance(v, (renpy.store.LayeredImage, renpy.store.LayeredImageProxy)):
                write_v = f"<LayeredImage {v.name}>"
            elif isinstance(v, text.text.Text):
                write_v = f"<Text {v.text}>"
            elif isinstance(v, text.extras.ParameterizedText):
                return
            elif isinstance(v, DynamicDisplayable):
                write_v = f"<DynamicDisplayable>"
            else:
                write_v = str(v)

            if write_v.startswith("<class") or write_v.startswith("<renpy") or write_v.startswith("<store") or \
                write_v.startswith("typing.") or write_v.startswith("<partial") or write_v.startswith("<module") \
                    or write_v.startswith("<enum") or write_v.startswith("<bound") or write_v.startswith("<built-in") \
                        or write_v.startswith("_Feature"):
                # If we don't have a good representation for it, it's probably garbage.
                return

            output_string += f"{' ' * indent}{k}: {write_v}{newline}"

    def _write(s: str, indent = 0, newline = "\n"):
        nonlocal output_string
        output_string += f"{' ' * indent}{s}{newline}"

    _write(f"{config.name} {config.version}")
    _write(f"{datetime.datetime.now()}")

    _write("=== STORE ===")
    logger.debug("Dumping store...")
    _store_c = 0
    for k in dir(store):
        v = getattr(store, k)
        if "Character" not in str(type(v)):
            _store_c += 1
            _write_kv(k, store = store)
    logger.debug(f"Dumped store ({_store_c})")

    _write("\n=== CHARACTERS ===")
    logger.debug("Dumping characters...")
    _char_c = 0
    for k in dir(store):
        v = getattr(store, k)
        if "Character" in str(type(v)):
            _char_c += 1
            _write_kv(k, store = store)
    logger.debug(f"Dumped characters ({_char_c})")

    _write("\n=== AUDIO ===")
    logger.debug("Dumping audio...")
    _write("== MUSIC ==")
    logger.debug("Dumping music...")
    _music_c = 0
    for k in dir(audio):
        v = str(getattr(audio, k))
        if "sfx_" not in k and "snd_" not in k and "dxcom" not in v and "text/" not in v:
            _music_c += 1
            _write_kv(k, store = audio)
    logger.debug(f"Dumped music ({_music_c})")

    _write("\n== DXCOM ==")
    logger.debug("Dumping DXCOM...")
    _dxcom_c = 0
    for k in dir(audio):
        v = str(getattr(audio, k))
        if "dxcom" in v:
            _dxcom_c += 1
            _write_kv(k, store = audio)
    logger.debug(f"Dumped DXCOM ({_dxcom_c})")

    _write("\n== SFX ==")
    logger.debug("Dumping SFX...")
    _sfx_c = 0
    for k in dir(audio):
        if "sfx_" in k or "snd_" in k:
            _sfx_c += 1
            _write_kv(k, store = audio)
    logger.debug(f"Dumped SFX ({_sfx_c})")

    _write("\n== TEXT BEEPS ==")
    logger.debug("Dumping text beeps...")
    _beep_c = 0
    for k in dir(audio):
        v = str(getattr(audio, k))
        if "text/" in v:
            _beep_c += 1
            _write_kv(k, store = audio)
    logger.debug(f"Dumped text beeps ({_beep_c})")

    _write("\n=== IMAGES ===")
    logger.debug("Dumping images...")
    _image_c = 0
    _video_c = 0

    image_dict = {}
    video_dict = {}
    for k in renpy.list_images():
        v = renpy.get_registered_image(k)
        if isinstance(v, video.Movie):
            video_dict[k] = v
            _video_c += 1
        else:
            image_dict[k] = v
            _image_c += 1

    for k, v in dict(sorted(image_dict.items(), key = lambda item: str(type(item[1])))).items():
        _write_kv(k, v = v)
    logger.debug(f"Dumped images ({_image_c})")

    _write("\n=== VIDEOS ===")
    for k, v in video_dict.items():
        _write_kv(k, v = v)
    logger.debug(f"Dumped videos ({_video_c})")

    _write("\n=== PERSISTENT ===")
    logger.debug("Dumping persistent...")
    _per_c = 0
    for k, v in persistent.__dict__.items():
        _per_c += 1
        _write_kv(k, v = v)
    logger.debug(f"Dumped persistent ({_per_c})")

    _write("\n=== SEEN LABELS ===")
    _label_c = 0
    _seen_c = 0
    for l in renpy.get_all_labels():
        _label_c += 1
        if renpy.seen_label(l):
            _seen_c += 1
            _write(l)
    logger.debug(f"Dumped seen labels ({_seen_c}/{_label_c})")

    with path.open(mode = "w") as f:
        f.write(output_string)

    logger.info(f"Dump written!")