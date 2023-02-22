import sys
import pygame as blockify
from termcolor import colored
from config import config
import themes.theme_manager as theme_manager
import data.stats_api as stats_api
import themes.theme as theme
import objects.platform as platform
import objects.ball as ball


class Main:
    def __init__(self):
        blockify.init()
        
        theme_manager.current_theme = theme.Theme(stats_api.get_level())
        
        self.screen = blockify.display.set_mode(config.get('displaySize'))
        
        self.background = blockify.image.load(config.get('themesImagesPath') + theme_manager.get_name(theme_manager.current_theme) + '/background.png').convert()
        self.platform = platform.Platform(self.screen.get_width(), self.screen.get_height(), config.get('themesImagesPath') + theme_manager.get_name(theme_manager.current_theme) + '/platform.png')
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

            self.set_display()
            self.fill_screen()
            self.check_game_status()

            blockify.display.update()
            blockify.time.Clock().tick(90)
            
        blockify.quit()
        sys.exit()


    def fill_screen(self):
        self.platform.update(self.screen.get_width())

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.platform.image, self.platform.rect)
        self.screen.blit(self.ball.image, self.ball.rect)
    
    
    def set_display(self):
        '''set display name and icon'''
        blockify.display.set_caption(config.get('name') + " " + config.get('version'))
        blockify.display.set_icon(blockify.image.load(config.get('logoPath')))
    
    
    def check_game_status(self):
        if self.ball.update(self.screen.get_width(), self.screen.get_height(), self.platform):
            # TODO: add game over screen/function
            self.game_over = True
            print("-> game over (ball fell off the screen))")
        

    def console_output(self):
        print(" ")
        print(" ")
        print(colored(f"{config.get('name')} | {config.get('version')}", "magenta"))
        print(colored(f"{config.get('description')}", "magenta"))
        print(colored("» made by: " + ", ".join(str(author) for author in config.get('authors')), "white"))
        print(colored(f"{config.get('github')}", "white"))
        print(" ")
        print(" ")


if __name__ == '__main__':
    Main()