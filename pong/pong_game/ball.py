"""Pong Game with Pygame."""
import pygame
from pygame.math import Vector2

from .paddle import Paddle


class Ball:
    """Ball class."""

    def __init__(
        self,
        x: int,
        y: int,
        speed: int,
        direction: Vector2,
        color: tuple = (255, 255, 255),
    ):
        """Initialize ball."""
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.color = color

    def move(self):
        """Move ball."""
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed

    def draw(self, screen: pygame.Surface):
        """Draw ball."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

    def bounce(self):
        """Bounce ball."""
        self.direction.x *= -1
        self.direction.y *= -1

    def check_bounce(self, height: int):
        """Check if ball bounces off the top or bottom."""
        if self.y < 0 or self.y > height:
            self.direction.y *= -1

    def check_collision(self, paddle: Paddle):
        """Check if ball collides with paddle."""
        if self.x + 5 > paddle.x and self.x - 5 < paddle.x + paddle.width:
            if self.y + 5 > paddle.y and self.y - 5 < paddle.y + paddle.height:
                self.bounce()

    def check_out(self, game_width: int):
        """Check if ball is out of bounds and if it is which side its out of bounds."""
        if self.x < 0:
            return -1
        if self.x > game_width:
            return 1
        return 0
