# imports the libraries
from time import sleep
import math
import pygame.locals 
import time 
import sys
from pygame.sprite import Sprite
import random
import pygame
from settings import Settings
from flower import Flower

#variables used in main.py that need to be utilized in the class
game_settings = Settings()
background = pygame.image.load("finalresources/images/background.png")
background = pygame.transform.scale(background, (480, 640))
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
flower = pygame.image.load("finalresources/images/flower.png")
flowerimage = pygame.transform.scale(flower, (45,45))

#defines the bomb class with the super class of Sprite
class bobOmb(Sprite):
    def __init__(self, game_settings, screen):
        # initializes the super class of Sprite
        super(bobOmb, self).__init__()
        self.screen = screen
        screen = pygame.display.get_surface()
        self.game_settings = game_settings
        self.image = pygame.image.load("finalresources/images/bob-omb.png")
        self.rect = self.image.get_rect()
        # sets the x coordinate of the image to a random integer between 30 and 350
        self.rect.x = random.randint(30,350)
        self.rect.y = self.rect.height
        # gets the x and y coordinate of the image and holds them
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # speed factor to dictate how quickly the bomb moves
        self.bomb_speed_factor = 1
        self.pos = self.rect.y
        self.rect.right = self.x
        #self.changepos = (self.x, 493)
        #self.dx = self.dx
        #blits the image at the current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # updates the position of the sprite
    def update(self):
        # takes the current y coordinate of the image and adds to it the speed factor, moving it down the screen
        self.y += self.bomb_speed_factor
        # waits 10 miliseconds
        pygame.time.delay(10)
        screen.blit(background,(0,0))
        self.rect.x = self.x
        self.rect.y = self.y
        # if the bomb moves 480 pixels to the right, it destorys itself
        if self.rect.right > 480:
            self.kill()

            
    # def checkCollision(self, sprite1, sprite2):
    #      if pygame.sprite.spritecollideany(flower, bobOmb):
    #          print('hit')
    # def changeDirection(self):
    #     if self.y == self.changepos:
    #         print("reached")

