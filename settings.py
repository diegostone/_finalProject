# imports the libraries
from time import sleep
import math
import pygame.locals 
import time 
import sys
from pygame.sprite import Sprite
import random
import pygame

# class for Settings
class Settings():
    def __init__(self):
        # sets the pixel width and height and loads the background image
        self.screen_width = 480
        self.screen_height = 640
        self.background = pygame.image.load("finalresources/images/background.png")
