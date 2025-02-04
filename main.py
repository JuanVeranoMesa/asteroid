import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init() #initializes pygame

clock = pygame.time.Clock() #This creates a universal clock variable

#placeholder container
AsteroidField.containers = ()

#start of functions
def main():
    #create groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    asteroidfield_group = pygame.sprite.Group()
    
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (asteroidfield_group, updatable_group)
    
    #create asteroid field
    asteroid_field = AsteroidField()
    updatable_group.add(asteroid_field)
    
    #sets up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #I believe this puts the player in the middle of the screen
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True: #This is an infinite loop which runs the game and what is called for each run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update game state
        dt = clock.tick(60) / 1000 #This limits the amount of runs per second to 60 for 60 FPS
        updatable_group.update(dt)
        
        #draw everything
        screen.fill((0, 0, 0))
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()