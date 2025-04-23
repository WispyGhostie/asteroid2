# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        #You call screen here because it has the width and height
        #otherwise you would call pygame.Surface.fill() to create the screen
        #with particular inputs
        
        player.draw(screen)


        pygame.display.flip()
        
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
    #The if __name__ == "__main__": block checks whether the script is being run directly.
    #If it is, the block of code beneath it will execute.
    #If the script is imported, the block will not run.