import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_heigh = 600
        self.bg_color = (230, 230, 230)
        self.bg = pygame.image.load('images/background.png')