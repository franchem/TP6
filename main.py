import arcade as ac
from pyglet.event import EVENT_HANDLE_STATE
from enum import Enum
import game_state, attack_animation, cursorbox, random
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
WINDOW_TITLE = "Dwayne Johnson, Fichiers Epstein, Couple Lesbienne"

class Choices(Enum):
    ROCK = 0
    PAPER = 2
    SCISSORS = 3

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
        self.dynamics["rock"] = attack_animation.Animated_Sprite("assets/animations/rock", mirrored=True, scale=5)
        self.dynamics["paper"] = attack_animation.Animated_Sprite("assets/animations/paper", mirrored=True, scale=5)
        self.dynamics["scissors"] = attack_animation.Animated_Sprite("assets/animations/scissors", mirrored=True, scale=5)
        self.dynamics["robot"] = attack_animation.Multi_Animation_sprite(["assets/animations/test",
                                                                          "assets/animations/rock",
                                                                          "assets/animations/paper",
                                                                          "assets/animations/scissors"], mirrored=True, scale=5)

        self.human_wins = 0
        self.robot_wins = 0
        self.robot_choice = 0
        self.clash_result = "rien"

    def setup(self):
        self.dynamics["rock"].position = (100, 150)
        self.dynamics["paper"].position = (280, 150)
        self.dynamics["scissors"].position = (460, 150)

        self.human.position = (280, 350)
        self.human.scale = 2.5
        self.computer.position = (800, 350)
        self.computer.scale = 2.5

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if self.state == game_state.State.GAME_OVER:
            self.human_wins = 0
            self.robot_wins = 0
        self.state = game_state.State.ROUND_ACTIVE
        self.clash_result = random.choice(("draw", "com win", "hum win"))


    def draw_static(self):
        ac.draw_text("Roche, Papier, Ciseaux", 150, 800, (50, 150, 150), 60)
        # carres blancs
        ac.draw.draw_lrbt_rectangle_outline(20., 180, 70, 230, (100, 100, 100), 10)
        ac.draw.draw_lrbt_rectangle_outline(200, 360, 70, 230, (100, 100, 100), 10)
        ac.draw.draw_lrbt_rectangle_outline(380, 540, 70, 230, (100, 100, 100), 10)
        # carre rouge
        ac.draw.draw_lrbt_rectangle_outline(720, 880, 70, 230, (250, 0, 0), 10)

        # faces
        ac.draw_sprite(self.human, pixelated=True)
        ac.draw_sprite(self.computer, pixelated=True)

    def on_draw(self):
        self.clear()
        self.draw_static()

        ac.draw_sprite(self.dynamics["rock"], pixelated=True)
        ac.draw_sprite(self.dynamics["paper"], pixelated=True)
        ac.draw_sprite(self.dynamics["scissors"], pixelated=True)

        if self.state == game_state.State.NOT_STARTED:
            ac.draw_text("Pesez sur espace pour débuter", 100, 700, (255, 255, 255), 50)
        elif self.state == game_state.State.ROUND_ACTIVE:
            ac.draw_text("Appuyez sur un des trois icones", 100, 700, (255, 255, 255), 50)

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

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for key in self.dynamics:
            if self.dynamics[key].collides_with_point((x, y)):
                self.state = game_state.State.ROUND_DONE
                if key == "rock":
                    choice = Choices.ROCK
                if key == "paper":
                    choice = Choices.PAPER
                else:
                    choice = Choices.SCISSORS

                if self.clash_result == "draw":
                    self.robot_choice = choice
                elif self.clash_result == "com win":
                    self.robot_choice = (choice+1)%3
                else:
                    self.robot_choice = (choice-1)%3
                self.dynamics["robot"].textures = self.dynamics["robot"].anim_list[self.robot_choice+1]
def main():
    window = GameView()
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()