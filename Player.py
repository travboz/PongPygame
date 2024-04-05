import pygame
from pygame.locals import *

class Player():
    """
    Class representing a player paddle in the Pong game.

    Attributes:
        paddle (pygame.Rect): Rectangle representing the player's paddle.
        speed (int): Speed of the player's paddle.
        score (int): Player's score.
    """

    def __init__(self, paddle_info, speed):
        """
        Initializes the Player object.

        Args:
            paddle_info (dict): Dictionary containing paddle information (left, top, width, height).
            speed (int): Initial speed of the player's paddle.
        """
        self.paddle = pygame.Rect(
            paddle_info["left"],
            paddle_info["top"],
            paddle_info["width"],
            paddle_info["height"],
        )
        self.speed = speed
        self.score = 0

    def getRect(self):
        """
        Get the rectangle representing the player's paddle.

        Returns:
            pygame.Rect: Rectangle representing the player's paddle.
        """
        return self.paddle

    def adjustSpeed(self, newSpeed):
        """
        Adjust the speed of the player's paddle.

        Args:
            newSpeed (int): The amount by which to adjust the speed.
        """
        self.speed += newSpeed

    def getScore(self):
        """
        Get the player's current score.

        Returns:
            int: Player's score.
        """
        return self.score

    def scorePoint(self):
        """Increment the player's score."""
        self.score += 1

    def player_animation(self, screen_info):
        """
        Move the player's paddle based on its speed and ensure it stays within the screen bounds.

        Args:
            screen_info (dict): Dictionary containing screen information (width, height).
        """
        self.getRect().y += self.speed
        if self.getRect().top <= 0:
            self.getRect().top = 0
        if self.getRect().bottom >= screen_info["height"]:
            self.getRect().bottom = screen_info["height"]
