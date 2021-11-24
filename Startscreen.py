import pygame
from pygame.locals import *
import os

from Button import Button

class Startscreen():
    
    def __init__(self, screen):
        self.screen = screen
        self.bgimage = pygame.image.load(os.path.join('Images', 'startscreen.png')).convert()
        self.fontNewGame = pygame.font.Font(None,25)
        self.screen.blit(self.bgimage, (0,0))

    def showButtons(screen, buttonList):
        screen.blit(buttonList[0].image, buttonList[0].width, buttonList[0].height)