import sys
from typing import Type
import pygame as blockify
from termcolor import colored

import themes.theme
from config import config
import themes.theme_manager as theme_manager
import data.stats_api as stats_api
from levels import level


class Main:
    blockify = blockify
    running = True
    screen = blockify.display.set_mode(config.get('displaySize'))

    def on_enable(self):
        try:
            self.console_output()
            self.start_game()
            self.quit_game()
        except Exception as exception:
            print(colored(f"Couldn't start the main-script\n\nError: {exception}", "red"))

    def start_game(self):
        blockify.init()

        blockify.display.set_caption(f" | {config.get('name')}")
        blockify.display.set_icon(blockify.image.load(config.get('logoPath')))
        blockify.mouse.set_cursor(*blockify.cursors.tri_left)

        theme_manager.current_theme = themes.theme.Theme(stats_api.get_level())
        level.generate(Main.screen, config.get('platformSpeed'))

    def quit_game(self):
        try:
            while self.running:
                for event in blockify.event.get():
                    if event.type == blockify.QUIT:
                        self.running = False
            blockify.quit()
            quit()
            sys.exit()

        except Exception as exception:
            print(colored(f"Couldn't quit the game\n\nError: {exception}", "red"))

    def console_output(self):
        print()
        print(" ")
        print(colored(f"{config.get('name')} | {config.get('version')}", "magenta"))
        print(colored(f"{config.get('description')}", "white"))
        print(colored("» made by: " + ", ".join(str(author) for author in config.get('authors')), "white"))
        print(colored(f"{config.get('github')}", "light_grey"))
        print(" ")

    def setRunning(self, running):
        """Set the game status"""
        self.running = running

    def isRunning(self):
        """Return the value of the status of the game"""
        return self.running


if __name__ == "__main__":
    Main().on_enable()
