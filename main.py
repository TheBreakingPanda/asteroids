import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from shot import Shot


def main():
    """Initialize the game, run the main loop, and handle shutdown."""

    pygame.init()

    # Debug: confirm pygame version and screen dimensions on startup
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0  # Delta time in seconds; 0 on first frame

    # Sprite groups — updatable runs logic, drawable renders, asteroids tracks collisions
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign groups via class-level containers so new instances register automatically
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    # Create the asteroid field (registers itself into the updatable group)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # ---------- Main Game Loop ----------
    while True:
        log_state()  # Debug snapshot of current game state

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Render: clear → update logic → draw sprites → present
        screen.fill("black")
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Player hit an asteroid! Game over!.")
                sys.exit()

        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)
        pygame.display.flip()
    

        dt = clock.tick(60) / 1000  # Cap at 60 FPS; convert ms → seconds


if __name__ == "__main__":
    main()