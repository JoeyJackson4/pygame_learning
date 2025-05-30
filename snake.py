import pygame
import time
import random
blue= 0, 150, 200
green = 100, 255, 120
red = 255, 0, 0


score = 0

pygame.init()
width, height = 720, 480
running = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')






snake_position = [360,240]
snake_speed = 15
direction = 'RIGHT'
snake_body = [[360,240],[350,240],[340,240],[330,240]]


fruit_position = [random.randint(1,71),random.randint(1,47)]
fruit_position[0] = fruit_position[0]*10
fruit_position[1] = fruit_position[1]*10
print(snake_position)
print(fruit_position)
def endgame():
    my_font = pygame.font.SysFont('comicsansms',50)

    game_over_surface = my_font.render('GAME OVER',True,red)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.center = [(width/2), (height/2)]

    screen.blit(game_over_surface,game_over_rect)
    
    
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and direction !='DOWN':
            direction = 'UP'
            eat = False
        if event.key == pygame.K_DOWN and direction !='UP':
            direction = 'DOWN'
            eat = False
        if event.key == pygame.K_LEFT and direction !='RIGHT':
            direction = 'LEFT'
            eat = False
        if event.key == pygame.K_RIGHT and direction !='LEFT':
            direction = 'RIGHT'
            eat = False
        


    screen.fill(green)#first
    
    
    
    
    for pos in snake_body:
        pygame.draw.rect(screen,blue,pygame.Rect(pos[0],pos[1],10, 10))
    pygame.draw.circle(screen,red,(fruit_position[0],fruit_position[1]),5)
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    snake_body.insert(0,list(snake_position))

    
    if snake_position == fruit_position:
        fruit_position = [random.randint(0,71),random.randint(0,47)]
        fruit_position[0] = fruit_position[0]*10
        fruit_position[1] = fruit_position[1]*10
    else:
        snake_body.pop()
    
        
    pygame.display.flip()#last
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

    if snake_position[0] <0 or snake_position[0] >width:
        endgame()
    if snake_position[1] <0 or snake_position[1] >height-10:
        endgame()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            endgame()

    

pygame.quit()