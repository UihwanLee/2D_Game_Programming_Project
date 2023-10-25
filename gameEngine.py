from pico2d import *

from Define import *
from gameScene import Scene
from gameSystem import GameSystem


# 게임 내 모든 씬, 오브젝트, 시스템 관리할 클래스
class GameEngine:

    # 게임에서 몇 개의 scene을 사용할 것인지 정하고 초기에 보여줄 scene을 game_world로 설정한다.
    def __init__(self):
        self.running = True
        self.scene_01 = Scene(1)
        self.game_world = self.scene_01
        self.game_system = GameSystem()
        self.player = None
        pass

    # 이벤트 처리 함수. gamePlayer와 gameSystem 모듈로 전달하여 이벤틍에 적절한 동작을 수행한다.
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                self.running = False
            else:
                if(self.player != None):
                    if(self.player.bActive):
                        self.player.handle_event(event)

    # scene을 생성하는 함수. scene에 그릴 scene 정보/오브젝트 정보를 전달한다.
    def create_scenes(self):
        self.scene_01.create_object(background_name, background_pos, background_img, background_size,background_type, 0, True)
        self.scene_01.create_player(player_name, Hitter, 1, True,  0)
        self.scene_01.create_playerAI(playerAI_name, Pitcher, 1, True, 0)
        self.scene_01.create_object(throw_target_name, throw_target_pos, throw_target_img, throw_target_size, DYNAMIC, 1, True)
        self.scene_01.create_object(throw_target_effect_name, throw_target_effect_pos, throw_target_effect_img, throw_target_effect_size, DYNAMIC, 1, True)
        pass

    # scene을 렌더링하는 함수. 현재 game_world 리스트 안에 들어있는 모든 객체를 렌더링한다.
    def render_scenes(self):
        clear_canvas()
        self.game_world.render_objects()
        update_canvas()

    # 게임을 실행하는 함수. 모든 scene을 render하고 이벤트를 지속적으로 받는다.
    def run(self):
        open_canvas()
        self.create_scenes()
        self.player = self.game_world.fine_object('player')
        self.game_system.playerAI = self.game_world.fine_object('playerAI')
        self.game_system.throw_ball()
        while self.running:
            self.render_scenes()
            self.handle_events()
        close_canvas()
