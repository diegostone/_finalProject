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

# #images

flower = pygame.image.load("finalresources/images/flower.png")

# # cannonBall = pygame.image.load()

bobOmb = pygame.image.load("finalresources/images/bob-omb.png")

# # gameover = pygame.image.load()

cloud = pygame.image.load("finalresources/images/cloud.png")

# # rope = pygame.image.load()

# #music


# # enemy = pygame.mixer.Sound()
# # drawBack = pygame.mixer.Sound()
# # shoot = pygame.mixer.Sound()

# # point1 = pygame.mixer.Sound()
# # point2 = pygame.mixer.Sound()
# # point3 = pygame.mixer.Sound()
# # point4 = pygame.mixer.Sound()

# # cloudm = pygame.mixer.Sound()

# # cloudHit = pygame.mixer.Sound()

# # warning = pygame.mixer.Sound()

# # scream = pygame.mixer.Sound()
#main music
pygame.mixer.init()
pygame.mixer.music.load("finalresources/audio/backgroundmusic.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

if pygame.mixer.music.get_busy() == False:
    pygame.mixer.music.rewind("finalresources/audio/backgroundmusic.mp3")


# # #loadimages


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
    def update(self):
        print()

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




    #Start the main loop for the run_game
    while True:
        screen.fill(0)
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
        timer = 1000
        timer-=1
        if timer <= 500:
            screen.blit(cloud,(10,10))
            

run_game()
