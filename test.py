'''
Created on 2020年6月5日

@author: Administrator
'''
import pygame
from pygame.locals import *

SCREEN_WIDTH = 1440
SCREEN_HIGHT = 900
BG_COLOR = pygame.Color(255,255,255)
pygame.init()
screen = pygame.display.set_mode([1024,768])
screen.fill(BG_COLOR)
robot= pygame.image.load('image/robotrunr.png')
#screen.blit(robot,[0,0])
pygame.display.flip()

angelc = 90
angel = 0
angel1= 0



while True:
    #pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and 0<=event.pos[0]<=100 and 0<=event.pos[1]<=100:
            print('左转')
            angel=angel+90
            angel1=angel%360
            print(angel)
            print(angel1)
            new_robot = pygame.transform.rotate(robot,angelc)
            robot = new_robot
            robot_rect = robot.get_rect()
            #screen.fill([245,245,245])
            #screen.blit(bg,[0,0])
            screen.blit(robot,[400,400])
            #screen.blit(btn_left,[650,0])
            #screen.blit(btn_ahead,[650,40])
            pygame.display.update()
            
        if event.type == pygame.QUIT:
            pygame.quit()
            
