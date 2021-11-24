import pygame
from pygame.locals import *
import os

class Endscreen():
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.fontend = pygame.font.Font(None,30)
        self.fontNewGame = pygame.font.Font(None,25)
        self.endScreenUiEndText = self.fontend.render('Hulahu hat das Schloss erreicht.', True, Color('white'))
        # self.endScreenUiNewGame = self.fontNewGame.render('Drücke <- für leichtes Spiel und -> für schweres Spiel', True, Color('white'))
        
    def update(self, screen, game, buttonList):
        # Anzeige Hit-User-Interface
        self.endScreenUiScoreText = self.fontend.render('Dein Score: ' + str(game.endscore) + ' %', True, Color('white'))
        screen.blit(self.endScreenUiEndText, (180,100))
        screen.blit(self.endScreenUiScoreText, (180,130))
        #screen.blit(self.endScreenUiNewGame, (50,350))
        for button in buttonList:
            self.screen.blit(button.image, (button.x, button.y))
    
    def collsionDetection(self, buttonList, mousepos):
        for button in buttonList:
            if button.collide(mousepos):
                return button.type
        return False
