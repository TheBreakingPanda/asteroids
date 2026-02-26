
import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite groups — updatable runs logic, drawable renders, asteroids and shots track collisions
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign groups via class-level containers so new instances register automatically
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0  # Delta time in seconds; 0 on first frame

    # Main game loop
    while True:
        log_state()  # Periodic debug snapshot of game state

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Check every asteroid against the player for a collision
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Check every shot against every asteroid for collisions
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()  # Remove the shot from all groups
                    asteroid.kill()  # Remove the asteroid from all groups
                    break  # A shot can only hit one asteroid, so stop checkingw

        # Render: clear screen, draw all sprites, then present
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Cap at 60 FPS and convert ms → seconds for dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
