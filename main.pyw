import pygame

from settings import Settings
import game_functions as gf
from penguin import Penguin

settings = Settings()

clock = pygame.time.Clock()

Running = True

def main():
    pygame.init()
    pygame.display.set_caption('INF.ANIMATION')
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_heigh))
    penguin = Penguin(screen, settings)

    while Running:
      	penguin.update()
      	gf.check_events(penguin)
      	gf.update_screen(screen, settings, penguin)
      	clock.tick(30)

if __name__ == '__main__':
    main()