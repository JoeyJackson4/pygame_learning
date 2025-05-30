import pygame
import time
import random

pygame.init()
width, height = 500, 500
running = True
screen = pygame.display.set_mode((width, height))

background_colour = 0, 150, 200

background_colour1 = 0, 0, 200

spinning_cat = pygame.image.load("spinning_cat.jfif")
spinning_cat = pygame.transform.scale(spinning_cat,(60,40))
spinning_cat_rect = spinning_cat.get_rect()

crosshairs = pygame.image.load("crosshair.png")
crosshairs = pygame.transform.scale(crosshairs,(60,40))
crosshairs_rect =  crosshairs.get_rect()
pos = [250,250]
use_Bullet = False
screen.fill(background_colour)#first
bullets = 6
cat_speed = [0,0]
cat_speed[0] = random.randint(-5,5)
cat_speed[1] = random.randint(-5,5)
kill = False
bounce = 0
lose = False
hits = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if crosshairs_rect.center[0] < spinning_cat_rect.right and crosshairs_rect.center[0] > spinning_cat_rect.left and crosshairs_rect.center[1] < spinning_cat_rect.bottom and crosshairs_rect.center[1] > spinning_cat_rect.top:
                if bullets >0:
                    if kill == False:
                        print("TES")
                        kill = True
                        cat_speed = [0,0]
                        bullets += 1
                        bounce = 0
                        hits += 1
                else:
                    print("no more bullets")
            if crosshairs_rect.center[0] > spinning_cat_rect.right: 
                if bullets >0:
                    if kill == False:
                        print("no")
                        use_Bullet = True
                else:
                    print("no more bullets")
            if crosshairs_rect.center[0] < spinning_cat_rect.left: 
                if bullets >0:
                    if kill == False:
                        print("no")
                        use_Bullet = True
                else:
                    print("no more bullets")
                    bounce = 9
            if crosshairs_rect.center[1] > spinning_cat_rect.bottom: 
                if bullets >0:
                    if kill == False:
                        print("no")
                        use_Bullet = True
                else:
                    print("no more bullets")
            if crosshairs_rect.center[1] < spinning_cat_rect.top:
                if bullets >0:
                    if kill == False:
                        print("no")
                        use_Bullet = True
                else:
                    print("no more bullets")
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_a:
                pos = (crosshairs_rect.center[0]-20, crosshairs_rect.center[1])
            if event.key ==  pygame.K_d:
                pos = (crosshairs_rect.center[0]+20, crosshairs_rect.center[1])
            if event.key ==  pygame.K_w:
                pos = (crosshairs_rect.center[0], crosshairs_rect.center[1]-20)
            if event.key ==  pygame.K_s:
                pos = (crosshairs_rect.center[0], crosshairs_rect.center[1]+20)
            if event.key == pygame.K_r:
                kill = False
                cat_speed[0] = random.randint(-5,5)
                cat_speed[1] = random.randint(-5,5)
                print(cat_speed)
            
            


    
    crosshairs_rect.center = pos

    screen.fill(background_colour)
    if kill == False:
        screen.blit(spinning_cat, spinning_cat_rect)
    if lose == False:
        screen.blit(crosshairs,crosshairs_rect)
    if hits == 5:
        print("you win")
        crosshairs_rect.center = [250,250]
        hits = 0
        screen.blit(crosshairs,crosshairs_rect)

    #print(spinning_cat_rect.topleft)
    
    spinning_cat_rect = spinning_cat_rect.move(cat_speed)

    if spinning_cat_rect.left <0 or spinning_cat_rect.right > width:
        cat_speed[0] = -cat_speed[0]
        
        bounce += 1
        print(bounce)
    if spinning_cat_rect.top <0 or spinning_cat_rect.bottom > height:
        cat_speed[1] = -cat_speed[1]
        
        bounce += 1
        print(bounce)
        

    if bounce == 10:
        print("you lose")
        bullets = 0
        cat_speed = [0,0]
        bounce = 0
        lose = True
        spinning_cat_rect.center = [250,250]
    if use_Bullet == True:
        bullets = bullets-1
        use_Bullet = False
    pygame.display.flip()#last

    time.sleep(10/1000)
    

pygame.quit()