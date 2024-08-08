init python:
    from pathlib import Path

    def dump_persistent():
        try:
            p = Path("./persistent.txt")
            pe = {}
            print(persistent.__dict__)
            for k, v in persistent.__dict__.items():
                if k != "_preferences":
                    pe[k] = v
            with open(p, "w") as f:
                for k, v in pe.items():
                    f.write(f"{k}: {v}\n")
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