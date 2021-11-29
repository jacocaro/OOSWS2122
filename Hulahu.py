"""
WS 2021/22 - TH Brandenburg - OOS - Prof. Dr. Thomas Preuss
Semesterprojekt Python - Pygame - Sidescroller Hulahu
@author: Annemie Berning, Carolin Jacob
@version: 1.0
@date: 01.12.2021
"""

import pygame
from pygame.locals import *
import sys
from Endscreen import Endscreen
from Player import Player
from Game import Game
from Background import Background
from Startscreen import Startscreen
from Button import Button

class Hulahu():
    """
    initialized Game with mainloop

    Attributes
    ----------
    W, H : int - width and hight
    screen : Display - display module
    runner : Player - initialize player
    moving_speed : int - background scrolling speed
    buttonList, buttonListEndScreen : list - list of Buttons used in Start- and Endscreen  
    game : Game - initialize game
    clock : Clock - initialize clock module
    back_ground : Background - initialize Background
    final_screen : Endscreen - initialize Endscreen
    start_screen : Startscreen - initialize Startscreen
    speed : int - max Framerate
    startScreen : Boolean - activates startscreen
    levelRunning : Boolean - activates running mode 
    endScreen : Boolean - activates endscreen
    levelTime : int - millisec until running mode finishes 
    castleTime : int - millisec until castles is drawn
    showCastle : Boolean - activates castle
    owl, win : Sound - game sound
    channel1, channel2 : Channel - sound channel

    Methods
    -------
    initGame() : set caption, add user events
    newLevel(level, obstacles speed) : restarts level with given level and speed
    mainLoop() : game loop to run game with runnig mode, start- and endscreen
    """
    def __init__(self):
        self.W, self.H = 800, 447
        self.screen = pygame.display.set_mode(
            (self.W, self.H))  # setting screen
        self.screen.fill((255, 255, 255))
        self.runner = Player(200, 330, 40, 55)
        self.moving_speed = 5
        self.buttonList = [Button(10, 390, 107, 45, 'leicht'), Button(
            132, 390, 107, 45, 'schwer'), Button(254, 390, 107, 45, 'ende')]
        self.buttonListEndScreen = [Button(410, 390, 107, 45, 'leicht'), Button(
            532, 390, 107, 45, 'schwer'), Button(654, 390, 107, 45, 'ende')]
        self.game = Game(1, self.runner, 0)
        self.clock = pygame.time.Clock()
        self.back_ground = Background(self.moving_speed, self.game)
        self.final_screen = Endscreen(self.game, self.screen)
        self.start_screen = Startscreen(self.screen)
        self.speed = 30  # Max Framerate
        self.startScreen = True
        self.levelRunning = False
        self.endScreen = False
        self.levelTime = 20000
        self.castleTime = 14500
        self.showCastle = False
        self.owl = pygame.mixer.Sound('Sound/owl.wav')
        self.win = pygame.mixer.Sound('Sound/win.wav')
        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)

    def initGame(self):
        """
        set caption, add user events
        """
        pygame.display.set_caption('Hulahu auf Reisen')  # setting game title

        # Adding User events
        self.add_obstacle = pygame.USEREVENT + 1
        pygame.time.set_timer(
            self.add_obstacle, self.game.generate_random_time(self.game.level), loops=1)

        self.level_end_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.level_end_timer, self.levelTime, loops=1)

        self.show_castle_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.show_castle_timer, self.castleTime, loops=1)

    def newLevel(self, level, obstacleSpeed):
        """
        restarts level with given level and speed
        @param level: int
        @param obstacleSpeed: int
        """
        # initialize new game and new Background with new HitUi
        self.game = Game(level, self.runner, obstacleSpeed)
        self.back_ground = Background(self.moving_speed, self.game)

        # set needed event-timers
        pygame.time.set_timer(
            self.show_castle_timer, self.castleTime, loops=1)
        pygame.time.set_timer(
            self.add_obstacle, self.game.generate_random_time(self.game.level), loops=1)
        pygame.time.set_timer(
            self.level_end_timer, self.levelTime, loops=1)

        # set switches
        self.startScreen = False
        self.showCastle = False
        self.endScreen = False
        self.levelRunning = True

        # start sound
        self.channel2.play(self.owl)

    def mainLoop(self):
        """
        game loop to run game with runnig mode, start- and endscreen
        """
        while True:
            # Main loop
            while self.levelRunning:
                # Eventhandler: Cycles through all occurring events
                for event in pygame.event.get():
                    if event.type == self.add_obstacle:
                        self.game.add_random_obstacle(self.showCastle)
                        pygame.time.set_timer(
                            self.add_obstacle, self.game.generate_random_time(self.game.level), loops=1)
                    if event.type == self.show_castle_timer:
                        self.showCastle = True
                    if event.type == self.level_end_timer:
                        self.channel1.play(self.win)
                        self.endScreen = True
                        self.levelRunning = False

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                        if not(self.runner.jumping):
                            self.runner.jumping = True
                    if keys[pygame.K_h]:
                        self.game.show_hitboxes = not self.game.show_hitboxes
                    if keys[pygame.K_e] or keys[pygame.K_RIGHT]:
                        if not(self.runner.fading):
                            self.runner.fading = True

                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                self.back_ground.update(self.screen, self.showCastle)
                self.runner.update(self.screen)
                self.game.update_obstacles(self.screen, self.showCastle)
                pygame.display.update()
                self.clock.tick(self.speed)

            while self.startScreen:
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == MOUSEBUTTONDOWN:
                        if self.start_screen.collsionDetection(self.buttonList, pygame.mouse.get_pos()) == 'leicht':
                            self.newLevel(1,7)

                        elif self.start_screen.collsionDetection(self.buttonList, pygame.mouse.get_pos()) == 'schwer':
                            self.newLevel(2,10)

                        elif self.start_screen.collsionDetection(self.buttonList, pygame.mouse.get_pos()) == 'ende':
                            pygame.quit()
                            sys.exit()

                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                self.start_screen.update(self.screen, self.buttonList)
                pygame.display.update()

            while self.endScreen:
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == MOUSEBUTTONDOWN:
                        if self.final_screen.collsionDetection(self.buttonListEndScreen, pygame.mouse.get_pos()) == 'leicht':
                            self.newLevel(1,7)

                        elif self.final_screen.collsionDetection(self.buttonListEndScreen, pygame.mouse.get_pos()) == 'schwer':
                            self.newLevel(2,10)

                        elif self.final_screen.collsionDetection(self.buttonListEndScreen, pygame.mouse.get_pos()) == 'ende':
                            pygame.quit()
                            sys.exit()

                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                self.final_screen.update(self.screen, self.game, self.buttonListEndScreen, self.endScreen)
                pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    hulahu = Hulahu()
    hulahu.initGame()
    hulahu.mainLoop()
