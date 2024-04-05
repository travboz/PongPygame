import pygame
from pygame.locals import *

class Opponent():
    def __init__(self, paddle, speed):
        self.paddle = paddle
        self.speed = speed

    def getRect(self):
        return self.paddle.getRect()

    def adjustSpeed(self, newSpeed):
        self.speed += newSpeed

    def ai_animation(self, screen_info, ball):
        if self.getRect().top < ball.getY():
            self.getRect().top += self.speed
        if self.getRect().bottom > ball.getX():
            self.getRect().bottom -= self.speed

        if self.getRect().top <= 0:
            self.getRect().top = 0
        if self.getRect().bottom >= screen_info["height"]:
            self.getRect().bottom = screen_info["height"]

