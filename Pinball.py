import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pinball Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the ball
ball_radius = 10
ball_x = random.randint(ball_radius, width - ball_radius)
ball_y = height // 2
ball_speed_x = random.randint(2, 4)
ball_speed_y = random.randint(2, 4)

# Set up the paddles
paddle_width = 100
paddle_height = 10
paddle_x = width // 2 - paddle_width // 2
paddle_y = height - 2 * paddle_height

# Set up game variables
score = 0
lives = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Frame rate: 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the walls
    if ball_x <= ball_radius or ball_x >= width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= ball_radius:
        ball_speed_y = -ball_speed_y

    # Check if the ball hits the paddle
    if ball_y >= paddle_y - ball_radius and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y
        score += 1

    # Check if the ball falls off the screen
    if ball_y >= height - ball_radius:
        lives -= 1
        ball_x = random.randint(ball_radius, width - ball_radius)
        ball_y = height // 2
        ball_speed_x = random.randint(2, 4)
        ball_speed_y = random.randint(2, 4)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Draw the paddle
    pygame.draw.rect(screen, RED, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the score and lives
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(score_text, (10, 10))
    lives_text = font.render("Lives: " + str(lives), True, GREEN)
    screen.blit(lives_text, (width - lives_text.get_width() - 10, 10))

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
