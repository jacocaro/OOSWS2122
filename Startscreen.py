import pygame
from pygame.locals import *
import os

class Startscreen():
    
    def __init__(self, screen):
        self.screen = screen
        self.bgimage = pygame.image.load(os.path.join('Images', 'startscreen.png')).convert()
        self.fontNewGame = pygame.font.Font(None,25)
        self.screen.blit(self.bgimage, (0,0))

    def update(self, screen, buttonList):
        for button in buttonList:
            screen.blit(button.image, (button.x, button.y))
    
    def collsionDetection(self, buttonList, mousepos):
        for button in buttonList:
            if button.collide(mousepos):
                return True, button.type
        return False
