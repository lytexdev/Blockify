current_theme = None


def get_current():
    """Return the current theme"""
    return current_theme


def get_name(theme):
    """Return the name of the given theme in lowercase"""
    return str(theme.name.lower())


def get_value(theme):
    """Return the value of the given theme"""
    return theme.value
