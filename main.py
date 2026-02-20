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

        self.human = ac.Sprite("assets/human.png")
        self.computer = ac.Sprite("assets/compy.png")

        self.dynamics = {}
        self.dynamics["rock"] = attack_animation.Animated_Sprite("assets/animations/rock", mirrored=True)

    def setup(self):
        self.dynamics["rock"].position = (100, 150)

        self.human.position = (250, 300)
        self.human.scale = 2
        self.computer.position = (800, 300)
        self.computer.scale = 2

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if self.state == game_state.State.GAME_OVER:
            pass
        self.state = game_state.State.ROUND_ACTIVE


    def draw_static(self):
        ac.draw_text("Roche, Papier, Ciseaux", 150, 800, (50, 150, 150), 60)
        # carres blancs
        ac.draw.draw_lrbt_rectangle_outline(50, 150, 100, 200, (200, 200, 200), 10)
        ac.draw.draw_lrbt_rectangle_outline(200, 300, 100, 200, (200, 200, 200), 10)
        ac.draw.draw_lrbt_rectangle_outline(350, 450, 100, 200, (200, 200, 200), 10)
        # carre rouge
        ac.draw.draw_lrbt_rectangle_outline(750, 850, 100, 200, (250, 0, 0), 10)

        # faces
        ac.draw_sprite(self.human, pixelated=True)
        ac.draw_sprite(self.computer, pixelated=True)

    def on_draw(self):
        self.clear()
        self.draw_static()

        ac.draw_sprite(self.dynamics["rock"], pixelated=True)

        cursorbox.draw_information()

    def on_update(self, delta_time: float) -> bool | None:
        for key in self.dynamics:
            self.dynamics[key].update(delta_time)

    def on_mouse_motion(self, x: float, y: float, shit, shit2):
        cursorbox.mouseX = x
        cursorbox.mouseY = y
        for key in self.dynamics:
            if self.dynamics[key].collides_with_point((x, y)):
                self.dynamics[key].playing = True
            else:
                self.dynamics[key].playing = False

def main():
    window = GameView()
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()