import pygame

pygame.init()
width, height = 500, 500
running = True
screen = pygame.display.set_mode((width, height))

background_colour = 0, 150, 200

spinning_cat = pygame.image.load("spinning_cat.jfif")
spinning_cat = pygame.transform.scale(spinning_cat,(50,40))

spinning_cat_rect = spinning_cat.get_rect()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background_colour)#first

    screen.blit(spinning_cat, spinning_cat_rect)

    pygame.display.flip()#last
    

pygame.quit()