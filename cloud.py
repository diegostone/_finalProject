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

#variables used in main.py that need to be utilized in the class
game_settings = Settings()
background = pygame.image.load("finalresources/images/background.png")
background = pygame.transform.scale(background, (480, 640))
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
cloudimage = pygame.image.load('finalresources/images/cloud.png')

# defines the Cloud class with the super class of Sprite
class Cloud(Sprite):
    def __init__(self, game_settings, screen):
        # initializes the super class
        super(Cloud, self).__init__()
        self.screen = screen
        screen = pygame.display.get_surface()
        self.game_settings = game_settings
        self.image = pygame.image.load("finalresources/images/cloud.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # gets the x and y coordinate of the sprite and holds the values uses 'float'
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # uses this int to dictate how fast the sprite moves
        self.cloud_speed_factor = 1
        self.pos = self.rect.y
        self.rect.right = self.x
    # blits the image at the current position
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    # updates the pos of the image
    def update(self):
        # sets the x coordinate of the image to the current x coordinate plus the speed factor, to move it across the screen
        self.x += self.cloud_speed_factor
        #re-blits the background
        screen.blit(background,(0,0))
        self.rect.x = self.x
        self.rect.y = self.y
        print('forward')
        # once the image reaches a certain point, the speed factor is set to negative so the x coordinate becomes smaller and moves left
        if self.x == 416.0:
            self.cloud_speed_factor = -1
        if self.x == 30.0:
            self.cloud_speed_factor = 1
    
