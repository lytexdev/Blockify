current_gamestate = None


def get_current():
    """Return the current theme"""
    return current_gamestate


def get_name(gamestate):
    """Return the name of the given theme in lowercase"""
    return str(gamestate.name.lower())


def get_value(gamestate):
    """Return the value of the given theme"""
    return gamestate.value
