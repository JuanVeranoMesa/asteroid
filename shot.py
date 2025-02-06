import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape, pygame.sprite.Sprite):

    def __init__(self, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        x, y = position
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        self.velocity = velocity
        # Add to all containers
        for group in self.__class__.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
        
    def update(self, dt):
        self.position += self.velocity * dt