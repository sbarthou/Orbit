import pygame
import numpy as np


pygame.init()
SIZE = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Quadtree')
clock = pygame.time.Clock()




class Punto:
    def __init__(self, radio, x, y):
        self.radio = radio
        self.x = x
        self.y = y
        
    def draw(self, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radio)

        
    
    
class Cuadrado:
    def __init__(self, center, width, height):
        self.center = np.asarray(center)
        self.width = width
        self.height = height
        self.NO = np.array([(center[0] - width/4), (center[1] - height/4)])
        self.NE = np.array([(center[0] + width/4), (center[1] - height/4)])
        self.SO = np.array([(center[0] - width/4), (center[1] + height/4)])
        self.SE = np.array([(center[0] + width/4), (center[1] + height/4)])
        
        
    def draw_lines(self):
        pygame.draw.line(screen, 'green', (0, self.height/2), (self.width, self.height/2))
        pygame.draw.line(screen, 'green', (self.width/2, 0), (self.width/2, self.height))
        



class Quadtree:
    def __init__(self, cuadrado):
        self.cuadrado = cuadrado
        self.NO = Cuadrado(cuadrado.NO, cuadrado.width/2, cuadrado.height/2)
        self.NE = Cuadrado(cuadrado.NE, cuadrado.width/2, cuadrado.height/2)
        self.SO = Cuadrado(cuadrado.SO, cuadrado.width/2, cuadrado.height/2)
        self.SE = Cuadrado(cuadrado.SE, cuadrado.width/2, cuadrado.height/2)
        
        
        
        
cuadrado = Cuadrado((WIDTH/2, HEIGHT/2), WIDTH, HEIGHT)

quad = Quadtree(cuadrado)


        

# puntos = []
# for i in range(4):
#     punto = Punto(5, random.randint(0, WIDTH), random.randint(0, HEIGHT))
#     puntos.append(punto)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.fill('#000000')
    
    cuadrado.draw_lines()
    quad.NO.draw_lines()
    quad.NE.draw_lines()
    
    pygame.display.flip()
    # clock.tick(60)