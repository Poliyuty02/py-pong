"""
PONG GAME - Workshop Edition
A classic arcade game built with Pygame.
This code is intentionally left with customization opportunities for students.
"""

# Import the required libraries
import pygame
import sys

# Initialize Pygame (this starts all the game modules)
pygame.init()

# --- Game Constants (Things that rarely change) ---
# TODO: STUDENT CHALLENGE 1 - Change the game window size!
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors in RGB format (Red, Green, Blue)
# TODO: STUDENT CHALLENGE 2 - Change the colors below to your favorites!
WHITE = (255, 255, 255)      # Try (0, 255, 0) for neon green
BLACK = (0, 0, 0)            # Try (255, 0, 0) for red background
BALL_COLOR = (255, 255, 255) # Try (255, 255, 0) for yellow ball

# Game Settings
FPS = 60  # Frames per second (how smooth the game runs)
WINNING_SCORE = 5  # TODO: STUDENT CHALLENGE 3 - Change this to 3 or 10!

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG - Your Name Here")  # TODO: Add your name!

# Clock controls the game speed
clock = pygame.time.Clock()


class Paddle:
    """Represents the left and right paddles in the game."""
    
    def __init__(self, x, y, width, height, speed):
        """
        Initialize a paddle.
        :param x: X-coordinate (left/right position)
        :param y: Y-coordinate (top/bottom position)
        :param width: How wide the paddle is
        :param height: How tall the paddle is
        :param speed: How fast the paddle moves
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        # TODO: STUDENT CHALLENGE 4 - Try changing the paddle color!
        self.color = WHITE
        
    def move(self, up_key, down_key):
        """
        Move the paddle up or down based on key presses.
        :param up_key: The key that moves the paddle up (e.g., pygame.K_UP)
        :param down_key: The key that moves the paddle down
        """
        keys = pygame.key.get_pressed()
        
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
            
    def draw(self):
        """Draw the paddle on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    """Represents the ball that bounces around the screen."""
    
    def __init__(self, x, y, radius, speed_x, speed_y):
        """
        Initialize the ball.
        :param x: Starting X position
        :param y: Starting Y position
        :param radius: Size of the ball
        :param speed_x: Horizontal speed (negative = left, positive = right)
        :param speed_y: Vertical speed
        """
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = BALL_COLOR
        # TODO: STUDENT CHALLENGE 5 - Change the starting speed (try 5, 4 or 7, 6)
        
    def move(self):
        """Update ball position based on its speed."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
    def draw(self):
        """Draw the ball on the screen."""
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        
    def reset(self):
        """Reset ball to the center after a point is scored."""
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # TODO: STUDENT CHALLENGE 6 - Make the ball go in a random direction on reset!
        # Hint: You can randomize self.speed_x and self.speed_y
        self.speed_x = abs(self.speed_x)  # Make it go right by default
        # Flip a coin to decide if it goes up or down
        if self.speed_y < 0:
            self.speed_y = -abs(self.speed_y)


class GameManager:
    """Controls the game logic, scoring, and win conditions."""
    
    def __init__(self):
        """Initialize the game objects and scores."""
        # Create paddles
        # Left paddle (x=20, centered vertically)
        self.left_paddle = Paddle(20, SCREEN_HEIGHT // 2 - 60, 15, 120, 7)
        # Right paddle (x=SCREEN_WIDTH-35)
        self.right_paddle = Paddle(SCREEN_WIDTH - 35, SCREEN_HEIGHT // 2 - 60, 15, 120, 7)
        
        # Create ball
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 8, 4, 4)
        
        # Scores
        self.left_score = 0
        self.right_score = 0
        
        # Font for displaying text
        self.font = pygame.font.Font(None, 74)  # None = default font, size 74
        
        # Game state
        self.winner = None  # Will be "left" or "right" when game ends
        
    def handle_collisions(self):
        """Check and respond to ball collisions with walls and paddles."""
        # Wall collision (top and bottom)
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= SCREEN_HEIGHT:
            self.ball.speed_y *= -1  # Reverse vertical direction
            
        # Paddle collisions
        if self.ball.rect.colliderect(self.left_paddle.rect) or \
           self.ball.rect.colliderect(self.right_paddle.rect):
            self.ball.speed_x *= -1  # Reverse horizontal direction
            # TODO: STUDENT CHALLENGE 7 - Add a sound effect here!
            # Hint: pygame.mixer.Sound('beep.wav').play()
            
    def update_score(self):
        """Update scores if ball goes past paddles and check for winner."""
        # Ball passed left paddle (right player scores)
        if self.ball.rect.left <= 0:
            self.right_score += 1
            self.ball.reset()
            
        # Ball passed right paddle (left player scores)
        if self.ball.rect.right >= SCREEN_WIDTH:
            self.left_score += 1
            self.ball.reset()
            
        # Check for winner
        if self.left_score >= WINNING_SCORE:
            self.winner = "Left Player"
        elif self.right_score >= WINNING_SCORE:
            self.winner = "Right Player"
            
    def draw_scores(self):
        """Display current scores on the screen."""
        left_text = self.font.render(str(self.left_score), True, WHITE)
        right_text = self.font.render(str(self.right_score), True, WHITE)
        
        # Position scores (left score top-left, right score top-right)
        screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
        screen.blit(right_text, (SCREEN_WIDTH * 3 // 4, 20))
        
    def draw_winner(self):
        """Display winner message and wait for spacebar to reset."""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Winner text
        winner_text = self.font.render(f"{self.winner} Wins!", True, WHITE)
        text_rect = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(winner_text, text_rect)
        
        # Instruction text
        small_font = pygame.font.Font(None, 36)
        restart_text = small_font.render("Press SPACE to play again or ESC to quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
        
        # Wait for player input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Reset the game
                        self.__init__()
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
    def run(self):
        """Main game loop - runs until the player quits."""
        running = True
        
        while running:
            # Handle events (like quitting)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            # Check if game is over
            if self.winner:
                self.draw_winner()
                continue  # Skip the rest of the loop until game resets
                
            # Move objects
            self.left_paddle.move(pygame.K_w, pygame.K_s)  # W = up, S = down
            self.right_paddle.move(pygame.K_UP, pygame.K_DOWN)  # Arrow keys
            self.ball.move()
            
            # Check collisions and scoring
            self.handle_collisions()
            self.update_score()
            
            # Draw everything
            screen.fill(BLACK)  # Clear screen
            self.left_paddle.draw()
            self.right_paddle.draw()
            self.ball.draw()
            self.draw_scores()
            
            # Draw center line (optional, just for looks)
            pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            
            # Update display
            pygame.display.flip()
            
            # Control game speed
            clock.tick(FPS)
            
        pygame.quit()
        sys.exit()


# --- Run the game! ---
if __name__ == "__main__":
    game = GameManager()
    game.run()
