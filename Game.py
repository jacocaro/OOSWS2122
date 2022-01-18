import pygame
from pygame.locals import *
import random
from Light import Light
from Wall import Wall
from Castle import Castle

class Game():
    """
    obstacle utility class

    Attributes
    ----------
    obstacle_prefabs : list - list of used obstacles
    obstacles : list - list of obstacles 
    player : Player 
    level : int - level difficulty 
    hit_count : int - count number of hits
    r : int - random number
    obstacleCount : int - count number of obstacles in game 
    endscore : int - number for endscore
    show_hitboxes : Boolean - check for hitbox display
    obstacle_speed : int - obstacle moving speed
    castle : Castle 
    font : Font
    hitUi : Font - set text

    Methods
    -------
    update_obstacles(screen, showCastle) : move obstacle, check for collision, cont hits, calculates endscore
    generate_prefabs(level) : returns list of obstacles 
    add_random_obstacle(showCastle) : adds random obstacle to obstacle list
    generate_random_time(level) : generate random time between obstacles 

    """
    def __init__(self, level, player, obstacle_speed):
        self.obstacle_prefabs = self.generate_prefabs(level)
        self.obstacles = []
        self.player = player
        self.level = level
        self.hit_count = 0
        self.r = 0
        self.obstacleCount = 0
        self.endscore = 100
        self.show_hitboxes = False
        self.obstacle_speed = obstacle_speed
        self.castle = Castle(810, 220, 0, 0, 5)
        # Anzeige Hit-User-Interface
        self.font = pygame.font.Font(None,25)
        self.hitUi = self.font.render('Hits: ' + str(self.hit_count), True, Color('white'))

    def update_obstacles(self, screen, showCastle):
        """
        move obstacle, check for collision, cont hits, calculates endscore
        @param screen : Screen
        @param showCastle : Boolean
        """
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
        """
        returns list of obstacles 
        @param level : int
        """
        if level == 1:
            return [Wall]
        if level == 2:
            return [Wall, Light]

    def add_random_obstacle(self, showCastle):
        """
        adds random obstacle to obstacle list
        @param showCastle : Boolean
        """
        self.r = random.randrange(0, len(self.obstacle_prefabs))
        if showCastle == False:
            # Lantern
            if self.r == 1:
                self.obstacles.append(self.obstacle_prefabs[self.r](810, 270, 105, 105, self.obstacle_speed))
                self.obstacleCount += 1
            # Wall
            if self.r == 0:
                self.obstacles.append(self.obstacle_prefabs[self.r](810, -30, 20, 447, self.obstacle_speed))
                self.obstacleCount += 1
    
    def generate_random_time(self, level):
        """
        generate random time between obstacles 
        @param level: int
        """
        if level == 1:
            r = random.randrange(1500, 3000)  
        if level == 2:
            r = random.randrange(1000, 2500)  
        return r