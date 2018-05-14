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
flower = pygame.image.load("finalresources/images/flower.png")
flowerimage = pygame.transform.scale(flower, (45,45))

# defines the Flower class with the super class of Sprite
class Flower(Sprite):
    def __init__(self, game_settings, screen):
        super(Flower, self).__init__()
        self.screen = screen
        screen = pygame.display.get_surface()
        self.game_settings = game_settings
        self.image = pygame.image.load("finalresources/images/flower.png")
        self.image = pygame.transform.scale(flower, (45,45))
        # gives the flower sprite a rectangle for a hitbox
        self.rect = self.image.get_rect()
        
