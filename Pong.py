# 1 - Import packages
import pygame
import random
from pygame.locals import *
import sys

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # reversing the ball speeds on contact with borders
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= SCREEN_WIDTH:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, LIGHT_GRAY)
        screen.blit(number_three, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, LIGHT_GRAY)
        screen.blit(number_two, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, LIGHT_GRAY)
        screen.blit(number_one, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None

# 2 - Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FRAMES_PER_SECOND = 60
GRAY = (230, 230, 230)
LIGHT_GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
PURPLE = (255, 0, 255)

BALL_HEIGHT = 30
BALL_WIDTH = 30

CENTER_BALL = ((SCREEN_WIDTH / 2 - BALL_HEIGHT // 2), (SCREEN_HEIGHT / 2 - BALL_WIDTH // 2))
PLAYER_DIM = (10, 140)

# 3 - Initialize the world
pygame.init()
# this window is our 'Display Surface' which objects can be drawn onto
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
player = pygame.Rect(SCREEN_WIDTH - 20, (SCREEN_HEIGHT/2 - PLAYER_DIM[1]/2), PLAYER_DIM[0], PLAYER_DIM[1])
opponent = pygame.Rect(10, (SCREEN_HEIGHT/2 - PLAYER_DIM[1]/2), PLAYER_DIM[0], PLAYER_DIM[1])

ball = pygame.Rect(CENTER_BALL[0], CENTER_BALL[1], BALL_WIDTH, BALL_HEIGHT)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text variables
player_score = 0
opponent_score = 0

game_font = pygame.font.Font("freesansbold.ttf", 32)

# Score timer
score_time = True

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


    # 8 - Do any "per frame" actions
    # Game logic
    ball_animation()
    player_animation()
    opponent_ai()

    # 9 - Clear the window
    screen.fill(BLACK)

    # 10 - Draw all window elements
    pygame.draw.rect(screen, LIGHT_GRAY, player)
    pygame.draw.rect(screen, LIGHT_GRAY, opponent)
    pygame.draw.ellipse(screen, LIGHT_GRAY, ball)
    pygame.draw.aaline(screen, LIGHT_GRAY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    if score_time:
        ball_restart()


    player_text = game_font.render(f"{player_score}", False, LIGHT_GRAY)
    screen.blit(player_text, (660, 470))

    opponent_text = game_font.render(f"{opponent_score}", False, LIGHT_GRAY)
    screen.blit(opponent_text, (600, 470))

    # 11 - Update the window
    pygame.display.flip()
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
