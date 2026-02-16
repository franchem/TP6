import arcade


class Animated_Sprite(arcade.Sprite):
    def __init__(self, path, rows, columns, sizeX, sizeY):

        super().__init__()

        # code pour transformer une spritesheet en spritelist
        self.texture_list = []
        sheet = arcade.load_spritesheet(f"{path}.png")
        texture_list = sheet.get_texture_grid(
            size=(sizeX, sizeY),
            columns=columns,
            count=rows*columns
        )
        for a in texture_list:
            self.texture_list.append(a)

        self.cur_texture_index = 0
        self.textures = self.texture_list
        self.set_texture(self.cur_texture_index)
        self.current_delay = 0
        self.animation_delay = 0.1
        self.scale = 4
        self.playing = False

    def update(self, delta_time):
        if self.playing:
            self.current_delay += delta_time
            if self.current_delay > self.animation_delay:
                self.current_delay = 0
                self.set_texture(self.cur_texture_index)
                self.cur_texture_index += 1
                if self.cur_texture_index >= len(self.textures)-1:
                    self.cur_texture_index = 0
