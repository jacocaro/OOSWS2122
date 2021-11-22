import pygame
from pygame.locals import *
import os

class Wall(object):
    light_img = pygame.image.load(os.path.join('images', 'wall.png'))

    def __init__(self, x, y, width, height, moving_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False
        self.moving_speed = moving_speed

    def update(self, screen):

        # verschiebe sprite auf x-Achse nach links entsprechend moving_speed
        self.x -= self.moving_speed
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        screen.blit(self.light_img, (self.x, self.y))