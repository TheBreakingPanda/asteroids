
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


# Represents a single shot fired by the player
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # Renders the shot as a white circle outline
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # Moves the shot along its velocity vector, scaled by delta time
    def update(self, dt):
        self.position += self.velocity * dt
