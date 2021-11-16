import pygame
from pygame.locals import *
import os
import sys

pygame.init()

W, H = 800, 447
screen = pygame.display.set_mode((W,H)) #setting screen 
screen.fill((255, 255, 255))
pygame.display.set_caption('Hiker') #setting game title


class Background():
      def __init__(self):
            self.bgimage = pygame.image.load(os.path.join('Images','background.png')).convert() #first bg-image
            self.rectBGimg = self.bgimage.get_rect() #second bg-image 

            # first point top left
            self.bgY1 = 0
            self.bgX1 = 0
 
            # second point one bgimage.with next to it 
            self.bgY2 = 0
            self.bgX2 = self.rectBGimg.width

            #moving speed of images
            self.moving_speed = 5
         
      def update(self):
            #decrementing both x-values by speed-value
            self.bgX1 -= self.moving_speed
            self.bgX2 -= self.moving_speed

            # If variables exceed the width of the screen --> reset original position at the left
            if self.bgX1 <= -self.rectBGimg.width:
                  self.bgX1 = self.rectBGimg.width
            if self.bgX2 <= -self.rectBGimg.width:
                  self.bgX2 = self.rectBGimg.width
             
      def render(self):
            # method to draw the background to the screen
            screen.blit(self.bgimage, (self.bgX1, self.bgY1))
            screen.blit(self.bgimage, (self.bgX2, self.bgY2))

clock = pygame.time.Clock()
back_ground = Background()

run = True
speed = 30  #Speed for moving background

#Adding a new User event 
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 500)

# Main loop
while run:
     #Cycles through all occurring events   
      for event in pygame.event.get():
            if event.type == inc_speed:
                 speed += 0.5     
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
      back_ground.update()
      back_ground.render()
    
      pygame.display.update()
      clock.tick(speed)