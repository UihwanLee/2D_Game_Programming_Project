from pico2d import *

from Define import *
from scene import Scene


# 게임 내 모든 씬, 오브젝트, 시스템 관리할 클래스
class GameEngine:
    def __init__(self):
        self.running = True
        self.scene_01 = Scene(1)
        self.curScene = self.scene_01
        pass

    def Handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                self.running = False

    def BuildScenes(self):
        self.scene_01.CreateObject(background_pos, background_img, background_type, 0, True)
        pass

    def RenderScenes(self):
        self.curScene.Render()

    def Run(self):
        open_canvas()
        self.BuildScenes()
        while self.running:
            self.RenderScenes()
            self.Handle_events()
        close_canvas()


