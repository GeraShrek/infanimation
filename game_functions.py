import sys

import pygame

def check_events(penguin):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                penguin.moving_right = True
                penguin.moving_left = False

            elif event.key == pygame.K_LEFT:
                penguin.moving_left = True
                penguin.moving_right = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                penguin.moving_right = False
            elif event.key == pygame.K_LEFT:
                penguin.moving_left = False


def update_screen(screen, settings, penguin):
    pygame.display.flip()
    screen.fill(settings.bg_color)
    screen.blit(settings.bg, (0,0))
    penguin.blitme()