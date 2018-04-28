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
import math
import pygame.locals 
import time 
import sys
from pygame.sprite import Sprite
import random
import pygame



#main music
pygame.mixer.init()
#pygame.mixer.music.load("finalresources/audio/backgroundmusic.mp3")
#pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.set_volume(0.25)

#if pygame.mixer.music.get_busy() == False:
 #   pygame.mixer.music.rewind("finalresources/audio/backgroundmusic.mp3")


# # #loadimages

flower = pygame.image.load("finalresources/images/flower.png")
background = pygame.image.load("finalresources/images/background.png")
cannon = pygame.image.load("finalresources/images/cannon.png")
cannon = pygame.transform.scale(cannon, (50,50))
background = pygame.transform.scale(background, (480, 640))
flower = pygame.transform.scale(flower, (45,45))
bobomb = pygame.image.load("finalresources/images/bob-omb.png")

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
    def __init__(self,screen,game_settings,pos,speed,velocity,location):
        self.screen = screen
        self.image = pygame.image.load("finalresources/images/bob-omb.png")
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.target = None
        self.position = self.image.get_rect()
        self.distance = None
        self.vec = None
        self.__dict__[self.vec]
        self.velocity = velocity
    def moveLoop(self):
        while True:
            for x in range(100):
                screen.blit(background, self.position, self.position)
                self.screen.blit(self.image, self.position)
                pygame.display.update()
                
    def location(self):
        self.x = x
        self.y = y
        self.xVelocity = -self.velocity
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
class Cannon_ball():
    def __init__(self, screen, game_settings):
        self.image = pygame.image.load("..stone_diego/finalresources/images/cannon.png")
        self.screen = screen
        self.game_settings = game_settings
        # self.pos = pos
        # self.speed = speed
        # self.distance = distance
        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect(32,32,32,32)
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def location(self):
        print("something")
        # self.x = x
        # self.y = y

def runGame():
    #initialize pygame, settings, and screen object
    global game_settings
    global screen
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    #sets run_game to be true
    #run_game.has_been_called = Tru
    #initialize
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Bob-omb Squad")
    #enemy = bobOmb(game_settings, screen)
    
    handled = False
    #Start the main loop for the run_game
    while True:
        spawntimer=-1
        screen.fill(0)
        ev = pygame.event.get()
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos == (220,360):
                    print("clicked!")

        cannon = Cannon_ball(screen, game_settings)
        cannon.draw
        if pygame.mouse.get_pressed()[0] and Cannon_ball.rect.collidepoint(pygame.mouse.get_pos()):
            print("worked")



        screen.blit(background,(0,0))
        screen.blit(flower,(170,565))    
        screen.blit(flower,(92,565)) 
        screen.blit(flower,(262,565)) 
        screen.blit(flower,(340,565)) 
        screen.blit(cannon,(220,360))

        pygame.display.update()
        # spawntimer = 100
        # spawntimer1 = 0
        # bombs = [[480, 100]]

        # if spawntimer == 0:
        #     bombs.append([random.randint(0,480), 640])
        #     spawntimer=100-(spawntimer1*2)
        #     if spawntimer1>=35:
        #         spawntimer1=35
        #     else:
        #         spawntimer1+=5
        # index=0
        # for bomb in bombs:
        #     if bomb[0]<-64:
        #         bombs.pop(index)
        #     bomb[0]-=7
             
        #     bombrect=pygame.Rect(bobomb.get_rect())
        
        #     bombrect.top=bomb[1]
        #     bombrect.bottom=bomb[0]
        #     if bombrect.bottom<64:
        #         bombs.pop(index)
              
           

        #     index+=1
        # for bomb in bombs:
        #     screen.blit(bobomb, bomb)

            
    pygame.display.flip()    
    #starts timer for spawning
        

runGame()
