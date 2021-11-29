import pygame
from pygame.locals import *
import os

class Wall(object):
    """
    setup Wall and scroll function 

    Attributes
    ----------
    x, y : int - x and y position of wall
    width, height : int - width and heigth of wall
    moving_speed : int - background scrolling speed
    hitbox : Rect - rectangle to check collision
    is_collided : Boolean - true on collision
    wall_img : image - wall image
    
    Methods
    -------
    update(screen) : moving wall on screen
    """

    def __init__(self, x, y, width, height, moving_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moving_speed = moving_speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False
        self.wall_img = pygame.image.load(os.path.join('images', 'wall.png'))

    def update(self, screen):
        """
        moving wall on screen
        @param screen : Display
        """
        # moving sprite on x axis to left according moving_speed 
        self.x -= self.moving_speed
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        screen.blit(self.wall_img, (self.x, self.y))