"""
MC Digger Tool - Automatic Mining Script for Minecraft
Supports both Single Player and Server connections
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import List, Dict, Tuple
import config

# Setup logging
logging.basicConfig(
    level=logging.DEBUG if config.DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MinecraftDigger:
    """Main class for automated mining in Minecraft"""
    
    def __init__(self):
        self.width = config.DIG_WIDTH
        self.length = config.DIG_LENGTH
        self.depth = config.DIG_DEPTH
        self.interval = config.DIG_INTERVAL
        self.current_tool = None
        self.blocks_dug = 0
        self.is_running = False
        
        logger.info("MC Digger Tool initialized")
        logger.info(f"Configuration: {self.width}x{self.length}x{self.depth}")
    
    def get_user_input(self) -> Tuple[int, int, int, int]:
        """Get mining area dimensions from user"""
        print("\n" + "="*50)
        print("MC DIGGER TOOL - Configuration")
        print("="*50)
        
        try:
            width = int(input(f"Width (X axis) [default: {self.width}]: ") or self.width)
            length = int(input(f"Length (Z axis) [default: {self.length}]: ") or self.length)
            depth = int(input(f"Depth (Y axis) [default: {self.depth}]: ") or self.depth)
            interval = int(input(f"Dig interval (blocks) [default: {self.interval}]: ") or self.interval)
            
            if width <= 0 or length <= 0 or depth <= 0 or interval <= 0:
                raise ValueError("All values must be positive")
            
            self.width = width
            self.length = length
            self.depth = depth
            self.interval = interval
            
            logger.info(f"User configured area: {width}x{length}x{depth}, interval: {interval}")
            return width, length, depth, interval
            
        except ValueError as e:
            logger.error(f"Invalid input: {e}")
            print(f"❌ Invalid input: {e}")
            return self.get_user_input()
    
    def get_appropriate_tool(self, block_type: str) -> str:
        """Get the most appropriate tool for the block type"""
        block_type = block_type.lower()
        
        # Check exact match first
        if block_type in config.TOOLS:
            return config.TOOLS[block_type]
        
        # Check partial match
        for key, tool in config.TOOLS.items():
            if key in block_type:
                return tool
        
        # Default to pickaxe
        return "wooden_pickaxe"
    
    def change_tool(self, new_tool: str) -> bool:
        """Change to appropriate tool"""
        if new_tool == self.current_tool:
            return True
        
        self.current_tool = new_tool
        logger.info(f"Switched to: {new_tool}")
        print(f"🔧 Tool changed to: {new_tool}")
        return True
    
    def dig_block(self, x: int, y: int, z: int) -> bool:
        """Simulate digging a block at given coordinates"""
        try:
            # In a real implementation, this would send dig packets to the server
            # For now, we simulate the action
            self.blocks_dug += 1
            return True
        except Exception as e:
            logger.error(f"Failed to dig block at ({x}, {y}, {z}): {e}")
            return False
    
    def dig_area(self) -> None:
        """Main digging loop for the specified area"""
        print("\n" + "="*50)
        print("STARTING DIG OPERATION")
        print("="*50)
        
        self.is_running = True
        start_time = datetime.now()
        
        try:
            current_y = 0
            
            while current_y < self.depth and self.is_running:
                print(f"\n📍 Digging at depth: {current_y + 1}/{self.depth}")
                
                for x in range(0, self.width, self.interval):
                    for z in range(0, self.length, self.interval):
                        if not self.is_running:
                            break
                        
                        # Simulate block detection and tool selection
                        block_type = f"stone_{current_y}"  # In real implementation, detect block
                        tool_needed = self.get_appropriate_tool(block_type)
                        
                        if self.change_tool(tool_needed):
                            if self.dig_block(x, current_y, z):
                                print(f"✓ Dug block at ({x}, {current_y}, {z})")
                
                current_y += 1
            
            elapsed_time = datetime.now() - start_time
            print("\n" + "="*50)
            print("DIG OPERATION COMPLETED")
            print("="*50)
            print(f"✅ Total blocks dug: {self.blocks_dug}")
            print(f"⏱️  Time taken: {elapsed_time}")
            logger.info(f"Dig operation completed. Blocks dug: {self.blocks_dug}, Time: {elapsed_time}")
            
        except KeyboardInterrupt:
            print("\n⛔ Mining operation stopped by user")
            logger.info(f"Mining stopped by user. Blocks dug: {self.blocks_dug}")
        except Exception as e:
            logger.error(f"Error during dig operation: {e}")
            print(f"❌ Error: {e}")
    
    def display_status(self) -> None:
        """Display current status"""
        print("\n" + "="*50)
        print("STATUS")
        print("="*50)
        print(f"Current tool: {self.current_tool or 'None'}")
        print(f"Blocks dug: {self.blocks_dug}")
        print(f"Area size: {self.width}x{self.length}x{self.depth}")
        print(f"Dig interval: {self.interval}")
    
    def run_interactive(self) -> None:
        """Run in interactive mode"""
        print("\n🎮 MC DIGGER TOOL - Interactive Mode")
        print("="*50)
        
        # Get configuration from user
        self.get_user_input()
        
        # Confirm settings
        print("\n📋 Summary:")
        print(f"  Area: {self.width}x{self.length}x{self.depth} blocks")
        print(f"  Interval: {self.interval} blocks")
        
        confirm = input("\n▶️  Start mining? (y/n): ").lower()
        if confirm == 'y':
            self.dig_area()
        else:
            print("❌ Cancelled")


def main():
    """Main entry point"""
    try:
        digger = MinecraftDigger()
        digger.run_interactive()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        logger.info("Application terminated by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()