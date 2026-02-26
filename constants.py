# --- Screen ---
SCREEN_WIDTH = 1280   # Window width in pixels
SCREEN_HEIGHT = 720   # Window height in pixels

# --- Player ---
PLAYER_RADIUS = 20          # Collision radius of the player ship
LINE_WIDTH = 2              # Stroke width for drawing the ship
PLAYER_TURN_SPEED = 300     # Rotation speed in degrees per second
PLAYER_SPEED = 200          # Movement speed in pixels per second
PLAYER_SHOT_COOLDOWN_SECONDS = 0.3  # Minimum seconds between shots

# --- Shots ---
SHOT_RADIUS = 5           # Collision radius of the player's shots
SHOT_SPEED = 500          # Speed of the player's shots in pixels per second

# --- Asteroids ---
ASTEROID_MIN_RADIUS = 20                            # Radius of the smallest asteroid (tier 1)
ASTEROID_KINDS = 3                                  # Number of size tiers
ASTEROID_SPAWN_RATE_SECONDS = 0.8                   # Seconds between each asteroid spawn
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Radius of the largest asteroid