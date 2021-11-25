import pygame
import os
from pygame.locals import *
import random
from Light import Light
from Wall import Wall
from Castle import Castle

class Game():

    def __init__(self, level, player, moving_speed, obstacle_speed):
        self.obstacle_prefabs = self.generate_prefabs(level)
        self.obstacles = []
        self.player = player
        self.level = level
        self.hit_count = 0
        self.r = 0
        self.obstacleCount = 0
        self.endscore = 100
        self.show_hitboxes = False
        self.moving_speed = moving_speed
        self.obstacle_speed = obstacle_speed
        self.castle = Castle(810, 220, 0, 0, 5)
        # Anzeige Hit-User-Interface
        self.font = pygame.font.Font(None,25)
        self.hitUi = self.font.render('Hits: ' + str(self.hit_count), True, Color('white'))

    def update_obstacles(self, screen, showCastle):
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
                    self.endscore = int((self.obstacleCount-self.hit_count) / (self.obstacleCount/100))
                    #Update Hit-User Interface
                    self.hitUi = self.font.render('Hits: ' + str(self.hit_count), True, Color('white'))
        if showCastle:
            self.castle.update(screen)

    def generate_prefabs(self, level):
        if level == 1:
            return [Wall]
        if level == 2:
            return [Wall, Light]

    def add_random_obstacle(self, showCastle):
        self.r = random.randrange(0, len(self.obstacle_prefabs))
        if showCastle == False:
            # Lantern
            if self.r == 1:
                self.obstacles.append(self.obstacle_prefabs[self.r](810, 270, 114, 117, self.obstacle_speed))
                self.obstacleCount += 1
            # Wall
            if self.r == 0:
                self.obstacles.append(self.obstacle_prefabs[self.r](810, -30, 20, 447, self.obstacle_speed))
                self.obstacleCount += 1
      
    
    def generate_random_time(self, level):
        if level == 1:
            r = random.randrange(1500, 3000)  
        if level == 2:
            r = random.randrange(1000, 2500)  
        return r