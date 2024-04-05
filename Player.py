import pygame
from pygame.locals import *

class Player():
    def __init__(self, paddle, speed):
        self.paddle = paddle
        self.speed = speed

    def getRect(self):
        return self.paddle.getRect()

    def adjustSpeed(self, newSpeed):
        self.speed += newSpeed

    def player_animation(self, screen_info):
        self.getRect().y += self.speed
        if self.getRect().top <= 0:
            self.getRect().top = 0
        if self.getRect().bottom >= screen_info["height"]:
            self.getRect().bottom = screen_info["height"]
