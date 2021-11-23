import pygame
from pygame.locals import *
import random
from Light import Light
from Wall import Wall

class Game():

    def __init__(self, level, player, moving_speed):
        self.obstacle_prefabs = self.generate_prefabs(level)
        self.obstacles = []
        self.player = player
        self.level = level
        self.hit_count = 0
        self.r = 0
        self.show_hitboxes = False
        self.moving_speed = moving_speed
        # Anzeige Hit-User-Interface
        self.font = pygame.font.Font(None,25)
        self.hitUi = self.font.render('Hits: ' + str(self.hit_count), True, Color('white'))

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
                    self.player.gotHit = True
                    self.hit_count += 1
                    #Update Hit-User Interface
                    self.hitUi = self.font.render('Hits: ' + str(self.hit_count), True, Color('white'))

    def generate_prefabs(self, level):
        if level == 1:
            return [Light]
        if level == 2:
            return [Light, Wall]

    def add_random_obstacle(self):
        self.r = random.randrange(0, len(self.obstacle_prefabs))
        # Lantern
        if self.r == 0:
            self.obstacles.append(self.obstacle_prefabs[self.r](810, 270, 114, 117, self.moving_speed))
        # Wall
        if self.r == 1:
            self.obstacles.append(self.obstacle_prefabs[self.r](810, 0, 20, 447, self.moving_speed))
    
    def generate_random_time(self, level):
        if level == 1:
            r = random.randrange(3500, 6001)  
        if level == 2:
            r = random.randrange(2000, 3501)  
        return r