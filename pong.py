import pygame
import pygame.freetype
import sys
import random
from time import sleep

clock = pygame.time.Clock()
pygame.init()

screen_width = 1280
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Initial Scores
player_1_score = 0
player_2_score = 0

# Text Font
font = pygame.freetype.Font('OpenSans-Bold.ttf', 32)

def boundaries():
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height
    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height


def ball_movement():
    global ball_speed_x, ball_speed_y, player_1_score, player_2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= - 1
    if ball.left < 0:
        sleep(3)
        ball_restart()
        player_2_score += 1

    if ball.right >= screen_width:
        sleep(3)
        ball_restart()
        player_1_score += 1

    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

"""
Game Objects
"""

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player_1 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
player_1_speed = 0

player_2 = pygame.Rect(1260, screen_height / 2 - 70, 10, 140)
player_2_speed = 0
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Controls
        if event.type == pygame.KEYDOWN:
            # Player 1
            if event.key == pygame.K_s:
                player_1_speed = 7
            if event.key == pygame.K_w:
                player_1_speed = - 7

            # Player 2
            if event.key == pygame.K_DOWN:
                player_2_speed = 7
            if event.key == pygame.K_UP:
                player_2_speed = - 7
        if event.type == pygame.KEYUP:
            # Player 1
            if event.key == pygame.K_s:
                player_1_speed = 0
            if event.key == pygame.K_w:
                player_1_speed = 0

            # Player 2
            if event.key == pygame.K_DOWN:
                player_2_speed = 0
            if event.key == pygame.K_UP:
                player_2_speed = 0

    # Draws Game Objects
    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player_1)
    pygame.draw.rect(screen, light_grey, player_2)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Player/ Ball movement
    player_1.y += player_1_speed
    player_2.y += player_2_speed

    ball_movement()
    boundaries()
    # Score Display
    font.render_to(screen, (screen_width/2 - 25, screen_height/2), f'{player_1_score}  {player_2_score}', 'grey')

    # Update game window
    pygame.display.flip()
    clock.tick(60)
