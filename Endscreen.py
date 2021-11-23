import pygame
from pygame.locals import *
import os

class Endscreen():
    def __init__(self, game):
        self.game = game
        self.bgimage = pygame.image.load(os.path.join(
            'Images', 'background.png')).convert()  # first bg-image
        self.fontend = pygame.font.Font(None,45)
        self.endScreenUiEndText = self.fontend.render('Hulahu hat das Schloss erreicht.', True, Color('white'))
        self.endScreenUiScoreText = self.fontend.render('Dein Score: ' + str(game.hit_count), True, Color('white'))

    def update(self, screen):
        screen.blit(self.bgimage, (0,0))
        # Anzeige Hit-User-Interface
        screen.blit(self.endScreenUiEndText, (230,230))
        screen.blit(self.endScreenUiScoreText, (230,280))
