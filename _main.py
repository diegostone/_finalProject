# https://pastebin.com/MRBDdeku

# ''' I want to use pygame to recreate the  "bob-omb squad" minigame from Super Mario 64 DS. 
#         deals heavily with x y coordinates to register hits, and a high score point system
# https://youtu.be/h1FKzGk80Bo?t=842 : this is a video of what the game is 
# '''
''' I want to use pygame to recreate the  "bob-omb squad" minigame from Super Mario 64 DS. 
#         deals heavily with x y coordinates to register hits, and a high score point system
# https://youtu.be/h1FKzGk80Bo?t=842 : this is a video of what the game is 
I first main objective is to re-create the assets in the game using a sprite creator
I will need to learn how to use trigonometry to be able to align the angle of a mouse movement with the 
angle of the catapult and the cannon
The way it is too ambitious is with having different power levels in how far you pull the catapult, as 
that is hard and tedious
In a way that it is not ambitious enough is that it only takes place on one screen, and there is only one 
element to the game 
'''

from time import sleep
from random import randint
import math
import pygame
import pygame.locals 
import time 
import sys
from pygame.sprite import Sprite


#main music
pygame.mixer.init()
#pygame.mixer.music.load("finalresources/audio/backgroundmusic.mp3")
#pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.set_volume(0.25)

if pygame.mixer.music.get_busy() == False:
    pygame.mixer.music.rewind("finalresources/audio/backgroundmusic.mp3")


# # #loadimages

flower = pygame.image.load("finalresources/images/flower.png")
background = pygame.image.load("finalresources/images/background.png")
background = pygame.transform.scale(background, (480, 640))
flower = pygame.transform.scale(flower, (50,50))

class Settings():
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 640
        self.background = pygame.image.load("finalresources/images/background.png")

class Cloud():
    def __init__(self,screen,game_settings):
        self.screen = screen
        self.image = pygame.image.load("finalresources/images/cloud.png")
        self.game_settings = game_settings
        self.rect = self.image.get_rect()
        self.screen.rect = screen.get_rect()
        self.center = float(self.rect.centerx)

    #def update(self):
        
    def draw(self):
         self.screen.blit(self.image, self.rect)   

class bobOmb(Sprite):
    def __init__(self,screen,game_settings,pos,speed,velocity):
        self.screen = screen
        self.image = pygame.image.load("finalresources/images/bob-omb.png")
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.target = None
        self.position = list(self.rect.center)
        self.distance = None
        self.vec = None
        self.__dict__[self.vec]
        self.velocity = velocity
    def moveLoop(self):
        while True:
            count += 1
            if count == 10:
                count = 0
                bobOmb.move(0, 3)
    def location(self):
        self.x = x
        self.y = y
        self.xVelo = -self.velocity
    def draw(self):
        self.screen.blit(self.image, self.rect)
    

      

def run_game():
    #initialize pygame, settings, and screen object
    global game_settings
    global screen
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    #sets run_game to be true
    #run_game.has_been_called = True
    pass
    #initialize
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Bob-omb Squad")
    #enemy = bobOmb(game_settings, screen)


    #Start the main loop for the run_game
    while True:
        screen.fill(0)
        clock = pygame.time.Clock()
        clock.tick(0.5)

        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        screen.blit(background,(0,0))
        screen.blit(flower,(170,565))    
        screen.blit(flower,(92,565)) 
        screen.blit(flower,(262,565)) 
        screen.blit(flower,(340,565)) 
        pygame.display.update()

    #starts timer for spawning
        

run_game()
