import pygame
from pygame.locals import *
import os

class Startscreen():
    def __init__(self):
        self.bgimage = pygame.image.load(os.path.join('Images', 'startscreen.png')).convert()
        self.fontend = pygame.font.Font(None,45)
        self.fontNewGame = pygame.font.Font(None,25)
        self.endScreenUiEndText = self.fontend.render('Willkommen!', True, Color('white'))
        self.endScreenUiNewGame = self.fontNewGame.render('Drücke <- für leichtes Spiel und -> für schweres Spiel', True, Color('white'))
        

    def update(self, screen):
        screen.blit(self.bgimage, (0,0))
        # Anzeige Hit-User-Interface
        # self.endScreenUiScoreText = self.fontend.render('Dein Score: ' + str(game.hit_count), True, Color('white'))
        
        screen.blit(self.endScreenUiEndText, (230,230))
        # screen.blit(self.endScreenUiScoreText, (230,280))
        screen.blit(self.endScreenUiNewGame, (50,350))
