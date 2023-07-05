init python:
    import platform
    import time

    def make_traceback(file_name, line_num, small_error, exception_text):

        traceback = f"""I'm sorry, but an uncaught exception occurred.

While running game code:
  File "game/{file_name}", line {line_num}, in <module>
    raise Exception(\"{small_error}\")
Exception: {exception_text}

{platform.platform()} {platform.machine()}
{renpy.version()}
{renpy.config.name} {renpy.config.version}
{time.ctime()}
"""

        loc = config.basedir.replace("\\", "/") + "/traceback_user.txt"
        with open(loc, "w+") as f:
            f.write(traceback)

screen fake_error(file_name, line_num, small_error, exception_text):
    add "#dadada"
    add Text("An exception has occurred.", size=40, style="_default"):
        xpos 0.1 ypos 0.05
    add Text(f"File \"{file_name}\", line {line_num}:\nSee traceback_user.txt for details.", size=20, style="_default"):
        xpos 0.1 ypos 0.15
    add Text(small_error, size=20, style="_default"):
        xpos 0.1 ypos 0.25
    python:
        make_traceback(file_name, line_num, small_error, exception_text)

    key "mouseup_1" action Hide("fake_error")
