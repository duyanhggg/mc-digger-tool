"""
Configuration file for MC Digger Tool
"""

# Minecraft Server Configuration
SERVER_HOST = "localhost"  # Server address (IP or domain)
SERVER_PORT = 25565        # Default Minecraft port
USERNAME = "YourUsername"  # Your Minecraft username
PASSWORD = None            # Password (None for offline mode)
OFFLINE_MODE = True        # Set to True for single player / offline servers

# Digger Configuration
DIG_WIDTH = 10             # Width of the area to dig (X axis)
DIG_LENGTH = 10            # Length of the area to dig (Z axis)
DIG_DEPTH = 5              # How deep to dig (Y axis, downwards)
DIG_INTERVAL = 5           # Blocks between each dig pass

# Tool Configuration
TOOLS = {
    "stone": "wooden_pickaxe",
    "cobblestone": "wooden_pickaxe",
    "dirt": "wooden_shovel",
    "grass": "wooden_shovel",
    "sand": "wooden_shovel",
    "gravel": "wooden_shovel",
    "wood": "wooden_axe",
    "oak_log": "wooden_axe",
    "spruce_log": "wooden_axe",
    "birch_log": "wooden_axe",
}

# Logging
DEBUG_MODE = True
LOG_FILE = "digger.log"