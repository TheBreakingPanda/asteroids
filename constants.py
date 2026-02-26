
# --- Screen ---
SCREEN_WIDTH = 1280   # Window width in pixels
SCREEN_HEIGHT = 720   # Window height in pixels
LINE_WIDTH = 2        # Stroke width used when drawing all shapes

# --- Player ---
PLAYER_RADIUS = 20          # Collision radius of the player ship
PLAYER_TURN_SPEED = 300     # Rotation speed in degrees per second
PLAYER_SPEED = 200          # Movement speed in pixels per second
PLAYER_SHOOT_SPEED = 500    # Shot velocity in pixels per second
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3  # Minimum seconds between shots

# --- Asteroids ---
ASTEROID_MIN_RADIUS = 20                              # Radius of the smallest asteroid (tier 1)
ASTEROID_KINDS = 3                                    # Number of size tiers
ASTEROID_SPAWN_RATE_SECONDS = 0.8                     # Seconds between each spawn
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Radius of the largest asteroid

# --- Shots ---
SHOT_RADIUS = 5  # Collision radius of a fired shot
