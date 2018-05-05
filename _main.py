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

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

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
# cannonimage = pygame.image.load("finalresources/images/cannon.png")
# cannonimage = pygame.transform.scale(cannonimage, (50,50))
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
    
class Cannon_ball(pygame.sprite.Sprite):
    def __init__(self, screen, game_settings, surface):
        self.image = pygame.image.load("finalresources/images/cannon.png") 
        self.image = pygame.transform.scale(self.image, (50,50))
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
       # self.vector = vector
        self.game_settings = game_settings
        self.surface = pygame.surface
        # self.pos = pos
        # self.speed = speed
        # self.distance = distance
        self.rect = self.image.get_rect()
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos
    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # self.x = x
        # self.y = y
# class Point(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(pygame.sprite.Sprite, self).__init__()
#         self.rect = pygame.Rect(x,y,x+1,y+1)

# collisions = pygame.sprite.collide(Point(x,y), False)

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

    print("screen spawned")
    handled = False
    #Start the main loop for the run_game
    Pclick = False
    timer = 0
    cannon = Cannon_ball(screen,game_settings, pygame.surface)
    while True:
        pos1 = pygame.mouse.get_pos()
        # if codeTimerFPS <= 1000:
        #     codeTimerFPS += 1
        # else:
        #     print("This code ran 1000 times. \n\n my name is diego and i can't write code \n\n ---------")
        #     codeTimerCount += 1
        #     if codeTimerCount >= 10:
        #         time = 1
        #         print("string" + time)
        #     codeTimerFPS = 0
        spawntimer=-1
        # screen.fill(0)
        ev = pygame.event.get()
        # cannon = Cannon_ball(screen, game_settings, pygame.surface)
        # cannon.update
        cannon = Cannon_ball(screen,game_settings,pygame.surface)
        # bomb = bobOmb(screen, game_settings,"","","","")
        # bomb.moveLoop
        #Watch for keyboard and mouse events
        screen.blit(background,(0,0))
        # screen.blit(flower,(170,565))    
        # screen.blit(flower,(92,565)) 
        # screen.blit(flower,(262,565)) 
        # screen.blit(flower,(340,565)) 
        screen.blit(cannon.image,(220,360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for event in ev:
            # hi this is ben attempting to fix diego's code take 2000000:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouseX, mouseY = mouse[0], mouse[1]
                if (220 <= mouseX and 260 >= mouseX) and (360 <= mouseY and 400 >= mouseY):
                    Pclick = True
                    print("pclick set to true")
            # if event.type == pygame.MOUSEBUTTONUP:
            #     Pclick = False
            #     print("pclick set to false")
            #     timer = 0
            #     moveX, moveY = 0, 0
            #     cannon.center = (240, 380)
        if Pclick == True:
            timer += 1
            if timer >= 50:
                print("timer hit 50")
                mouse = pygame.mouse.get_pos()
                cannon.center = mouse
                screen.blit(cannon.image,cannon.center)
                print("im blitting I swear!")
            # if event.type == pygame. and Pclick == False:
            #     pos = pygame.mouse.get_pos()
            #     Pclick = True
            #     #Ben McCardy wrote this code :)
            #     if (220 <= pos[0] and 260 >= pos[0]) and (360 <= pos[1] and 400 >= pos[1]):
            #         print("works")
            #         Pclick = True
            #         print("pclick set to true")
            # elif event.type == pygame.K_SPACE:
            #     print("pclick set to true ran")
            #     #screen.blit(cannon.image,(posX,posY))
            #     i+=1
            #     print(i)
            #     if i == 0:
            #         pos = pygame.mouse.get_pos()
            #     if i == 60:
            #         pos2 = pygame.mouse.get_pos()
            #         i == 0
            #         moveDist[0] += pos2[0]-pos[0]
            #         moveDist[1] += pos2[1]-pos[1]
            #         print(moveDist)
            #     if moveDist[0] >= 15 or moveDist[1] >= 15:
            #         cannon.move(moveDist[0], moveDist[1])
            #         print("cannon moved")
            #     if event.type == pygame.MOUSEBUTTONUP:
            #         Pclick = False
            #         moveDist = [0,0]
            #         i=0
                


        
        
        

    

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
