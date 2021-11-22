import pygame
from pygame.locals import *
import os
import sys
import random

pygame.init()

W, H = 800, 447
screen = pygame.display.set_mode((W, H))  # setting screen
screen.fill((255, 255, 255))
pygame.display.set_caption('Hulahu auf Reisen')  # setting game title


# -------------------------------- Klassen -------------------------------------------
class Player(object):
    # evtl später Array mit Bildern für Animation hinterlegen
    run = pygame.image.load(os.path.join('Images', 'ghost.png'))
    # evtl später Array mit Bildern für Animation hinterlegen
    jump = pygame.image.load(os.path.join('Images', 'ghost.png'))
    fade = pygame.image.load(os.path.join('Images', 'ghost_trans.png'))
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
        self.runCount = 0
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
                self.runCount = 0  # um rennen Animation von Bild index 0 neu zu starten
        
        if self.fading:
            screen.blit(self.fade, (self.x, self.y))
            self.fadeCount += 1

            if self.fadeCount > 20:
                self.fadeCount = 0
                self.fading = False
                self.runCount = 0  # um rennen Animation von Bild index 0 neu zu starten

        else:
            screen.blit(self.run, (self.x, self.y))
            # ----------- falls doch Animation gewünscht:
            # if self.runCount > 42:
            # self.runCount = 0
            # screen.blit(self.run, (self.x,self.y)): self.jump durch self.run[gewünschte Anzahl] ersetzen
            # self.runCount += 1

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def collide(self, obstacle):
        if self.hitbox.colliderect(obstacle.hitbox):
            if self.fading and type(obstacle) == Wall:
                return False
            else:
                return True
        return False

class Light(object):
    light_img = pygame.image.load(os.path.join('images', 'lantern.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False

    def update(self, screen):

        # verschiebe sprite auf x-Achse nach links entsprechend moving_speed
        self.x -= moving_speed
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        screen.blit(self.light_img, (self.x, self.y))

class Wall(object):
    light_img = pygame.image.load(os.path.join('images', 'wall.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_collided = False

    def update(self, screen):

        # verschiebe sprite auf x-Achse nach links entsprechend moving_speed
        self.x -= moving_speed
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        screen.blit(self.light_img, (self.x, self.y))

class Background():
    def __init__(self):
        self.bgimage = pygame.image.load(os.path.join(
            'Images', 'background.png')).convert()  # first bg-image
        self.rectBGimg = self.bgimage.get_rect()  # second bg-image

        # first point top left
        self.bgY1 = 0
        self.bgX1 = 0

        # second point one bgimage.with next to it
        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

    def update(self):
        # decrementing both x-values by speed-value
        self.bgX1 -= moving_speed
        self.bgX2 -= moving_speed

        # If variables exceed the width of the screen --> reset original position at the left
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

        screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        screen.blit(self.bgimage, (self.bgX2, self.bgY2))


class Game():

    def __init__(self, level, player):
        self.obstacle_prefabs = self.generate_prefabs(level)
        self.obstacles = []
        self.player = player
        self.hit_count = 0
        self.show_hitboxes = False

    def update_obstacles(self, screen):
        for obstacle in self.obstacles:

            if obstacle.x < -150:
                self.obstacles.pop(self.obstacles.index(obstacle))
            else:
                obstacle.update(screen)

            if self.show_hitboxes:
                pygame.draw.rect(screen, (255, 0, 0), obstacle.hitbox, 2)
                pygame.draw.rect(screen, (255, 0, 0), self.player.hitbox, 2)

            if self.player.collide(obstacle):
                if obstacle.is_collided == False:
                    obstacle.is_collided = True
                    self.hit_count += 1
                    pygame.display.set_caption('Hulahu, Collide count: ' + str(self.hit_count))

    def generate_prefabs(self, level):
        if level == 1:
            return [Light]
        if level == 2:
            return [Light, Wall]

    def add_random_obstacle(self):
        r = random.randrange(0, len(self.obstacle_prefabs))
        # Lantern
        if r == 0:
            self.obstacles.append(self.obstacle_prefabs[r](810, 270, 114, 117))
        # Wall
        if r == 1:
            self.obstacles.append(self.obstacle_prefabs[r](810, 0, 20, 447))


# ----------------- Variablen und Mainloop -------------------------------------
runner = Player(200, 313, 40, 55)
game = Game(2, runner)
clock = pygame.time.Clock()
back_ground = Background()
speed = 30  # Max Framerate
moving_speed = 5

# Adding User events
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 500)

add_obstacle = pygame.USEREVENT + 2
pygame.time.set_timer(add_obstacle, 2000)

# Main loop
while True:
    # Eventhandler: Cycles through all occurring events
    for event in pygame.event.get():
        # if event.type == inc_speed:
        #      moving_speed += 0.5
        if event.type == add_obstacle:
            game.add_random_obstacle()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not(runner.jumping):
                runner.jumping = True
        if keys[pygame.K_h]:
            game.show_hitboxes = not game.show_hitboxes
        if keys[pygame.K_e] or keys[pygame.K_RIGHT]:
            if not(runner.fading):
                runner.fading = True

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    back_ground.update()
    runner.update(screen)
    game.update_obstacles(screen)
    pygame.display.update()
    clock.tick(speed)
