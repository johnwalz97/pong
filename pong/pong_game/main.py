"""Pong Game with Pygame."""
import pygame
import typer
from pygame.math import Vector2

from .ball import Ball
from .hud import Hud
from .paddle import Paddle
from .paddle_controller import AIPaddleControl, KeyboardPaddleControl, GamePadControl


pygame.font.init()


class Pong:
    """Pong Game."""

    def __init__(
        self, width: int, height: int, ball_speed: int, paddle_speed: int, fps: int
    ):
        """Initialize pong."""
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.fps = fps
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", 20)

        self.ball_speed = ball_speed
        self.paddle_speed = paddle_speed
        self._reset_self()

    def _reset_self(self):
        """Reset self."""
        self.winner = 0

        self.ball = Ball(
            x=self.width // 2,
            y=self.height // 2,
            speed=self.ball_speed,
            direction=Vector2(1, 1),
        )
        self.paddle_left = Paddle(
            x=0, y=self.height // 2, width=5, height=100, speed=self.paddle_speed
        )
        self.paddle_right = Paddle(
            x=self.width - 5,
            y=self.height // 2,
            width=5,
            height=100,
            speed=self.paddle_speed,
        )
        self.paddle_left_control = GamePadControl()
        self.paddle_right_control = AIPaddleControl(self.ball)
        self.hud = Hud(
            x=self.width // 2 - 200,
            y=0,
            width=200,
            height=50,
        )

    def _reset_ball(self):
        """Reset ball."""
        self.ball.x = self.width // 2
        self.ball.y = self.height // 2
        self.ball.direction = self.ball.direction.rotate(180)
        self.ball.speed = self.ball_speed

    def draw(self):
        """Draw pong."""
        self.paddle_left.draw(self.screen)
        self.paddle_right.draw(self.screen)
        self.ball.draw(self.screen)
        self.hud.draw(self.screen, self.paddle_left.lives, self.paddle_right.lives)

        pygame.display.update()

    def check_win(self, lives_left: int, lives_right: int):
        """Check if someone wins."""
        if lives_left == 0:
            self.winner = -1
        if lives_right == 0:
            self.winner = 1
        return self.winner != 0

    def run(self):
        """Run pong."""
        while True:
            self.clock.tick(self.fps)
            self.screen.fill((0, 0, 0))

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if self.winner or self.check_win(self.paddle_left.lives, self.paddle_right.lives):
                continue

            self.paddle_left_control.move(self.paddle_left)
            self.paddle_right_control.move(self.paddle_right)

            self.ball.move()

            if side_out := self.ball.check_out(self.width):
                if side_out < 0:
                    self.paddle_left.kill()
                else:
                    self.paddle_right.kill()
                self._reset_ball()

            self.ball.check_bounce(self.height)
            self.ball.check_collision(self.paddle_left)
            self.ball.check_collision(self.paddle_right)


def play(
    width: int = typer.Option(
        default=800, help="Width of the screen.", show_default=True
    ),
    height: int = typer.Option(
        default=600, help="Height of the screen.", show_default=True
    ),
    ball_speed: int = typer.Option(
        default=4, help="Speed of the ball.", show_default=True
    ),
    paddle_speed: int = typer.Option(
        default=4, help="Speed of the paddle.", show_default=True
    ),
    fps: int = typer.Option(default=60, help="Frames per second.", show_default=True),
):
    """Play pong."""
    pong = Pong(width, height, ball_speed, paddle_speed, fps)
    pong.run()
