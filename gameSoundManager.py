from pico2d import *
from gameObject import *

from Define import *

'''
    2DGP 게임에서 Sound를 관리하는 모듈

    게임 background
    게임 sound_effect

'''

class Sound(GameObject):
    def __init__(self, name, bgm, sound_effect):
        super().__init__(-1, name, [0, 0], None, [10, 10], STATIC, 0, False, bgm, sound_effect)
        # self.sound = load_music(bgm)

    def playBGM(self):
        if self.bgm:
            self.bgm.set_volume(32)
            self.bgm.repeat_play()

class SoundManager:
    def __init__(self):
        self.cur_bgm = None
        self.bgm = {}
        self.sound_effect = {}

    def create_bgm(self, name, bgm):
        self.bgm[name] = Sound(name, bgm, None)

    def create_sound_effect(self, name, sound_effect):
        self.sound_effect[name] = Sound(name, None, sound_effect)

    def init_sound(self):
        # BGM
        self.create_bgm(bgm_scene01_name, bgm_scene01_path)
        self.create_bgm(bgm_scene02_name, bgm_scene02_path)

        # Sound Effect
        self.create_sound_effect(sf_button_click_name, sf_button_click_path)
        self.create_sound_effect(sf_hit_name, sf_hit_path)
        self.create_sound_effect(sf_hit_home_run_name, sf_hit_home_run_path)
        self.create_sound_effect(sf_throw_name, sf_throw_path)
        self.create_sound_effect(sf_out_name, sf_out_path)
        self.create_sound_effect(sf_safe_name, sf_safe_path)
        self.create_sound_effect(sf_strike_name, sf_strike_path)
        self.create_sound_effect(sf_strike_out_name, sf_strike_out_path)
        self.create_sound_effect(sf_ball_name, sf_ball_path)
        self.create_sound_effect(sf_home_run_name, sf_home_run_path)

    def playBGM(self):
        self.bgm[self.cur_bgm].playBGM()

    def setBGM(self, bgm):
        self.cur_bgm = bgm
