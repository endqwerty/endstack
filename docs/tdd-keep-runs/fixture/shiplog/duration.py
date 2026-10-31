import re

_UNITS = {"h": 3600, "m": 60, "s": 1}
_PART = re.compile(r"(\d+)([hms])")


def parse_duration(text):
    """Parse '1h30m', '45s', '2h' into seconds. Used by `shiplog freeze --for`."""
    text = text.strip()
    if not text or _PART.sub("", text):
        raise ValueError(f"bad duration: {text!r}")
    total = 0
    for number, unit in _PART.findall(text):
        total = int(number) * _UNITS[unit]
    return total
