import pygame
from pygame.locals import *
import os

class Button(object):
    """
    setup Button and collision detection

    Attributes
    ----------
    x, y : int - x and y position of Button
    width, height : int - width and heigth of Button
    hitbox : Rect - rectangle to check collision
    is_collided : Boolean - true on collision
    type : String - defines Button type / image type
    image : image - button image
    
    Methods
    -------
    collide(mousepos) : checks for collision
    """

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False
        if image == 'leicht':
            self.type = 'leicht'
            self.image = pygame.image.load(os.path.join('Images', 'Button_leicht.png')).convert()
        if image == 'schwer':
            self.type = 'schwer'
            self.image = pygame.image.load(os.path.join('Images', 'Button_schwer.png')).convert()
        if image == 'ende':
            self.type = 'ende'
            self.image = pygame.image.load(os.path.join('Images', 'Button_ende.png')).convert()
    
    def collide(self, mousepos):
        """
        checks for collision
        @param mousepos : list - x and y position 
        """
        mousepos_rect = pygame.Rect(mousepos[0], mousepos[1], 1, 1)
        if self.hitbox.colliderect(mousepos_rect):
            return True
        return False