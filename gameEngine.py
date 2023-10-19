from pico2d import *

from Define import *
from gameScene import Scene


# 게임 내 모든 씬, 오브젝트, 시스템 관리할 클래스
class GameEngine:
    def __init__(self):
        self.running = True
        self.scene_01 = Scene(1)
        self.game_world = self.scene_01
        pass

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                self.running = False

    def build_scenes(self):
        self.scene_01.create_object(background_pos, background_img, background_type, 0, True)
        self.scene_01.create_player(player_pos, player_img, player_type, 1, True)
        pass

    def render_scenes(self):
        self.game_world.render_objects()

    def run(self):
        open_canvas()
        self.build_scenes()
        while self.running:
            self.render_scenes()
            self.handle_events()
        close_canvas()
