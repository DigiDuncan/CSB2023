screen fake_error(file_name, line_num, small_error, exception_text):
    add "#dadada"
    add Text("An exception has occurred.", size=40, style="_default"):
        xpos 0.1 ypos 0.05
    add Text(f"File \"{file_name}\", line {line_num}:\nSee traceback.txt for details.", size=20, style="_default"):
        xpos 0.1 ypos 0.15
    add Text(small_error, size=20, style="_default"):
        xpos 0.1 ypos 0.25
    python:
        try: sys.modules['renpy.error'].report_exception(exception_text, False)
        except: pass

    key "mouseup_1" action Hide("fake_error")
