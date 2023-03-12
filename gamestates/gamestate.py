from enum import Enum


class GameState(Enum):
    """Enum for the Gamestate of the game"""
    MENU_STATE = 1
    INGAME_STATE = 2
    END_STATE = 3,
