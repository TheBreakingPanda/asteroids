
import pygame


# Base class for all circular game objects (player, asteroids, shots)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Register with sprite groups if the subclass has defined containers
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # Must be overridden by subclass to render the object
    def draw(self, screen):
        pass

    # Must be overridden by subclass to update state each frame
    def update(self, dt):
        pass

    # Returns True if this object overlaps with another CircleShape
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
