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
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.fading = False
        self.fadeCount = 0
        self.jumpCount = 0
        self.hit = False
        self.gothitcount = 0
        self.colliding = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, screen):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            # wenn Animation erfolgen soll: self.jump durch self.jump[gewünschte Anzahl] ersetzen
            screen.blit(self.jump, (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
        
        if self.fading:
            screen.blit(self.fade, (self.x, self.y))
            self.fadeCount += 1
            if self.fadeCount > 20:
                self.fadeCount = 0
                self.fading = False

        if self.hit:
            screen.blit(self.ghostHit, (self.x, self.y))
            self.gothitcount += 1
            if self.gothitcount > 5:
                self.gothitcount = 0
                self.hit = False
                      
        if not self.hit and not self.fading:
            screen.blit(self.run, (self.x, self.y))

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def collide(self, obstacle):
        if self.hitbox.colliderect(obstacle.hitbox):
            if self.fading and type(obstacle) == Wall:
                return False
            else:
                self.hit = True
                return True
        return False