init python:
    import json
    from pathlib import Path

    def dump_persistent():
        try:
            p = Path("./persistent.json")
            pe = {}
            print(persistent.__dict__)
            for k, v in persistent.__dict__.items():
                if type(v) in [int, str, float, bool, list, dict]:
                    pe[k] = v
            with open(p, "w") as f:
                json.dump(pe, f)
            return p.absolute(), True
        except Exception as e:
            return e, False


label dump:
    centered "Dumping persistent data...{nw=1}"
    $ dump_path, dump_success = dump_persistent()
    if dump_success:
        centered "Dumped persistent data!\n[dump_path]"
    else:
        centered "⚠️ Dump failed!\n[dump_path]"
    $ renpy.quit()