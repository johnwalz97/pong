"""entrypoint for pong and other simple games"""
# use typer to create a simple cli that can launch different games
import typer

from .pong_game.main import play as play_pong
from .procedural_platform_game.main import play as play_platformer

app = typer.Typer(help="choose a game to play")
app.command(name="pong")(play_pong)
app.command(name="platformer")(play_platformer)


@app.command()
def info():
    """show info"""
    print("pong")


def main():
    """main function"""
    return app()


if __name__ == "__main__":
    main()
