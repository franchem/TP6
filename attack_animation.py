import arcade
from pathlib import Path


class Animated_Sprite(arcade.Sprite):
    def __init__(self, path, mirrored=False, scale=1):

        super().__init__()

        dir_path = Path(path)
        self.textures = []
        for file in dir_path.iterdir():
            self.textures.append(arcade.load_texture(path+"/"+file.name))
        if mirrored:
            mirrored_list = self.textures[::-1]
            mirrored_list.pop(0)
            mirrored_list.pop(-1)
            for texture in mirrored_list:
                self.textures.append(texture)

        self.cur_texture_index = 0
        self.set_texture(self.cur_texture_index)

        self.current_delay = 0
        self.animation_delay = 0.1
        self.scale = scale
        self.playing = False

    def update(self, delta_time):
        if self.playing:
            self.current_delay += delta_time
            if self.current_delay > self.animation_delay:
                self.current_delay = 0
                self.set_texture(self.cur_texture_index)
                self.cur_texture_index += 1
                if self.cur_texture_index == len(self.textures):
                    self.cur_texture_index = 0


class Multi_Animation_sprite(arcade.Sprite):
    def __init__(self, lst, mirrored=False, scale=1):
        super().__init__()
        self.anim_list = []
        for path in lst:
            dir_path = Path(path)
            self.anim_list.append([])
            for file in dir_path.iterdir():
                self.anim_list[-1].append(arcade.load_texture(path + "/" + file.name))
            if mirrored:
                mirrored_list = self.anim_list[-1][::-1]
                mirrored_list.pop(0)
                mirrored_list.pop(-1)
                for texture in mirrored_list:
                    self.anim_list[-1].append(texture)
        self.textures = self.anim_list[0]
        self.cur_texture_index = 0
        self.set_texture(self.cur_texture_index)
        self.current_delay = 0
        self.animation_delay = 0.1
        self.scale = scale
        self.playing = False

    def update(self, delta_time):
        if self.playing:
            self.current_delay += delta_time
            if self.current_delay > self.animation_delay:
                self.current_delay = 0
                self.set_texture(self.cur_texture_index)
                self.cur_texture_index += 1
                if self.cur_texture_index == len(self.textures):
                    self.cur_texture_index = 0
