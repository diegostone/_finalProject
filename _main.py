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

# exit the program
# def events():
# 	for event in pygame.event.get():
# 		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
# 			pygame.quit()
# 			sys.exit()

#plays music and has it repeat forever
# pygame.mixer.init()
# pygame.mixer.music.load("finalresources/audio/backgroundmusic.mp3")
# pygame.mixer.music.play(-1, 0.0)
# pygame.mixer.music.set_volume(0.25)
#pygame.mixer
# if pygame.mixer.music.get_busy() == False:
#     pygame.mixer.music.rewind("finalresources/audio/backgroundmusic.mp3")


#loadimages

flower = pygame.image.load("finalresources/images/flower.png")
background = pygame.image.load("finalresources/images/background.png")
cannonimage = pygame.image.load("finalresources/images/cannon.png")
cannonimage = pygame.transform.scale(cannonimage, (50,50))
background = pygame.transform.scale(background, (480, 640))
flowerimage = pygame.transform.scale(flower, (45,45))
bobomb = pygame.image.load("finalresources/images/bob-omb.png")
# class for the width and height of the window and sets the background
class Flower(Sprite):
    def __init__(self, game_settings, screen):
        super(Flower, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("finalresources/images/flower.png")
        self.image = pygame.transform.scale(flower, (45,45))
        
        
    


class Cannon_balls(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        # self.image = pygame.Surface((10, 20))
        self.image = cannonimage
        self.image.set_colorkey(BLACK)
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        # eliminate if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Settings():
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 640
        self.background = pygame.image.load("finalresources/images/background.png")


 

class bobOmb(Sprite):
    def __init__(self, game_settings, screen):
        super(bobOmb, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("finalresources/images/bob-omb.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30,350)
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.bomb_speed_factor = 1
        self.pos = self.rect.y
        self.rect.right = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.y += self.bomb_speed_factor
        pygame.time.delay(10)
        screen.blit(background,(0,0))
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.right > 480:
            self.kill()
    #def moveLoop(self):
        
        


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
    pygame.display.set_caption("Bob-omb Squad")
    #enemy = bobOmb(game_settings, screen)

    print("screen spawned")
    #Start the main loop for the run_game
    Pclick = False
    Sclick = False
    timer = 0
    cannon = Cannon_ball(screen, game_settings)
    flower = Flower(game_settings, screen)
    bomb = bobOmb(game_settings, screen)
    #cloud = Cloud(screen, game_settings)
    

    while True:
        bomb.update()
        bomb.blitme()

        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # hi this is ben attempting to fix diego's code take 2000000:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouseX, mouseY = mouse[0], mouse[1]
                cannon.pos = mouse
                if (220 <= mouseX and 260 >= mouseX) and (360 <= mouseY and 400 >= mouseY):
                    Pclick = True
                    print("pclick set to true")
                # cannonRelease = False
            if event.type == pygame.MOUSEBUTTONUP:
                Pclick = False
                print("pclick set to false")
                timer = 0
                cannon.center = (240, 380)
                screen.blit(background,(0,0))
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Sclick = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    Sclick = True
            if Sclick == False:
                pass
            if Sclick == True:
                print('should be firing')
                print(cannon.new_pos)
                #cannon.fire()
                
                screen.blit(background,(0,0))

        if Pclick == True:
            timer += 1
            if timer >= 100:
                mouse = pygame.mouse.get_pos()
                newpos = mouse
                #print("cannon should be at " + str(mouse))

                screen.blit(background,(0,0))
                screen.blit(cannon.image, newpos)


                # print("im blitting I swear!")
        
                

        #screen.blit(background,(0,0))
        #screen.blit(background,(0,0))
        screen.blit(flower.image,(170,565))    
        screen.blit(flower.image,(92,565)) 
        screen.blit(flower.image,(262,565)) 
        screen.blit(flower.image,(340,565)) 
        screen.blit(cannon.image,(220,360))
        
        

    

        pygame.display.update()
       
            
    pygame.display.flip()    
    #starts timer for spawning
        

runGame()
