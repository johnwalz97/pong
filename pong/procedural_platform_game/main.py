"""2d Platform Game with Procedurally Generated Levels, Platforms and Enemies."""
import pygame
import typer


class Game:
    """Game Class."""
    
    def __init__(self, width: int, height: int, fps: int):
        """Initialize game."""
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self):
        """Draw game."""
        self.screen.blit(self.font.render("Hello World", True, (255, 255, 255)), (100, 100))

    def run(self):
        """Run game."""
        while True:
            self.clock.tick(self.fps)
            self.screen.fill((0, 0, 0))

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


def play(
    width: int = typer.Option(
        default=800, help="Width of the screen.", show_default=True
    ),
    height: int = typer.Option(
        default=600, help="Height of the screen.", show_default=True
    ),
    fps: int = typer.Option(default=60, help="Frames per second.", show_default=True),
):
    """Platformer Game Function"""
    game = Game(width, height, fps)
    game.run()
