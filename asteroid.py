import pygame #type: ignore
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

#Creates asteroid class, drawing from parent CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) #specifies drawing from CircleShape in case we inheret from somewhere else later
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            new_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(new_angle)
            v2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_one = Asteroid(self.position, new_radius)
            new_asteroid_one.velocity = v1 * 1.2

            new_asteroid_two = Asteroid(self.position, new_radius)
            new_asteroid_two.velocity = v2 * 1.2

        