import pygame
from pygame.locals import *

class Opponent():
    def __init__(self, paddle_info, speed):
        self.paddle = pygame.Rect(
            paddle_info["left"],
            paddle_info["top"],
            paddle_info["width"],
            paddle_info["height"],
        )
        self.speed = speed
        self.score = 0

    def getRect(self):
        return self.paddle

    def adjustSpeed(self, newSpeed):
        self.speed += newSpeed

    def getSpeed(self):
        return self.speed

    def getScore(self):
        return self.score

    def scorePoint(self):
        self.score += 1

    def ai_animation(self, screen_info, ball):
        if self.getRect().top < ball.getY():
            self.getRect().top += self.speed
        if self.getRect().bottom > ball.getX():
            self.getRect().bottom -= self.speed

        if self.getRect().top <= 0:
            self.getRect().top = 0
        if self.getRect().bottom >= screen_info["height"]:
            self.getRect().bottom = screen_info["height"]

