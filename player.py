import pygame
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    """Player-controlled ship represented as a triangle."""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0       # Current heading in degrees; 0 points down the +Y axis
        self.shoot_timer = 0    # Counts down to zero; shooting is blocked while positive

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

    def update(self, dt):
        """Poll input and apply movement, rotation, and shooting each frame."""
        self.shoot_timer -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        """Rotate the ship by PLAYER_TURN_SPEED scaled by dt. Negative dt rotates left."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Thrust along the current heading. Negative dt moves in reverse."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        """Fire a shot from the ship's nose if the cooldown has elapsed."""
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED