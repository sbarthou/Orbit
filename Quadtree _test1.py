import pygame


pygame.init()
SIZE = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Quadtree')
clock = pygame.time.Clock()


class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        pygame.draw.circle(screen, 'white', (self.x, self.y), 5)
        
        
class Rectangle:
    # Constructor
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height        
        
        
class Quadtree:
    # Constructor
    def __init__(self, limite, n):
        self.limite = limite
        self.capacidad = n
        self.Main = Rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)
        self.NW = None
        self.NE = None
        self.SW = None
        self.SW = None
        
    def subdivision(self):
        self.NW = Rectangle(self.Main.x/2, self.Main.y/2, self.Main.width/2, self.Main.height/2)
        self.NE = Rectangle(self.Main.x*(3/2), self.Main.y/2, self.Main.width/2, self.Main.height/2)
        self.SW = Rectangle(self.Main.x/2, self.Main.y*(3/2), self.Main.width/2, self.Main.height/2)
        self.SE = Rectangle(self.Main.x*(3/2), self.Main.y*(3/2), self.Main.width/2, self.Main.height/2)
        
    def sub_lines(self):
        pygame.draw.line(screen, 'green', (0, self.NW.height), (self.NW.width, self.NW.height))
        pygame.draw.line(screen, 'green', (self.NW.width, 0), (self.NW.width, self.NW.height))
        pygame.draw.line(screen, 'green', (self.NE.width, self.NE.height), (self.NE.width*2, self.NE.height))
        # pygame.draw.line(screen, 'green', (self.NE.width, 0), (self.NE.width, self.NE.height))
        # pygame.draw.line(screen, 'green', (0, self.SW.height), (self.SW.width, self.SW.height))
        pygame.draw.line(screen, 'green', (self.SW.width, self.SW.height), (self.SW.width, self.SW.height*2))
        # pygame.draw.line(screen, 'green', (self.SE.width, self.SE.height), (self.SE.width*2, self.SE.height))
        # pygame.draw.line(screen, 'green', (self.SE.width, self.SE.height), (self.SE.width, self.SE.height*2))
        
        
quad = Quadtree(0, 0)
quad.subdivision()
  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.fill('black')
    
    
    
    pygame.display.flip()
    # clock.tick(60)