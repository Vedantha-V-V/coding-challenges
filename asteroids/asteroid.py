import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid split")
        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
        new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2

