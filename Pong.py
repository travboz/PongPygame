# 1 - Import packages
import pygame
import random
from pygame.locals import *
import sys

from Ball import *
from Player import *
from Opponent import *

# 2 - Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FRAMES_PER_SECOND = 60

# Colours
GRAY = (230, 230, 230)
LIGHT_GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Asset values
BALL_WIDTH_HEIGHT = 30
PLAYER_DEFAULT_SPEED = 0
OPP_DEFAULT_SPEED = 7

PADDLE_DIMENSIONS = {
    "width" : 10,
    "height" : 140
}

screen_info = {
    "width" : SCREEN_WIDTH,
    "height" : SCREEN_HEIGHT,
    "fps" : FRAMES_PER_SECOND,
}

# 3 - Initialize the world
pygame.init()
# this window is our 'Display Surface' which objects can be drawn onto
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

# 4 - Load assets: image(s), sound(s),  etc.
player_info = {
    "left" : SCREEN_WIDTH - 20,
    "top" : (SCREEN_HEIGHT / 2 - PADDLE_DIMENSIONS["height"] / 2),
    "width" : PADDLE_DIMENSIONS["width"],
    "height" : PADDLE_DIMENSIONS["height"],
}

opponent_info = {
    "left" : 10,
    "top" : (SCREEN_HEIGHT / 2 - PADDLE_DIMENSIONS["height"] / 2),
    "width" : PADDLE_DIMENSIONS["width"],
    "height" : PADDLE_DIMENSIONS["height"],
}

ball_info = {
    "screen_center_x" : (SCREEN_WIDTH / 2 - BALL_WIDTH_HEIGHT // 2),
    "screen_center_y" : (SCREEN_HEIGHT / 2 - BALL_WIDTH_HEIGHT // 2),
    "width_height" : 30,
}

# 5 - Initialize variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

player = Player(
    player_info,
    PLAYER_DEFAULT_SPEED
)
opponent = Opponent(
    opponent_info,
    OPP_DEFAULT_SPEED
)

ball = Ball(
    ball_info,
    ball_speed_x,
    ball_speed_y)

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
                player.adjustSpeed(7)
            if event.key == pygame.K_UP:
                player.adjustSpeed(-7)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.adjustSpeed(-7)
            if event.key == pygame.K_UP:
                player.adjustSpeed(7)

    # 8 - Do any "per frame" actions
    # Game logic
    ball.ball_animation(player, opponent, screen_info)
    player.player_animation(screen_info)
    opponent.ai_animation(screen_info, ball)

    # 9 - Clear the window
    screen.fill(BLACK)

    # 10 - Draw all window elements
    pygame.draw.rect(screen, LIGHT_GRAY, player.getRect())
    pygame.draw.rect(screen, LIGHT_GRAY, opponent.getRect())
    pygame.draw.ellipse(screen, LIGHT_GRAY, ball.getRect())
    pygame.draw.aaline(screen, LIGHT_GRAY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # 11 - Update the window
    pygame.display.flip()
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
