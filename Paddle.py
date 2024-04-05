import pygame
from pygame.locals import *

class Paddle():
    def __init__(self, paddle_info):
        self.paddle = pygame.Rect(
            paddle_info["left"],
            paddle_info["top"],
            paddle_info["width"],
            paddle_info["height"],
        )

    def getRect(self):
        return self.paddle