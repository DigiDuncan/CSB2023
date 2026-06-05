# Main fonts
translate tok_sitelen_pona style default:
    font gui_theme_map["tp_font"]

translate tok_sitelen_pona python:
    gui.text_font = gui_theme_map["tp_font"]
    gui.name_text_font = gui_theme_map["tp_font"]
    gui.header_text_font = gui_theme_map["tp_font"]
    gui.system_font = gui_theme_map["tp_font"]
    gui.interface_text_font = gui_theme_map["tp_font"]
    gui.button_text_font = gui_theme_map["tp_font"]
    gui.choice_button_text_font = gui_theme_map["tp_font"]

    gui_theme_map["main_font"] = gui_theme_map["tp_font"]
    gui_theme_map["name_font"] = gui_theme_map["tp_font"]
    gui_theme_map["header_font"] = gui_theme_map["tp_font"]
