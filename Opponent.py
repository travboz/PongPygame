import pygame
from pygame.locals import *

class Opponent():
    """
    Class representing an opponent paddle in the Pong game.

    Attributes:
        paddle (pygame.Rect): Rectangle representing the opponent's paddle.
        speed (int): Speed of the opponent's paddle.
        score (int): Opponent's score.
    """

    def __init__(self, paddle_info, speed):
        """
        Initializes the Opponent object.

        Args:
            paddle_info (dict): Dictionary containing paddle information (left, top, width, height).
            speed (int): Initial speed of the opponent's paddle.
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
        Get the rectangle representing the opponent's paddle.

        Returns:
            pygame.Rect: Rectangle representing the opponent's paddle.
        """
        return self.paddle

    def adjustSpeed(self, newSpeed):
        """
        Adjust the speed of the opponent's paddle.

        Args:
            newSpeed (int): The amount by which to adjust the speed.
        """
        self.speed += newSpeed

    def getSpeed(self):
        """
        Get the speed of the opponent's paddle.

        Returns:
            int: Speed of the opponent's paddle.
        """
        return self.speed

    def getScore(self):
        """
        Get the opponent's current score.

        Returns:
            int: Opponent's score.
        """
        return self.score

    def scorePoint(self):
        """Increment the opponent's score."""
        self.score += 1

    def ai_animation(self, screen_info, ball):
        """
        Move the opponent's paddle based on its speed and ensure it stays within the screen bounds.

        Args:
            screen_info (dict): Dictionary containing screen information (width, height).
            ball (Ball): The ball object used in the game.
        """
        if self.getRect().top < ball.getY():
            self.getRect().top += self.speed
        if self.getRect().bottom > ball.getX():
            self.getRect().bottom -= self.speed

        if self.getRect().top <= 0:
            self.getRect().top = 0
        if self.getRect().bottom >= screen_info["height"]:
            self.getRect().bottom = screen_info["height"]
