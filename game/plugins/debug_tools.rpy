init python:
    def label_callback(name, abnormal):
        if not name.startswith("_"):
            store.last_label = name

    config.label_callback = label_callback
