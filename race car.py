import pygame

from rcar import Car
pygame.init()
width, height = 500, 500
running = True
screen = pygame.display.set_mode((width, height))
background_colour = 0, 150, 200
GREEN = (100,255,200)
GRAY = (210,210,210)
WHITE = (255,255,255)
RED = (255,0,0)
PURPLE = (255,0,255)

all_sprite_list = pygame.sprite.Group()
playerCar1 = Car(GREEN, 20, 30)
playerCar1.rect.x = 200
playerCar1.rect.y = 300

playerCar2 = Car(RED, 20, 30)
playerCar2.rect.x = 400
playerCar2.rect.y = 100

all_sprite_list.add(playerCar1)
all_sprite_list.add(playerCar2)






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    collide = playerCar1.rect.colliderect(playerCar2)

    if collide:
        playerCar1.rect.x = 200
        playerCar1.rect.y = 300
        playerCar2.rect.x = 100
        playerCar2.rect.y = 100
    else:


    
        if keys[pygame.K_LEFT]:
            playerCar1.moveLeft(1,-1)
        if keys[pygame.K_a]:
            playerCar2.moveLeft(1,-1)
        if keys[pygame.K_RIGHT]:       
            playerCar1.moveRight(1,width)
        if keys[pygame.K_d]:
            playerCar2.moveRight(1,width)
        if keys[pygame.K_UP]:
               playerCar1.moveUp(1,-1)
        if keys[pygame.K_w]:
            playerCar2.moveUp(1,-1)
        if keys[pygame.K_DOWN]:
            playerCar1.moveDown(1,height)
        if keys[pygame.K_s]:
            playerCar2.moveDown(1,height)
    

    screen.fill(background_colour)#first
    pygame.draw.rect(screen,GRAY, [40,0,200,500])
    pygame.draw.line(screen,WHITE,[140,0], [140,500],5)
    all_sprite_list.draw(screen)
    clock = pygame.time.Clock()
    clock.tick(200)
    pygame.display.flip()#last


    

pygame.quit()