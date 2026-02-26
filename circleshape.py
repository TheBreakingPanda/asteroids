import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for all circular game objects (player, asteroids).
    
    Subclasses must override draw() and update().
    If a subclass defines a 'containers' class attribute before instantiation,
    instances will register themselves with those sprite groups automatically.
    """

    def __init__(self, x, y, radius):
        # Register with sprite groups if containers are defined on the subclass
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Override in subclass to render the object."""
        pass

    def update(self, dt):
        """Override in subclass to update state each frame."""
        pass

    def collides_with(self, other):
        """Return True if this object collides with another CircleShape."""
        distance_squared = (self.position - other.position).length_squared()
        radius_sum = self.radius + other.radius
        return distance_squared < radius_sum * radius_sum