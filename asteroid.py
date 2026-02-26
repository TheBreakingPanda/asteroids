import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    """Represents a single asteroid in the game world."""

    def __init__(self, x, y, radius):
        """Initialize the asteroid at (x, y) with the given radius."""
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asteroid as a white circle outline on the given surface."""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Move the asteroid along its velocity vector, scaled by delta time."""
        self.position += self.velocity * dt