import math
import pygame
from sys import exit


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Background')
clock = pygame.time.Clock()

G = 1

class Body:
    def __init__(self, mass, radius, start_position):
        self.mass = mass
        self.radius = radius
        self.start_position = start_position
            
            
    def draw(self, surface, color):
        pygame.draw.circle(surface, color, self.start_position, self.radius)
        

planet1 = Body(1, 10, (width/2, height/2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Background        
    screen.fill('#000000')
    
    planet1.draw(screen, 'White')
    
    pygame.display.flip()
    clock.tick(60)