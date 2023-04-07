"""Pong Game with Pygame."""
import pygame


class Paddle:
    """Paddle class."""

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 10,
        height: int = 50,
        speed: int = 10,
        color: tuple = (255, 255, 255),
    ):
        """Initialize paddle."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.lives = 3

    def draw(self, screen: pygame.Surface):
        """Draw paddle."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction: int):
        """Move paddle."""
        self.y += direction * self.speed

    def check_bounce(self, height: int):
        """Check if paddle bounces."""
        if self.y < 0:
            self.y = 0
        if self.y > height - self.height:
            self.y = height - self.height

    def kill(self):
        """Kill paddle."""
        self.lives -= 1
