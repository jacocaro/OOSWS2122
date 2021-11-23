import pygame
from pygame.locals import *
import os
from Wall import Wall

class Player(object):
    # evtl später Array mit Bildern für Animation hinterlegen
    run = pygame.image.load(os.path.join('Images', 'ghost.png'))
    # evtl später Array mit Bildern für Animation hinterlegen
    jump = pygame.image.load(os.path.join('Images', 'ghost.png'))
    fade = pygame.image.load(os.path.join('Images', 'ghost_trans.png'))
    ghostHit = pygame.image.load(os.path.join('Images', 'ghost_red.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.y_base = 313
        self.width = width
        self.height = height
        self.jumping = False
        self.fading = False
        self.fadeCount = 0
        self.gotHit = False
        self.gothitcount = 0
        self.colliding = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        self.jump_multiplier = 0.89

    def update(self, screen):
        if self.jumping:
            self.jump_multiplier += 0.005

            self.y *= self.jump_multiplier

            if self.y >= self.y_base:
                self.y = self.y_base
                self.jump_multiplier = 0.89
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
        if self.hitbox.colliderect(obstacle.hitbox):
            if self.fading and type(obstacle) == Wall:
                return False
            else:
                return True
        return False