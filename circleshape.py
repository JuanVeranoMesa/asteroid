import pygame # type: ignore

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, target):
        #establish the vector positions for distance
        v1 = pygame.Vector2(self.position)
        v2 = pygame.Vector2(target.position)
        
        #find distance, return True if distance between the circles is less than two radius added
        if v1.distance_to(v2) <= (self.radius + target.radius):
            return True
        else:
            return False