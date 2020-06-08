'''
Created on 2020年6月2日

@author: Administrator
'''
import pygame
from pygame.locals import *
from _ast import If

#窗口宽度和高度
SCREEN_WIDTH = 1440
SCREEN_HIGHT = 900
#窗口背景色填充
BG_COLOR = pygame.Color(255,255,255)

class Game:
    '''
    游戏类功能：
    
    1.游戏开始
    2.游戏结束
    '''
    #定义窗口类变量
    screen = None  
    #定义地图类变量
    map = None
    #定义机器人类变量
    robot = None
    
    def __init__(self):
        '''
        Constructor
        '''
        #self.map = map
    
    def startGame(self):
        #pygame初始化
        pygame.init()
        #创建窗口对象，窗口可变大小
        Game.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT),RESIZABLE)
        #窗口标签显示‘地宝特攻’
        pygame.display.set_caption('地宝特攻')
        #创建地图对象
        Game.map = Map(70,111)
        #创建机器人对象
        Game.robot = Robot(137,82)        
        
        
        
        while True:
            #窗口填充色
            Game.screen.fill(BG_COLOR)
            Game.map.display()
            #Game.robot.display()
            self.getEvent()
            Game.robot.rotate()
            Game.robot.move()
            pygame.display.update()#
            
            
        
    def getEvent(self):
                
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.endGame()
                print('xiangshi')
            if event.type == pygame.MOUSEBUTTONDOWN and 0<=event.pos[0]<=100 and 0<=event.pos[1]<=100:
                Game.robot.rotateangel()
            if event.type == pygame.MOUSEBUTTONDOWN and 0<=event.pos[0]<=100 and 100<=event.pos[1]<=200: 
                Game.robot.is_move()
            if event.type == pygame.MOUSEBUTTONDOWN and 0<=event.pos[0]<=100 and 200<=event.pos[1]<=300: 
                Game.screen = pygame.display.set_mode((800,600))
                
    def endGame(self): 
        print('退出')
        pygame.quit()
                                                                                                                                             
class Robot:
    
    def __init__(self,left,top):
        
        self.images ={
             'r':pygame.image.load('image/robotrunr.png'),
             'u':pygame.image.load('image/robotrunu.png'),
             'l':pygame.image.load('image/robotrunl.png'),
             'd':pygame.image.load('image/robotrund.png')
             }
        self.direction='r'
        self.image=self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.angel = 0
        self.ismove = False
        
        
    def is_move(self):
        if self.ismove == True:
            self.ismove = False
        else:
            self.ismove = True
           
    def move(self):
        if self.ismove == True:
            if self.angel == 0:
                self.rect.x += 59
            elif self.angel == 90:
                self.rect.y -= 59
            elif self.angel == 180:
                self.rect.x -= 59
            elif self.angel == 270:
                self.rect.y += 59
            
        
           
    def rotateangel(self):
            
            self.angel = self.angel+90
        
            

    def display(self):
        
        #self.image= pygame.image.load('image/robotrunr.png')
        Game.screen.blit(self.image,self.rect)
        #self.rotate()
        
         
    
    def rotate(self):
        
        
        rect1 = pygame.Rect(0,0,self.rect.width // 2,self.rect.height)
        Game.tick = pygame.time.Clock()
        
        if self.angel % 360 == 0 :
            self.direction='r'
            self.image=self.images[self.direction]
            
            for n in range(2):
                Game.tick.tick(3)
                
                Game.screen.blit(self.image,(self.rect.left,self.rect.top),rect1)
                rect1.x+=rect1.width 
                print(rect1.x)
                if rect1.x>= 112:
                    rect1.x = 0
                
                pygame.display.update()
                
        elif self.angel % 360 == 90:
            self.direction='u'
            self.image=self.images[self.direction]
            
            for n in range(2):
                Game.tick.tick(3)
                
                
                Game.screen.blit(self.image,(self.rect.left,self.rect.top),rect1)#这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
                rect1.y+=rect1.height
                if rect1.y >= 112:
                    rect1.y = 0 
                pygame.display.update()
                
        elif self.angel % 360 == 180:
            self.direction='l'
            self.image=self.images[self.direction]
            for n in range(2):
                Game.tick.tick(3)
                
                Game.screen.blit(self.image,(self.rect.left,self.rect.top),rect1)#这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
                rect1.x+=rect1.width 
                print(rect1.x,rect1.width)
                if rect1.x>= 112:
                    rect1.x = 0
                
                pygame.display.update()
                
        elif self.angel % 360 == 270:
            self.direction='d'
            self.image=self.images[self.direction]
            for n in range(2):
                Game.tick.tick(3)
                
                Game.screen.blit(self.image,(self.rect.left,self.rect.top),rect1)#这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
                rect1.y+=rect1.height 
                print(rect1.x,rect1.width)
                if rect1.x>= 112:
                    rect1.x = 0
                
                pygame.display.update()

    
    def animotionscan(self):
        image = pygame.image.load('image/robotscan.png')
        rect = image.get_rect()
        rect2 = pygame.Rect(0,0,rect.width // 8,rect.height)
        Game.tick = pygame.time.Clock()
        for n in range(8):
            Game.tick.tick(3)
            Game.screen.blit(image,(self.left,self.top),rect2)#这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
            rect2.x+=rect2.width
            if rect2.x> 392:
                rect2.x = 0
            print(rect2.x)
            pygame.display.update()
        
         
        
    
class Map:
    
    def __init__(self,top,left):
        self.top = top
        self.left = left
        
    
    def display(self):
        
        mapimage = pygame.image.load('image\map12.jpg')
        Game.screen.blit(mapimage,(self.left,self.top))
        #pygame.display.update()
        
        
    
if __name__ == '__main__':
    
    Game().startGame()
    
    
    
     
        
