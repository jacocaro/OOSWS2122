import pygame
from pygame.locals import *
import sys
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
game = Game(2, runner, moving_speed)
clock = pygame.time.Clock()
back_ground = Background(moving_speed, game)
speed = 30  # Max Framerate

# Adding User events
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 500)

add_obstacle = pygame.USEREVENT + 2
pygame.time.set_timer(add_obstacle, game.generate_random_time(game.level), loops=1)

if __name__ == '__main__':
    # Main loop
    while True:
        # Eventhandler: Cycles through all occurring events
        for event in pygame.event.get():
            # if event.type == inc_speed:
            #      moving_speed += 0.5
            if event.type == add_obstacle:
                game.add_random_obstacle()
                pygame.time.set_timer(add_obstacle, game.generate_random_time(game.level), loops=1)

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
