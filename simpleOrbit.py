import pygame
import numpy as np
from sys import exit


pygame.init()

# Screen
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Background')
clock = pygame.time.Clock()

sun = pygame.Rect(width/2 - 50, height/2 - 50, 100, 100)   # pygame.Rect(x, y, width, height) El punto (0,0) del Rectangle es la esquina superior izquiera!

def circle_orbit(theta):   # función que retorna el valor de x e y según el theta entregado para generar circunferencia
    x = np.cos(theta)*150 + width/2   # + width/2 para establecer x en el centro más el valor de cos(theta)*radio
    y = np.sin(theta)*150 + height/2   # + height/2 para establecer x en el centro más el valor de cos(theta)*radio
    return x, y

theta = np.linspace(0, 2*np.pi, 100)
t_index = 0

running = True
# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Background        
    screen.fill('#000000')
    
    pygame.draw.line(screen, '#FFFFFF', (width/2, height/2), circle_orbit(theta[t_index]))
    pygame.draw.ellipse(screen, '#FFC700', sun)                
    pygame.draw.circle(screen, '#FFFFFF', (width/2, height/2), radius=(circle_orbit(2*np.pi)[0] - width/2), width=1)
    pygame.draw.circle(screen, '#0069BE', circle_orbit(theta[t_index]), radius=10)
    
    t_index += 1
    if t_index > len(theta)-1:
        t_index = 0
    
    pygame.display.flip()
    clock.tick(30)