'''
Created on 2020年6月2日

@author: Administrator
'''
import pygame
from pygame.locals import *





SCREEN_WIDTH = 1440
SCREEN_HIGHT = 900
BG_COLOR = pygame.Color(255,255,255)

class Game:
    '''
    游戏类功能：
    
    1.游戏开始
    2.游戏结束
    '''
    
    screen = None
    map = None
    robot = None

    def __init__(self):
        '''
        Constructor
        '''
        #self.map = map
    
    def startGame(self):
        pygame.init()
        Game.screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HIGHT))
        pygame.display.set_caption('地宝特攻')
        Game.map = Map(70,111)
        Game.robot = Robot(137,82)
        
        
        while True:
            self.screen.fill(BG_COLOR)
            self.getEvent()
            Game.map.display()
            Game.robot.display()
            pygame.display.update()
            
            
        
    def getEvent(self):
                
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.endGame()
                print('xiangshi')
            
    def endGame(self): 
        print('退出')
        pygame.quit()
                                                                                                                                             
class Robot:
    
    tick = None
    ANGEL = 0
    ANGEL1 = 0
    ANGELC = 90
    image = None
    image1 =None 
    
    def __init__(self,left,top):
        self.left = left
        self.top = top
    '''def reloadImage(self):
        Robot.image1= pygame.image.load('image/robotrunr.png')
        rect1 = Robot.image1.get_rect()
        rect3 = pygame.Rect(0,0,rect1.width // 2,rect1.height)
        Game.tick = pygame.time.Clock()
        
           
    def rotate(self):
        self.reloadImage()
        Game.screen.blit(Robot.image1,[self.left,self.top])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and 0<=event.pos[0]<=100 and 0<=event.pos[1]<=100:
                print('左转')
                Robot.ANGEL = Robot.ANGEL+90
                Robot.ANGEL1 = Robot.ANGEL%360
                print(Robot.ANGEL)
                print(Robot.ANGEL1)
                new_robot = pygame.transform.rotate(Robot.image1,Robot.ANGELC)
                robot = new_robot
                robot_rect = robot.get_rect()
                
                Map(70,111).display()
                Game.screen.blit(new_robot,[robot_rect.left,robot_rect.top])
                
                pygame.display.update()'''
    
    def display(self):
        
        #print(rect2.width)
        
        
        #self.animotionrun()
        self.animotionscan()
         
    
    def animotionrun(self):
        
        
        image1= pygame.image.load('image/robotrunr.png')
        rect1 = image1.get_rect()
        rect3 = pygame.Rect(0,0,rect1.width // 2,rect1.height)
        Game.tick = pygame.time.Clock()
        
        
        for n in range(2):
            Game.tick.tick(3)
            
            Game.screen.blit(image1,(self.left,self.top),rect3)#这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
            rect3.x+=rect3.width 
            print(rect3.x)
            if rect3.x>= 112:
                rect3.x = 0
            
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
        pass
    
    def display(self):
        
        mapimage = pygame.image.load('image\map12.jpg')
        Game.screen.blit(mapimage,(self.left,self.top))
        #pygame.display.update()
        
        
    
if __name__ == '__main__':
    
    Game().startGame()
    
    
    
     
        
