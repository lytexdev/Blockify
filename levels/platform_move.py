import sys
import main
from main import blockify
import themes.theme_manager as theme_manager


def move(screen, image, x, y, speed):
    """Moves the platform"""
    move_right = False
    move_left = False
    prev_rect = image.get_rect().move(x, y)

    try:
        background_image = blockify.image.load(
            f"{main.config.get('backgroundPath')}{theme_manager.get_name(theme_manager.current_theme)}.png").convert_alpha()
        screen.blit(background_image, (0, 0))
    except:
        print(f"Couldn't load background image. Does the path "
              f"'{main.config.get('backgroundPath')}{theme_manager.get_name(theme_manager.current_theme)}.png' "
              f"exists?")
        main.blockify.quit()
        sys.exit()

    while main.Main.running:
        for event in blockify.event.get():
            if event.type == blockify.QUIT:
                blockify.quit()
                sys.exit()
            if event.type == blockify.KEYDOWN:
                if event.key == blockify.K_RIGHT:
                    move_right = True
                if event.key == blockify.K_LEFT:
                    move_left = True
            if event.type == blockify.KEYUP:
                if event.key == blockify.K_RIGHT:
                    move_right = False
                    prev_rect = image.get_rect().move(x, y)
                if event.key == blockify.K_LEFT:
                    move_left = False
                    prev_rect = image.get_rect().move(x, y)

        if move_right and x + image.get_width() + 17 < screen.get_width():
            x += speed
            prev_rect = image.get_rect().move(x - 1, y)
        if move_left and x - 17 > 0:
            x -= speed
            prev_rect = image.get_rect().move(x + 1, y)

        screen.blit(background_image, prev_rect, prev_rect)
        screen.blit(image, (x, y))

        blockify.display.update()
