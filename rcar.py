import pygame
WHITE = (255,255,255)
class Car(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, colour, [0,0, width, height])
        #self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()

    def moveRight(self,pixels,max_x):
        new_x = self.rect.x + pixels
        max_x -= 19
        if new_x >= max_x:
            self.rect.x += 0
        else:
            self.rect.x += pixels
    def moveLeft(self,pixels,min_x):
        new_x = self.rect.x - pixels
        if new_x<=min_x:
            self.rect.x -= 0
        else:
            self.rect.x -= pixels
    def moveUp(self,pixels,min_y):
        new_y = self.rect.y - pixels
        if new_y<=min_y:
            self.rect.y -= 0
        else:
            self.rect.y -= pixels
    def moveDown(self,pixels,max_y):
        new_y = self.rect.y + pixels
        max_y -= 25
        if new_y>=max_y:
            self.rect.y -=0
        else:
            self.rect.y += pixels
