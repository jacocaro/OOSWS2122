import pygame
from pygame.locals import *
import os

class Background():
    """
    setup Background and scroll function 

    Attributes
    ----------
    moving_speed : int - background scrolling speed
    game : Game - set game 
    bgimage, rectBGimg : image - first and second background image
    bgY1, bgX1, bgY2, bgX2 : int - x and y position of both background images
    
    Methods
    -------
    update(screen, showCastle) : moving background on screen
    """
    def __init__(self, moving_speed, game):
        self.moving_speed = moving_speed
        self.game = game
        self.bgimage = pygame.image.load(os.path.join(
            'Images', 'background.png')).convert()  # first bg-image
        self.rectBGimg = self.bgimage.get_rect()  # second bg-image

        # first point top left
        self.bgY1 = 0
        self.bgX1 = 0

        # second point one bgimage.with next to it
        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

    def update(self, screen, showCastle):
        """
        moving background on screen
        @param screen : Display
        @param showCastle : Boolean
        """
        # decrementing both x-values by speed-value
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.moving_speed > 0 and showCastle:
            self.moving_speed -= 0.01

        # If variables exceed the width of the screen --> reset original position at the left
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

        screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        screen.blit(self.bgimage, (self.bgX2, self.bgY2))
        # Anzeige Hit-User-Interface
        screen.blit(self.game.hitUi, (10,10))
