import pygame

class Penguin():

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/penguin.png')
        self.walkRight = [pygame.image.load('images/penguin1.png'), pygame.image.load('images/penguin2.png')]
        self.walkLeft = [pygame.image.load('images/penguinback1.png'), pygame.image.load('images/penguinback2.png')]

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.animCount = 0


    def update(self):

        if self.animCount + 1 >= 30:
            self.animCount = 0

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.right += 10
            self.image = self.walkRight[self.animCount // 15]
            self.animCount += 3

        elif self.moving_left and self.rect.left > 0:
            self.rect.left -= 10
            self.image = self.walkLeft[self.animCount // 15]
            self.animCount += 3

        elif self.moving_right & self.moving_left == False:
            self.image = pygame.image.load('images/penguin.png')

    def blitme(self):
        self.screen.blit(self.image, self.rect)