import pygame
from pygame.locals import *
import sys
from Endscreen import Endscreen
from Player import Player
from Game import Game
from Background import Background

pygame.init()

W, H = 800, 447
screen = pygame.display.set_mode((W, H))  # setting screen
screen.fill((255, 255, 255))
pygame.display.set_caption('Hulahu auf Reisen')  # setting game title

# ----------------- Variablen und Mainloop -------------------------------------

runner = Player(200, 313, 40, 55)
moving_speed = 5
game = Game(1, runner, moving_speed)
clock = pygame.time.Clock()
back_ground = Background(moving_speed, game)
final_screen = Endscreen(game)
speed = 30  # Max Framerate
startScreen = False
levelRunning = True
endScreen = False
levelTime = 15000
castleTime = 10000
showCastle = False

# Adding User events
add_obstacle = pygame.USEREVENT + 1
pygame.time.set_timer(add_obstacle, game.generate_random_time(game.level), loops=1)

level_end_timer = pygame.USEREVENT + 2
pygame.time.set_timer(level_end_timer, levelTime, loops=1)

show_castle_timer = pygame.USEREVENT + 3
pygame.time.set_timer(show_castle_timer, castleTime, loops=1)

if __name__ == '__main__':

    while True:
        # Main loop
        while levelRunning:
            # Eventhandler: Cycles through all occurring events
            for event in pygame.event.get():
                if event.type == add_obstacle:
                    game.add_random_obstacle(showCastle)
                    pygame.time.set_timer(add_obstacle, game.generate_random_time(game.level), loops=1)
                if event.type == show_castle_timer:
                    showCastle = True
                if event.type == level_end_timer:
                    endScreen = True
                    levelRunning = False

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

            back_ground.update(screen)
            runner.update(screen)
            game.update_obstacles(screen)
            pygame.display.update()
            clock.tick(speed)
        
        while endScreen:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    # initialize new game and new Background with new HitUi
                    game = Game(1, runner, moving_speed)
                    back_ground = Background(moving_speed, game)

                    # set needed event-timers
                    pygame.time.set_timer(add_obstacle, game.generate_random_time(game.level), loops=1)
                    pygame.time.set_timer(level_end_timer, levelTime, loops=1)

                    # set switches
                    levelRunning = True
                    endScreen = False

                if keys[pygame.K_RIGHT]:
                    # initialize new game and new Background with new HitUi
                    game = Game(2, runner, moving_speed)
                    back_ground = Background(moving_speed, game)

                    # set needed event-timers
                    pygame.time.set_timer(add_obstacle, game.generate_random_time(game.level), loops=1)
                    pygame.time.set_timer(level_end_timer, levelTime, loops=1)

                    # set switches
                    levelRunning = True
                    endScreen = False
            
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            final_screen.update(screen, game)
            pygame.display.update()

