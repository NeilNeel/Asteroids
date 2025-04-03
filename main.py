from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt = 0    # Delta time (amount of time between a change)

    # Create a sprite group for the player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    # Assign static containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)

    #Create game objects
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, shots_group)
    asteroid_field = AsteroidField()  # Create an AsteroidField instance

    # Add player and asteroid field to update group
    updatable.add(player)
    drawable.add(player)
    updatable.add(asteroid_field)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black
        screen.fill((0,0,0))
        # Draw the player
        for i in drawable:
            i.draw(screen)
        updatable.update(dt)
        
        for asteroid in asteroids:
            if CircleShape.collide(player, asteroid):  # Correct collision check
                print("Collision! Game Over!")
                pygame.quit()
                exit()

    
        # Update the display
        pygame.display.flip()

        dt = Clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()