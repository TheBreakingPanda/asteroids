import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    """Represents a shot fired by the player."""
    def __init__(self, x, y, angle):
        super().__init__(x, y, radius=5)
        self.speed = 10
        self.angle = angle
    
    def draw(self, screen):
        """Draw the shot as a small white circle."""
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        """Move the shot in the direction of its angle."""
        direction = pygame.Vector2(0, -1).rotate(self.angle)
        self.position += direction * self.speed * dt