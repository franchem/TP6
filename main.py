import arcade as ac
from pyglet.event import EVENT_HANDLE_STATE

import game_state, attack_animation, cursorbox
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
WINDOW_TITLE = "Dwayne Johnson, Fichiers Epstein, Couple Lesbienne"

class GameView(ac.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.state = game_state.State.NOT_STARTED
        self.rock = attack_animation.Animated_Sprite("animations/test", 1, 9, 18, 18)

    def setup(self):
        self.rock.position = (500, 500)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if self.state == game_state.State.GAME_OVER:
            pass


    def draw_static(self):
        ac.draw_text("Roche, Papier, Ciseaux", 150, 800, (50, 150, 150), 60)

    def on_draw(self):
        self.clear()
        self.draw_static()

        ac.draw_sprite(self.rock, pixelated=True)

        cursorbox.draw_information()

    def on_update(self, delta_time: float) -> bool | None:
        self.rock.update(delta_time)

    def on_mouse_motion(self, x: float, y: float, shit, shit2):
        cursorbox.mouseX = x
        cursorbox.mouseY = y
        if self.rock.collides_with_point((x, y)):
            self.rock.playing = True
        else:
            self.rock.playing = False

def main():
    window = GameView()
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()