import pygame
import time

pygame.init()
width, height = 500, 500
running = True
screen = pygame.display.set_mode((width, height))

background_colour = 0, 150, 200

background_colour1 = 0, 0, 200
spinning_cat = pygame.image.load("spinning_cat.jfif")
spinning_cat = pygame.transform.scale(spinning_cat,(60,40))

spinning_cat_rect = spinning_cat.get_rect()


screen.fill(background_colour)#first

cat_speed = [1,1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    

    screen.blit(spinning_cat, spinning_cat_rect)
    print(spinning_cat_rect.topleft)
    spinning_cat_rect = spinning_cat_rect.move(cat_speed)

    if spinning_cat_rect.left <0 or spinning_cat_rect.right > width:
        cat_speed[0] = -cat_speed[0]
        print("hi")
    if spinning_cat_rect.top <0 or spinning_cat_rect.bottom > height:
        cat_speed[1] = -cat_speed[1]
        print("hi")

    if spinning_cat_rect.left <=1 and spinning_cat_rect.bottom >= 460:
        print("hii")
        screen.fill(background_colour)

    elif spinning_cat_rect.left <=1 and spinning_cat_rect.top <=1:
        print("hii")
        screen.fill(background_colour)
    if spinning_cat_rect.right >=440 and spinning_cat_rect.bottom >=460:
        print("hii")
        screen.fill(background_colour)
    elif spinning_cat_rect.right >=440 and spinning_cat_rect.top <=1:
        print("hii")
        screen.fill(background_colour)
        

    pygame.display.flip()#last

    time.sleep(10/1000)
    

pygame.quit()