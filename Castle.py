import pygame
from pygame.locals import *
import os

class Castle(object):
    """
    setup Castle and scroll function 

    Attributes
    ----------
    x, y : int - x and y position of Castle
    width, height : int - width and heigth of Castle
    moving_speed : int - background scrolling speed
    hitbox : Rect - rectangle to check collision
    is_collided : Boolean - true on collision
    castle_img : image - castle image
    
    Methods
    -------
    update(screen) : moving castle on screen
    """
    

    def __init__(self, x, y, width, height, moving_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moving_speed = moving_speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False
        self.castle_img = pygame.image.load(os.path.join('images', 'castle.png'))
        
    def update(self, screen):
        """
        moving castle on screen
        @param screen : Display
        """
        # moving sprite on x axis to left according moving_speed 
        self.x -= self.moving_speed
        if self.moving_speed > 0:
            self.moving_speed -= 0.01
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        screen.blit(self.castle_img, (self.x, self.y))