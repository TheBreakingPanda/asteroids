
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


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
