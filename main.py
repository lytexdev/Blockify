import sys
import pygame as blockify
from termcolor import colored
from config import config
import themes.theme_manager as theme_manager
import gamestates.gamestate_manager as gamestate_manager
import gamestates.gamestate as gamestate
import utils.data.stats_api as stats_api
import themes.theme as theme
import objects.platform as platform
import objects.blocks as blocks
import objects.ball as ball
from events import button_clicked, game_over
from objects.blocks import Blocks


class Main:
    def __init__(self):
        blockify.init()

        self.set_states()

        self.screen = blockify.display.set_mode(config.get('display_size'))
        self.background = blockify.image.load(config.get('themes_images_path') + theme_manager.get_name(
            theme_manager.current_theme) + '/background.png').convert()
        self.platform = platform.Platform(self.screen.get_width(), self.screen.get_height(),
                                          config.get('themes_images_path') + theme_manager.get_name(
                                              theme_manager.current_theme) + '/platform.png')
        self.blocks = blocks.Blocks()
        self.ball = ball.Ball(self.platform)
        self.running = True
        self.game_over = False
        self.start()

    def start(self):
        self.console_output()

        while self.running:
            for event in blockify.event.get():
                if event.type == blockify.QUIT:
                    self.running = False
                    self.game_over = True
                if event.type == blockify.MOUSEBUTTONUP:
                    button_clicked.HandleButtonClick()

            self.set_display()
            self.fill_screen()
            self.check_game_status()

            blockify.display.update()
            blockify.time.Clock().tick(config.get('fps_limit'))

        blockify.quit()
        sys.exit()

    def set_states(self):
        try:
            # set current theme to theme from stats
            theme_manager.current_theme = theme.Theme(stats_api.get_level())
        except:
            print(colored('Error: Theme couldn\t set. Exists your provided theme?', 'red'))

        gamestate_manager.current_gamestate = gamestate.GameState.INGAME_STATE

    def fill_screen(self):
        """fill screen with background via gamestate"""
        if gamestate_manager.current_gamestate == gamestate.GameState.MENU_STATE:
            start_screen = blockify.image.load('resources/images/screens/start.png').convert()
            self.screen.blit(start_screen, (0, 0))

        elif gamestate_manager.current_gamestate == gamestate.GameState.INGAME_STATE:
            self.platform.update(self.screen.get_width())

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.platform.image, self.platform.rect)
            self.screen.blit(self.ball.image, self.ball.rect)
            Blocks().draw_blocks(self.screen)

        elif gamestate_manager.current_gamestate == gamestate.GameState.END_STATE:
            lose_screen = blockify.image.load('resources/images/screens/ending.png').convert()
            self.screen.blit(lose_screen, (0, 0))

        else:
            print(colored('Very weird Error haha\nGamestate not found', 'red'))

    def set_display(self):
        """set display name and icon"""
        try:
            blockify.display.set_caption(f"Blockify | {config.get('version')}")
            blockify.display.set_icon(blockify.image.load(config.get('logo_path')))
        except:
            print(colored('Error: Couldn\'t set display name or icon', 'red'))

    def check_game_status(self):
        """check if ball is out of screen and set game over"""
        if self.ball.update(self.screen.get_width(), self.screen.get_height(), self.platform):
            self.set_game_over()

    def set_game_over(self):
        """set game over and fill screen"""
        game_over.GameOver()
        self.fill_screen()

    def console_output(self):
        print(" ")
        print(" ")
        print(colored(f"Blockify | {config.get('version')}", "magenta"))
        print(colored(f"{config.get('description')}", "magenta"))
        print(colored("» Made by: " + ", ".join(str(author) for author in config.get('authors')), "white"))
        print(colored(f"{config.get('github')}", "white"))
        print(" ")
        print(" ")


if __name__ == '__main__':
    Main()
