import pygame
from pygame.locals import *
import os

class Endscreen():
    def __init__(self, game):
        self.game = game
        
        self.fontend = pygame.font.Font(None,40)
        self.fontNewGame = pygame.font.Font(None,25)
        self.endScreenUiEndText = self.fontend.render('Hulahu hat das Schloss erreicht.', True, Color('white'))
        self.endScreenUiNewGame = self.fontNewGame.render('Drücke <- für leichtes Spiel und -> für schweres Spiel', True, Color('white'))
        

    def update(self, screen, game):
        # Anzeige Hit-User-Interface
        self.endScreenUiScoreText = self.fontend.render('Dein Score: ' + str(game.hit_count), True, Color('white'))
        
        screen.blit(self.endScreenUiEndText, (160,110))
        screen.blit(self.endScreenUiScoreText, (160,140))
        screen.blit(self.endScreenUiNewGame, (50,350))
