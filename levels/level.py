import main
from main import blockify
import themes.theme_manager as theme_manager
import levels.platform_move as platform


def generate(screen, speed):
    """Spawns the platform"""
    image = blockify.image.load(
        f"{main.config.get('platformPath')}{theme_manager.get_name(theme_manager.current_theme)}.png")

    x_height = screen.get_rect().centerx - (image.get_width() / 2)
    y_height = ((screen.get_height() - image.get_height()) - 128)

    platform.move(screen, image, x_height, y_height, speed)