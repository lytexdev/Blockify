import main
import themes.theme_manager as theme_manager


class Ball:
    def __init__(self, platform):
        self.image = main.blockify.image.load(main.config.get(f'themesImagesPath') +
                                              theme_manager.get_name(theme_manager.current_theme) + '/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = platform.rect.x + platform.rect.width // 2 - self.rect.width // 2
        self.rect.y = platform.rect.y - self.rect.height
        self.speed = [5, -5]


    def update(self, screen_width, screen_height, platform):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.x <= 0 or self.rect.x + self.rect.width >= screen_width:
            self.speed[0] = -self.speed[0]

        if self.rect.y <= 0:
            self.speed[1] = -self.speed[1]

        if self.rect.y + self.rect.height >= platform.rect.y and self.rect.x + self.rect.width >= platform.rect.x and self.rect.x <= platform.rect.x + platform.rect.width:
            self.speed[1] = -self.speed[1]

        if self.rect.y + self.rect.height >= screen_height - 40:
            return True
