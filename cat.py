import pygame, sys
from pygame.locals import *
from math import *

pygame.init()
pygame.font.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')
font = pygame.font.SysFont('Comic Sans MS',16)

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
theta=0
speed=5
time=0
count=0



while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    gametime=font.render('Your Game Time: '+str(time),False, (0,0,0) )
    DISPLAYSURF.blit(gametime,(10,10))  #display game time
    catx = catx + speed*sin(theta)
    caty = caty + speed*cos(theta)
    if catx<5:
        theta = -theta
    if catx>680:
        theta = -theta
    if caty<5:
        theta = pi - theta
    if caty > 520:
        theta = pi - theta

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_LEFT]:
                theta = theta + 3./speed
            if pygame.key.get_pressed()[K_RIGHT]:
                theta = theta - 3./speed
            if pygame.key.get_pressed()[K_UP]:
                speed = speed  * 1.05 
            if pygame.key.get_pressed()[K_DOWN]:
                speed = speed * 0.95

    #get game time            
    count = count +1
    if count == FPS:
        time = time +1
        count = 0

    pygame.display.update()
    fpsClock.tick(FPS)
# -*- coding: cp936 -*-
#!/usr/bin/env python
background_image_filename = 'wood.png'

import pygame, sys
from pygame.locals import *
from math import *
from random import *
from Tkinter import*

# set up the window
pygame.init()
pygame.font.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("chenglingjian's Adventure")
background = pygame.image.load(background_image_filename).convert()
font = pygame.font.SysFont('Comic Sans MS',16)
WHITE = (255, 255, 255)


#basic data
catx, caty = 10, 10
token_x, token_y = 400, 300
speed =  5
theta=[0]*100
time = count = score = 0
time_limit=60
catImgload = pygame.image.load('cat.png')
img = pygame.image.load('apple.png')
catImg=pygame.transform.scale(catImgload,(50,50))
token = pygame.transform.scale(img,(50,50))
catplay=[0]*100
catx=[6]*100
caty=[6]*100
anxial = anxiar = anxiau = anxiad = 0


#main loop
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background,(0,0))
    
    DISPLAYSURF.blit(token, (token_x, token_y)) #draw the token


#refresh time and score    
    for i in range(99,0,-1):
        catplay[i]=pygame.transform.rotate(catImg,theta[i]*57.29)
        
        DISPLAYSURF.blit(catplay[i], (catx[i], caty[i]))
        
    

    gametime = font.render('Time Left: '+str(time_limit - time),False, (0,0,0) )
    show_score = font.render('Your Score: '+str(score),False, (0,0,0) )
    DISPLAYSURF.blit(gametime,(10,10))  #display game time
    DISPLAYSURF.blit(show_score,(10,30))  #display score


    dis = sqrt((catx[0] - token_x)**2+(caty[0] - token_y)**2) #calculate the distance
    
    
#movement of cat    
    for i in range(99):
        catx[99-i]=catx[98-i]
        caty[99-i]=caty[98-i]
        theta[99-i]=theta[98-i]
        
    catx[0] = catx[0] + speed*sin(theta[0])
    caty[0] = caty[0] + speed*cos(theta[0])

    if catx[0]<5:
        theta[0] = -theta[0]
    if catx[0]>750:
        theta[0] = -theta[0]
    if caty[0]<5:
        theta[0] = pi - theta[0]
    if caty[0] > 550:
        theta[0] = pi - theta[0]

    #update game time  and score    
    count = count +1
    if count == FPS:
        time = time +1
        count = 0
    if dis<50:
        token_x = 750*random()
        token_y = 550*random()
        score += 1


#control the cat
    
    for event in pygame.event.get():   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                
                anxial = 1
            if event.key == K_RIGHT:
                
                anxiar = 1
            if event.key == K_UP:
                
                anxiau = 1
            if event.key == K_DOWN:
                
                anxiad = 1
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                anxial = 0
            if event.key == K_RIGHT:
                anxiar = 0
            if event.key == K_UP:
                anxiau = 0
            if event.key == K_DOWN:
                anxiad = 0


    if anxial == 1:
        theta[0] = theta[0] + 1./speed
    if anxiar == 1:
        theta[0] = theta[0] - 1./speed
    if anxiau == 1:
        speed = speed  * 1.05
    if anxiad == 1:
        speed = speed * 0.95




    pygame.display.update()
    fpsClock.tick(FPS)
