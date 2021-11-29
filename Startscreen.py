import pygame
from pygame.locals import *
import os

class Startscreen():
    """
    set up startscreen

    Attributes
    ----------
    screen : Display - set display
    bgimage : image - startscreen image 
    fontNewGame : Font - set font 

    Methods
    -------
    update(screen, buttonList) : shows buttons
    collisionDetection(buttonList, mousepos) : checks mouse click on button

    """
    def __init__(self, screen):
        self.screen = screen
        self.bgimage = pygame.image.load(os.path.join('Images', 'startscreen.png')).convert()
        self.fontNewGame = pygame.font.Font(None,25)
        self.screen.blit(self.bgimage, (0,0))

    def update(self, screen, buttonList):
        """
        shows buttons
        @param screen :  Display
        @param buttonList : list
        """
        for button in buttonList:
            screen.blit(button.image, (button.x, button.y))
    
    def collsionDetection(self, buttonList, mousepos):
        """
        checks mouse click on button
        @param buttonList : list
        @param mousepos : list
        @returns : Boolean or String
        """
        for button in buttonList:
            if button.collide(mousepos):
                return button.type
        return False
            
