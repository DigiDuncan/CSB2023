from time import strftime, localtime

import colored

__all__ = ["styles"]


class Style:
    __slots__ = ["name", "codes", "prefix", "showtime", "showprefix"]

    def __init__(self, name, codes, prefix = None, showtime = None, showprefix = None):
        self.name = name
        self.codes = codes
        self.prefix = prefix
        self.showtime = showtime
        self.showprefix = showprefix


class Styles:
    __slots__ = ["_styles", "default", "timestring", "timestampCodes"]

    def __init__(self):
        self._styles = {}
        self.timestring = "%d %b %H:%M:%S"
        self.timestampCodes = colored.fg("magenta")

    def create(self, name, *, fg = None, bg = None, attr = None, prefix = None, showtime = None, showprefix = None):
        """Create a custom style"""
        name = name.lower()
        codes = ""
        if fg is not None:
            codes += colored.fg(fg)
        if bg is not None:
            codes += colored.bg(bg)
        if attr is not None:
            codes += colored.attr(attr)
        self._styles[name] = Style(name, codes, prefix, showtime, showprefix)

    def format(self, message, *, style="default", showtime=None, showprefix=None):
        """Format a message in the requested style"""
        style = style.lower()
        if style not in self._styles:
            raise ValueError(f"Unknown style: {style}")
        styledata = self._styles[style]
        showtime = getFirstNotNone([showtime, styledata.showtime, True])
        showprefix = getFirstNotNone([showprefix, styledata.showprefix, True])
        formatted = ""
        if showtime:
            formatted += self._timestamp()
        if showprefix and styledata.prefix:
            formatted += styledata.codes + colored.attr("reverse") + styledata.prefix + colored.attr("reset") + " "
        formatted += "\n".join(styledata.codes + line + colored.attr("reset") for line in message.splitlines())
        return formatted

    def print(self, *args, **kwargs):
        """Print a message in the requested style"""
        print(self.format(*args, **kwargs))

    def _timestamp(self):
        """Color styling for terminal messages"""
        t = localtime()
        return self.timestampCodes + strftime(f"{self.timestring} | ", t) + colored.attr("reset")

    def __getattr__(self, name):
        name = name.lower()
        if name not in self._styles:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")
        return lambda message: self.print(message, style=name)

    def __str__(self):
        return "styles: " + (" ".join(self.format(level, style=level, showtime = False, showprefix = False) for level in self._styles.keys()))


# Returns the first not None value in a list
def getFirstNotNone(items):
    for i in items:
        if i is not None:
            return i
    return None


styles = Styles()
