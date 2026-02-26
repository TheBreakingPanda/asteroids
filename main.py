import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player




def main():
    # initialize all imported pygame modules
    pygame.init()

    # debug printouts for verification
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create the main display surface (the game window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # clock will help us cap framerate and compute delta time
    clock = pygame.time.Clock()
    dt = 0

    # create the player centered on the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    # ---------- main game loop ----------
    while True:
        # log current state for debugging & analysis
        log_state()

        # process pending events so the window remains responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # draw frame: clear screen to black then render objects
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # limit to 60 fps and compute delta time in seconds
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
