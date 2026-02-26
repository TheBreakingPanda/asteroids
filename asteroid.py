
import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


# Represents a single asteroid in the game world
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Renders the asteroid as a white circle outline
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # Moves the asteroid along its velocity vector, scaled by delta time
    def update(self, dt):
        self.position += self.velocity * dt

    # Destroys this asteroid and spawns two smaller ones if above minimum size
    def split(self):
        self.kill()

        # Only split if the resulting fragments will be above the minimum size threshold
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Log the split event for debugging and analytics purposes
        log_event("asteroid_split")

        # Generate two new velocity vectors by rotating the original velocity by a random angle in both directions
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # Create two new asteroids at the same position with the reduced radius and new velocities
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

