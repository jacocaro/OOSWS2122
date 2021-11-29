import pygame
from pygame.locals import *

class Endscreen():
    """
    set up endscreen

    Attributes
    ----------
    game : Game - set game
    screen : Display - set display
    fontend, fontNewGame : Font - set font 
    endscreenIsSet : Boolean - activates endscreen
    endScreenUiEndText : Font - set text of font

    Methods
    -------
    update(screen, game, buttonList, endscreen) : shows text, endscore and buttons
    collisionDetection(buttonList, mousepos) : checks mouse click on button

    """
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.fontend = pygame.font.Font(None,30)
        self.fontNewGame = pygame.font.Font(None,25)
        self.endscreenIsSet = False
        self.endScreenUiEndText = self.fontend.render('Hulahu hat das Schloss erreicht.', True, Color('white'))
        
    def update(self, screen, game, buttonList, endscreen):
        """
        shows text, endscore and buttons
        @param screen :  Display
        @param game : Game
        @param buttonList : list
        @param endscreen : Endscreen
        """
        # shows hit user interface
        if endscreen == False:
            self.endscreenIsSet = False
        if endscreen and self.endscreenIsSet == False:
            self.endScreenUiScoreText = self.fontend.render('Dein Score: ' + str(game.endscore) + ' %', True, Color('white'))
            screen.blit(self.endScreenUiEndText, (180,100))
            screen.blit(self.endScreenUiScoreText, (180,130))
            for button in buttonList:
                self.screen.blit(button.image, (button.x, button.y))
            self.endscreenIsSet = True
    
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
