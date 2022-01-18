import pygame
from pygame.locals import *
import os
from Wall import Wall

class Player(object):
    """
    setup Player - defines move set and collision detection

    Attributes
    ----------
    run, jump, fade, ghostHit : image - player images for different move set types 
    x, y : int - x and y position of player
    width, height : int - width and heigth of player
    y_base : int - initial y position
    jumping : Boolean - check for jump
    fading : Boolean - check for fade
    fadeCount : int - number to count fade frames
    gotHit : Boolean - check for hit
    gothitcount : int - number to count hit frames
    colliding : Boolean - check for collision
    hitbox : Rect - rectangle to check collision
    jump_multiplier : Decimal - height adjustment muliplier for jumping
    
    Methods
    -------
    update(screen) : defines move set for jump, fade and hit
    collide(obstacle) : checks for collision detection player - obstacle
    """
    run = pygame.image.load(os.path.join('Images', 'ghost.png'))
    jump = pygame.image.load(os.path.join('Images', 'ghost.png'))
    fade = pygame.image.load(os.path.join('Images', 'ghost_trans.png'))
    ghostHit = pygame.image.load(os.path.join('Images', 'ghost_red.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.y_base = y
        self.jumping = False
        self.fading = False
        self.fadeCount = 0
        self.gotHit = False
        self.gothitcount = 0
        self.colliding = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.jump_multiplier = 0.92

    def update(self, screen):
        """
        defines move set for jump, fade and hit
        @param screen: Display
        """
        if self.jumping:
            self.jump_multiplier += 0.005

            self.y *= self.jump_multiplier

            if self.y >= self.y_base:
                self.y = self.y_base
                self.jump_multiplier = 0.92
                self.jumping = False
        
        if self.fading:
            screen.blit(self.fade, (self.x, self.y))
            self.fadeCount += 1
            if self.fadeCount > 20:
                self.fadeCount = 0
                self.fading = False

        if self.gotHit:
            screen.blit(self.ghostHit, (self.x, self.y))
            self.gothitcount += 1
            if self.gothitcount > 10:
                self.gothitcount = 0
                self.gotHit = False
                      
        if not self.gotHit and not self.fading:
            screen.blit(self.run, (self.x, self.y))

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def collide(self, obstacle):
        """
        checks for collision detection player - obstacle
        @param obstacle : Object
        @returns : Boolean 
        """
        if self.hitbox.colliderect(obstacle.hitbox):
            if self.fading and type(obstacle) == Wall:
                return False
            else:
                return True
        return False