import math
import random
import pygame
import itertools
from sys import exit


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Orbit')
clock = pygame.time.Clock()

G = 0.1

class Body():
    def __init__(self, mass, radius, x, y, vx, vy):
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0
        
        
    def set_vx(self, value):
        self.vx = value
        
    def set_vy(self, value):
        self.vy = value
                
    def set_ax(self, value):
        self.ax = value
                
    def set_ay(self, value):
        self.ay = value
                
                
    def change_x(self, value):
        self.x += value
                
    def change_y(self, value):
        self.y += value
                
    def change_vx(self, value):
        self.vx += value
            
    def change_vy(self, value):
        self.vy += value
            
            
    def animate(self):
        self.change_vx(self.ax)
        self.change_vy(self.ay)
                
        self.change_x(self.vx)
        self.change_y(self.vy)
            
            
    def gravitate(self, body2):
        dx = abs(self.x - body2.x)
        dy = abs(self.y - body2.y)
        
        if dx < self.radius and dy < self.radius:
            pass
        else:
            try:
                r = math.sqrt(dx**2 + dy**2)        
                a = (G*body2.mass)/(r**2)      
                theta = math.asin(dy/r)
                ax = math.sin(theta)*a
                ay = math.cos(theta)*a
                        
                if self.x > body2.x :
                    self.set_ax(-ax)
                else:
                    self.set_ax(ax)
                    
                if self.y > body2.y :
                    self.set_ay(-ay)
                else:
                    self.set_ay(ay)
            except ZeroDivisionError:
                pass
                    
                    
    def draw(self, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)


bodies = []
for i in range(50):
    body = Body(1, 3, random.randint(0, width), random.randint(0, height), 0, 0)
    bodies.append(body)
    
body_pairs = list(itertools.combinations(bodies, 2))


# sun = Body(1000, 20, (width/2), (height/2), 0, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.fill('#000000')
    
    # sun.draw('yellow')
    
    for body1, body2 in body_pairs:
        body1.gravitate(body2)
        body2.gravitate(body1)
        body1.animate()
        body2.animate()
        body1.draw('white')
        body2.draw('white')
        
    # for body in bodies:
    #     body.gravitate(sun)
    #     body.animate()
    #     body.draw('white')
    
    pygame.display.flip()
    clock.tick(60)