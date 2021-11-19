import pygame
from pygame.locals import *
import os
import sys

pygame.init()

W, H = 800, 447
screen = pygame.display.set_mode((W,H)) #setting screen 
screen.fill((255, 255, 255))
pygame.display.set_caption('Hiker') #setting game title


# -------------------------------- Klassen -------------------------------------------
class Player(object):
      run = pygame.image.load(os.path.join('Images','hiker.png')) # evtl später Array mit Bildern für Animation hinterlegen
      jump = pygame.image.load(os.path.join('Images','hiker.png')) # evtl später Array mit Bildern für Animation hinterlegen
      jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]

      def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.jumpCount = 0
        self.runCount = 0

      def update(self, screen):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            screen.blit(self.jump, (self.x,self.y)) # wenn Animation erfolgen soll: self.jump durch self.jump[gewünschte Anzahl] ersetzen
            self.jumpCount += 1

            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0 # um rennen Animation von Bild index 0 neu zu starten
            # ------------ hier weitere Moves einfügen 
            
        else:
            screen.blit(self.run, (self.x,self.y))
            # ----------- falls doch Animation gewünscht:
            # if self.runCount > 42:
            # self.runCount = 0
            # screen.blit(self.run, (self.x,self.y)): self.jump durch self.run[gewünschte Anzahl] ersetzen
            # self.runCount += 1  

class Light(object):
    light_img = pygame.image.load(os.path.join('images', 'bush.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, screen):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        # hier Code für Animation
        screen.blit(self.light_img, (self.x,self.y))

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

            # moving speed of images
            self.moving_speed = 5
         
      def update(self):
            # decrementing both x-values by speed-value
            self.bgX1 -= self.moving_speed
            self.bgX2 -= self.moving_speed

            # If variables exceed the width of the screen --> reset original position at the left
            if self.bgX1 <= -self.rectBGimg.width:
                  self.bgX1 = self.rectBGimg.width
            if self.bgX2 <= -self.rectBGimg.width:
                  self.bgX2 = self.rectBGimg.width

            screen.blit(self.bgimage, (self.bgX1, self.bgY1))
            screen.blit(self.bgimage, (self.bgX2, self.bgY2))

# ----------------- Variablen und Mainloop -------------------------------------
clock = pygame.time.Clock()
back_ground = Background()
runner = Player(200, 313, 64, 64)
speed = 30  # Max Framerate
light_test = Light(300, 270, 64, 64)

# Adding a new User event 
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 500)

# Main loop
while True:
      # Eventhandler: Cycles through all occurring events   
      for event in pygame.event.get():
            if event.type == inc_speed:
                  back_ground.moving_speed += 0.5   

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                  if not(runner.jumping):
                        runner.jumping = True

            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()

      back_ground.update()
      runner.update(screen)
      light_test.update(screen)


      pygame.display.update()
      clock.tick(speed)