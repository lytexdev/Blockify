import main
from main import blockify
import gamestates.gamestate_manager as gamestate_manager
import gamestates.gamestate as gamestate


class GameOver:
    """Game Over Class"""
    def __init__(self):
        self.game_over = True
        self.lose_screen = None

        gamestate_manager.current_gamestate = gamestate.GameState.END_STATE

        # TODO: add Buttons to restart or quit the game

