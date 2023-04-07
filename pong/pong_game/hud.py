"""Pong Game with Pygame."""
import pygame


class Hud:
    """Hud class."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 200,
        height: int = 100,
        font: pygame.font.Font = None,
        color: tuple = (255, 255, 255),
    ):
        """Initialize hud."""
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        if font is None:
            self.font = pygame.font.SysFont("Arial", 20)
        self.color = color

    def _draw_lives(self, screen: pygame.Surface, lives_left: int, lives_right: int):
        """Draw Lives"""
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height),
            1,
        )
        pygame.draw.rect(
            screen,
            self.color,
            (self.x + self.width, self.y, self.width, self.height),
            1,
        )
        # add text for lives
        text = self.font.render(f"Lives: {lives_left}", True, self.color)
        screen.blit(text, (self.x + 10, self.y + 10))
        text = self.font.render(f"Lives: {lives_right}", True, self.color)
        screen.blit(text, (self.x + self.width + 10, self.y + 10))

    def _draw_winner(self, screen: pygame.Surface, winner: int):
        """Draw winner."""
        if winner == 1:
            text = self.font.render("Player 1 wins!", True, self.color)
            screen.blit(text, (self.x + self.width // 2 - 50, self.y + 10))
        elif winner == 2:
            text = self.font.render("Player 2 wins!", True, self.color)
            screen.blit(text, (self.x + self.width // 2 - 50, self.y + 10))

    def draw(self, screen: pygame.Surface, lives_left: int, lives_right: int):
        """Draw hud."""
        self._draw_lives(screen, lives_left, lives_right)
        if lives_left == 0 or lives_right == 0:
            self._draw_winner(screen, 1 if lives_left == 0 else 2)
