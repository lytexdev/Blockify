import main
from main import blockify


class Platform:
    def __init__(self, screen_width, screen_height, image_file):
        self.image = blockify.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2 - self.image.get_width() // 2
        self.rect.y = screen_height - 100
        self.speed = int(main.config.get('platform_speed'))

    def update(self, screen_width):
        keys = blockify.key.get_pressed()
        if keys[blockify.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[blockify.K_RIGHT] and self.rect.x < screen_width - self.image.get_width():
            self.rect.x += self.speed
