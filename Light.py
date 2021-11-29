import pygame
from pygame.locals import *
import os

class Light(object):
    """
    setup Light and scroll function 

    Attributes
    ----------
    x, y : int - x and y position of light
    width, height : int - width and heigth of light
    moving_speed : int - background scrolling speed
    hitbox : Rect - rectangle to check collision
    is_collided : Boolean - true on collision
    light_img : image - light image
    
    Methods
    -------
    update(screen) : moving light on screen
    """
    def __init__(self, x, y, width, height, moving_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moving_speed = moving_speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False
        self.light_img = pygame.image.load(os.path.join('images', 'lantern.png'))

    def update(self, screen):
        """
        moving light on screen
        @param screen : Display
        """
        # moving sprite on x axis to left according moving_speed 
        self.x -= self.moving_speed
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        screen.blit(self.light_img, (self.x, self.y))