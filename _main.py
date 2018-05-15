#Used code from Mr. Cozort's shmup and code writeen by Ben McCardy

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
#imports libraries
from time import sleep
import math
import pygame.locals 
import time 
import sys
from pygame.sprite import Sprite
import random
import pygame
from cloud import Cloud
from bomb import bobOmb
from settings import Settings
from flower import Flower

#plays music and has it repeat forever
pygame.mixer.init()
pygame.mixer.music.load("finalresources/audio/backgroundmusic.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
#loops the music forever / took this code for shmup by Chris Cozort
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.25)

#loadimages
background = pygame.image.load("finalresources/images/background.png")
cannonimage = pygame.image.load("finalresources/images/cannon.png")
#changes the dimensions of the images to make them larger
cannonimage = pygame.transform.scale(cannonimage, (50,50))
background = pygame.transform.scale(background, (480, 640))
# flowerimage = pygame.transform.scale(flower, (45,45))
bobomb = pygame.image.load("finalresources/images/bob-omb.png")
#defines class for the cannon ball with a super class of Sprite
class Cannon_ball(pygame.sprite.Sprite):
    def __init__(self, screen, game_settings):
        #defines the image and transforms its dimensions
        self.image = pygame.image.load("finalresources/images/cannon.png") 
        self.image = pygame.transform.scale(self.image, (50,50))
        screen = pygame.display.get_surface()
        self.game_settings = game_settings
        self.surface = pygame.surface
        self.rect = self.image.get_rect()
#         #finds the x and y coordinate of the images rectangle and sets into the position
        self.pos = [self.rect.x,self.rect.y]
        self.new_pos = [self.rect.x,self.rect.y]
#         #finds the coordinates of the mouse position
        self.mouse_pos = pygame.mouse.get_pos()
#         # get angle from mouse xy and player xy
        self.angle = math.atan2(self.mouse_pos[1]-(self.pos[1]+32),self.mouse_pos[0]-(self.pos[0]+26))
#         # rotation based on mouse position
        self.rot = pygame.transform.rotate(self.image, 360-self.angle*57.29)
#         # projectile speed
        self.velx = 1
        self.vely = 1
#         # get radians value from mouse xy and player xy
        self.rads = math.atan2(self.mouse_pos[1]-(self.rect.y), self.mouse_pos[0]-(self.rect.x))
    def fire(self):
        self.velx = math.cos(self.rads)*1
        self.vely = math.sin(self.rads)*1
        self.rect.x += self.velx 
        self.rect.y -= self.vely
        mouse_x = pygame.mouse.get_pos()[0]
        print(mouse_x)
        self.new_pos = [self.rect.x, self.rect.y]
        self.rect = self.new_pos
        self.rect.y += self.vely
        print("it fired (not really yet)")
    def blitme(self):
        screen.blit(self.image, self.new_pos)
#         # print(self.pos)
        print("draw cannon is calling")
    
#function that takes a new entity from the sprite group
def runGame():
    #initialize pygame, settings, and screen object
    global game_settings
    global screen
    game_settings = Settings()
    #sets screen to the width and height of the window, so assets can be blited in the window
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    #initialize
    pygame.init()
    #sets the window caption to "Bob-omb Squad"
    pygame.display.set_caption("Bob-omb Squad")
    # global variables used later on and also defines variable using the classes
    Pclick = False
    Sclick = False
    timer = 0
    cannon = Cannon_ball(screen, game_settings)
    flower = Flower(game_settings, screen)
    bomb = bobOmb(game_settings, screen)
    cloud = Cloud(game_settings, screen)
    all_sprites = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

# creates while true loop to have a continuing loop for the game
    while True:
        cloud.update()
        cloud.blitme()
        # if the event is that the user tries to exit the window, it closes the python window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Ben McCardy wrote this code (line 156-169)
            #checks if the user clicks down the left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                # sets the mouse variable to the coordinate position of the mouse cursor
                mouse = pygame.mouse.get_pos()
                mouseX, mouseY = mouse[0], mouse[1]
                cannon.pos = mouse
                # checks if the click was made in a certain area of the screen
                if (220 <= mouseX and 260 >= mouseX) and (360 <= mouseY and 400 >= mouseY):
                    Pclick = True
                    print("pclick set to true")
            # when the user release the mouse button it resets everything and moves the cannonball back
            if event.type == pygame.MOUSEBUTTONUP:
                Pclick = False
                print("pclick set to false")
                timer = 0
                cannon.center = (240, 380)
                screen.blit(background,(0,0))
           # checks if the spacebar button is clicked down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Sclick = True
            # checks if the space bar button is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    Sclick = True
            if Sclick == False:
                pass
            # if Slick is true, then it calls on the function to fire the cannon
            if Sclick == True:
                print('should be firing')
                print(cannon.new_pos)
                #cannon.fire()
                screen.blit(background,(0,0))
        # if the mouse button is being clicked
        if Pclick == True:
            timer += 1
            # after a ceetain amount of time, "mouse" gathers the current mouse position
            if timer >= 100:
                mouse = pygame.mouse.get_pos()
                newpos = mouse
                # blits the background and then the cannonball over the background at the current mouse position
                screen.blit(background,(0,0))
                screen.blit(cannon.image, newpos)
                
        # blits all the assets at the beginning at specific coordinates
        screen.blit(flower.image,(170,565))    
        screen.blit(flower.image,(92,565)) 
        screen.blit(flower.image,(262,565)) 
        screen.blit(flower.image,(340,565)) 
        screen.blit(cannon.image,(220,360))
        
        # updates the pygame window to display the new blits
        pygame.display.update()
       
    # flips the screen for the user      
    pygame.display.flip()
 
# calls on the rungame function with the whule true loop
runGame()
