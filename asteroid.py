import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # First kill the current asteroid
        self.kill()
    
        # If too small, just return - no splitting
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Calculate new properties for the split asteroids
        random_angle = random.uniform(20, 50)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2