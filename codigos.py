class Planet:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
sun = Planet(25, 1000)
earth = Planet(5, 20)

def dist(xy):
    sun_xy = [width/2, height/2]
    return math.dist(sun, xy)
        
def gForce(M, m, r):
    return constants.G*((M*m)/r**2)