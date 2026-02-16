import arcade

mouseX, mouseY = 0, 0

# a mettre dans le GameView
'''
def on_mouse_motion(self, x: float, y: float):
        cursorbox.mouseX = x
        cursorbox.mouseY = y
'''
# a mettre dans le on_draw()
# cursorbox.draw_information()

def draw_information():
    global mouseX
    global mouseY
    arcade.draw.draw_lrbt_rectangle_filled(mouseX+20, mouseX+80, mouseY-25, mouseY+5, (0, 0, 0))
    arcade.draw_text("X:"+str(mouseX), mouseX+20, mouseY-10, arcade.color.WHITE, 12)
    arcade.draw_text("Y:"+str(mouseY), mouseX+20, mouseY-23, arcade.color.WHITE, 12)