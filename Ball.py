import pygame
from pygame.locals import *

class Ball():
    def __init__(self, ball_info):
        self.ball = pygame.Rect(
            ball_info["screen_center_x"],
            ball_info["screen_center_y"],
            ball_info["width_height"],
            ball_info["width_height"]
        )

    def getRect(self):
        return self.ball

    def getX(self):
        return self.ball.x

    def getY(self):
        return self.ball.y