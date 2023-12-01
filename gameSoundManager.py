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

    def stopBGM(self):
        if self.bgm:
            self.bgm.stop()

    def playSE(self, volume):
        if self.se:
            self.se.set_volume(volume)
            self.se.play()

class SoundManager:
    def __init__(self):
        self.cur_bgm = None
        self.bgm = {}
        self.sound_effect = {}

    def create_bgm(self, name, bgm):
        self.bgm[name] = Sound(name, bgm, None)

    def create_sound_effect(self, name, sound_effect):
        self.sound_effect[name] = Sound(name, None, sound_effect)

    def playBGM(self):
        self.bgm[self.cur_bgm].playBGM()

    def setBGM(self, bgm):
        self.cur_bgm = bgm

    def stopBGM(self, bgm):
        self.bgm[self.cur_bgm].stopBGM()

    def playSE(self, se, volume):
        if self.sound_effect[se]:
            self.sound_effect[se].playSE(volume)

