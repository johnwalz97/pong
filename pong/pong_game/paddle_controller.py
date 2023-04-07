"""Pong Game with Pygame."""
from abc import ABC, abstractmethod

import pygame

from .ball import Ball
from .paddle import Paddle


class PaddleControl(ABC):
    """Abstract class for paddle control classes.

    We want to have different control classes that can be used to control the paddle such as
    keyboard control, ai control, gamepad control etc.
    """

    @abstractmethod
    def move(self, paddle: Paddle):
        """Move paddle."""
        pass


class KeyboardPaddleControl(PaddleControl):
    """Keyboard paddle control."""

    def move(self, paddle: Paddle):
        """Move paddle."""
        if pygame.key.get_pressed()[pygame.K_UP]:
            paddle.move(-1)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            paddle.move(1)


class AIPaddleControl(PaddleControl):
    """AI paddle control."""

    def __init__(self, ball: Ball):
        """Initialize AI paddle control."""
        self.ball = ball

    def move(self, paddle: Paddle):
        """Move paddle."""
        if self.ball.y < paddle.y:
            paddle.move(-1)
        if self.ball.y > paddle.y:
            paddle.move(1)


class GamePadControl(PaddleControl):
    """Gamepad paddle control."""

    def __init__(self):
        """Initialize gamepad paddle control."""
        pygame.joystick.init()
        self.j = pygame.joystick.Joystick(0)
        self.j.init()

    def move(self, paddle: Paddle):
        """Move paddle."""
        if self.j.get_axis(1) < 0:
            paddle.move(-1)
        if self.j.get_axis(1) > 0:
            paddle.move(1)
