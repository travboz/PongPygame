import pygame
import random
from pygame.locals import *
import time  # Import the time module

class Ball():
    def __init__(self, ball_info, speed_x, speed_y):
        self.ball = pygame.Rect(
            ball_info["screen_center_x"],
            ball_info["screen_center_y"],
            ball_info["width_height"],
            ball_info["width_height"]
        )

        self.ball_info = ball_info

        self.speed_x = speed_x
        self.speed_y = speed_y

        self.wait_time = None  # Initialize wait time

    def getRect(self):
        return self.ball

    def getX(self):
        return self.getRect().x

    def getY(self):
        return self.getRect().y

    def reset_pos(self, screen_info):
        self.getRect().centerx = screen_info["width"] // 2
        self.getRect().centery = screen_info["height"] // 2
        self.wait_time = time.time() + 2  # Set wait time to current time + 2 seconds
        self.speed_x = 0  # Stop the ball
        self.speed_y = 0

    def getXSpeed(self):
        return self.speed_x

    def getYSpeed(self):
        return self.speed_y

    def setXSpeed(self, speed):
        self.speed_x = speed

    def setYSpeed(self, speed):
        self.speed_y = speed

    def adjustXSpeed(self, adj):
        self.speed_x *= adj

    def adjustYSpeed(self, adj):
        self.speed_y *= adj

    def ball_animation(self, player, opponent, screen_info):

        # If it's time to move again
        if self.wait_time is not None and time.time() >= self.wait_time:
            # Pick a random direction
            self.speed_x = random.choice((7, -7))
            self.speed_y = random.choice((7, -7))
            self.wait_time = None  # Reset wait time

        self.getRect().x += self.getXSpeed()
        self.getRect().y += self.getYSpeed()

        # Reset position if out of bounds left or right
        if self.getRect().left <= 0 or self.getRect().right >= screen_info["width"]:
            self.reset_pos(screen_info)

        # reversing the ball speeds on contact with borders
        if self.ball.top <= 0 or self.ball.bottom >= screen_info["height"]:
            self.adjustYSpeed(-1)

        if self.ball.left <= 0:
            player.scorePoint()

        if self.ball.right >= screen_info["width"]:
            opponent.scorePoint()

        if self.ball.colliderect(player.getRect()) and self.getXSpeed() > 0:
            if abs(self.ball.right - player.getRect().left) < 10:
                self.adjustXSpeed(-1)

            elif abs(self.ball.bottom - player.getRect().top) < 10 and self.getYSpeed() > 0:
                self.adjustYSpeed(-1)
            elif abs(self.ball.top - player.getRect().bottom) < 10 and self.getYSpeed() < 0:
                self.adjustYSpeed(-1)

        if self.ball.colliderect(opponent.getRect()) and self.getXSpeed() < 0:
            if abs(self.ball.left - opponent.getRect().right) < 10:
                self.adjustXSpeed(-1)
            elif abs(self.ball.bottom - opponent.getRect().top) < 10 and self.getYSpeed() > 0:
                self.adjustYSpeed(-1)
            elif abs(self.ball.top - opponent.getRect().bottom) < 10 and self.getYSpeed() < 0:
                self.adjustYSpeed(-1)