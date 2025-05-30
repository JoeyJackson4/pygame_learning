import pygame

pygame.init()
width, height = 500, 500
running = True
screen = pygame.display.set_mode((width, height))

background_colour = 0, 150, 200

rect_colour = 155,0,255
circle_colour = 255, 0 , 0


screen.fill(background_colour)#first

center_cord = 250 ,250

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, rect_colour, pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen, circle_colour, center_cord, 15)
    pygame.draw.line(screen,(0,255,50),(280,280),(140,280),10)
    pygame.draw.polygon(screen,(0,0,255),((5,5),(6,6),(7,7),(8,6),(5,5)),5)
    pygame.draw.polygon(screen,(0,255,255),[(150,150),(120,180),(135,210),(165,210),(180,180)])
    pygame.draw.circle(screen, (255,255,255), (300,300), 20)
    pygame.draw.circle(screen, (255,255,255), (315,300), 15)
    pygame.draw.circle(screen, (255,255,255), (285,300), 15)

    pygame.display.flip()#last


    

pygame.quit()