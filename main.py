# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    #Group containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for collide in asteroids:
            if  collide.collision_check(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        #You call screen here because it has the width and height
        #otherwise you would call pygame.Surface.fill() to create the screen
        #with particular inputs
        
        for draw in drawable:
            draw.draw(screen)


        pygame.display.flip()
        
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
    #The if __name__ == "__main__": block checks whether the script is being run directly.
    #If it is, the block of code beneath it will execute.
    #If the script is imported, the block will not run.