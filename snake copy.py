import pygame

blue= 0, 150, 200
green = 100, 255, 120
red = 255, 0, 0

pygame.init()
width, height = 720, 480
running = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')






snake_position = [360,240]
snake_speed = 15
direction = 'RIGHT'
snake_body = [[360,240],[350,240],[340,240],[330,240]]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and direction !='DOWN':
            direction = 'UP'
        if event.key == pygame.K_DOWN and direction !='UP':
            direction = 'DOWN'
        if event.key == pygame.K_LEFT and direction !='RIGHT':
            direction = 'LEFT'
        if event.key == pygame.K_RIGHT and direction !='LEFT':
            direction = 'RIGHT'


    screen.fill(green)#first
    
    
    
    
    for pos in snake_body:
        pygame.draw.rect(screen,blue,pygame.Rect(pos[0],pos[1],10, 10))
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    snake_body.insert(0,list(snake_position))
    
    pygame.display.flip()#last
    clock = pygame.time.Clock()
    clock.tick(snake_speed)


    

pygame.quit()