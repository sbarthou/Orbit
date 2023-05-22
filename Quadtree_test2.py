import pygame
import random


pygame.init()
SIZE = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Quadtree')
clock = pygame.time.Clock()
screen.fill('black')



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        pygame.draw.circle(screen, 'white', (self.x, self.y), 5)
        
        

# Creador de cuadrado con su centro y dimensiones (puede dibujar lineas)        
class Cuadrado:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self):
        pygame.draw.line(screen, 'green', ((self.x - self.width/2), self.y), ((self.x + self.width/2), self.y))
        pygame.draw.line(screen, 'green', (self.x, (self.y - self.height/2)), (self.x, (self.y + self.height/2)))
        
        

# Toma como parámetro un Cuadrado y divide en subcuadrados        
def divide(cuadrado, coord):
    new_width = cuadrado.width / 2
    
    if coord == 'nw':
        nw = Cuadrado(new_width/2, new_width/2, new_width, new_width)
        nw.draw()
    elif coord == 'ne':
        ne = Cuadrado((cuadrado.width - new_width/2), new_width/2, new_width, new_width)
        ne.draw()
    
    
    
def count(points, cuadrado, limite):
    c = {'nw': 0, 'ne': 0, 'sw': 0, 'se': 0}
    lista = []
    for point in points:
        
        if c['nw'] <= limite:
            if point.x < cuadrado.x and point.y < cuadrado.y:
                c['nw'] += 1
                if c['nw'] > limite:
                    lista.append('nw')
        
        if c['ne'] <= limite:        
            if point.x >= cuadrado.x and point.y < cuadrado.y:
                c['ne'] += 1
                if c['ne'] > limite:
                    lista.append('ne')
                
        if c['sw'] <= limite:
            if point.x < cuadrado.x and point.y >= cuadrado.y:
                c['sw'] += 1
                if c['sw'] > limite:
                    lista.append('sw')
            
        if c['se'] <= limite:    
            if point.x >= cuadrado.x and point.y >= cuadrado.y:
                c['se'] += 1
                if c['se'] > limite:
                    lista.append('se')
    return lista
        

        
points = []        
for i in range(10):
    point = Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    points.append(point)
        
        

limite = 2        
cuadrado1 = Cuadrado(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)
dividir = count(points, cuadrado1, limite)

    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.fill('black')
    
    
    for point in points:
        point.draw()
        
    cuadrado1.draw()
    
    for i in dividir:
        divide(cuadrado1, i)
    
    
    pygame.display.flip()
    # clock.tick(60)