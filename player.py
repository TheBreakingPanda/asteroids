import pygame

import circleshape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(circleshape.CircleShape):
    """Player-controlled ship represented as a triangle."""

    rotation = 0  # Current heading in degrees; 0 points down the +Y axis

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

    def triangle(self):
        """Return the three vertices of the ship triangle based on current position and rotation."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius          # Nose
        b = self.position - forward * self.radius - right  # Rear left
        c = self.position - forward * self.radius + right  # Rear right
        return [a, b, c]

    def draw(self, screen):
        """Render the ship as a white triangle outline."""
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, direction, dt):
        """Rotate the ship. direction: -1 = left, +1 = right."""
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Thrust along the current heading. Negative dt moves in reverse."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        """Poll input and apply movement each frame."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)