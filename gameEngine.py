from pico2d import *

from Define import *
from gameScene import Scene
from gameSystem import GameSystem
from gameUIManager import UIManager


# 게임 내 모든 씬, 오브젝트, 시스템 관리할 클래스
class GameEngine:

    # 게임에서 몇 개의 scene을 사용할 것인지 정하고 초기에 보여줄 scene을 game_world로 설정한다.
    def __init__(self):
        self.running = True
        self.scene_01 = Scene(1)
        self.game_world = self.scene_01
        self.game_system = GameSystem()
        self.ui_manager = UIManager()
        self.player = None
        pass

    # 게임 내에서 사용할 game_system, player, playerAI 등을 초기화
    def init_setting(self):
        self.game_system.playerAI = self.game_world.find_object('playerAI')
        self.game_system.base_ball = self.game_world.find_object(base_ball_name)

        self.player = self.game_world.find_object(player_name)
        self.player.game_system = self.game_system

        self.game_system.throw_target = self.ui_manager.find_ui(throw_target_name)
        self.game_system.throw_target_effect = self.ui_manager.find_ui(throw_target_effect_name)
        self.game_system.throw_target_end = self.ui_manager.find_ui(throw_target_end_name)

        self.playerAI = self.game_system.playerAI
        self.playerAI.game_system = self.game_system

        self.game_system.ui_manager = self.ui_manager

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
        self.scene_01.create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 2, False)

    # ui를 생성하는 함수. 게임에서 사용할 ui 오브젝트를 관리하는 클래스를 생성한다.
    def create_ui(self):
        self.ui_manager.create_ui(throw_target_name, throw_target_pos, throw_target_img, throw_target_size, DYNAMIC,1, False, throw_target_ui_size)
        self.ui_manager.create_ui(throw_target_effect_name, throw_target_effect_pos, throw_target_effect_img, throw_target_effect_size, DYNAMIC, 1, False, throw_target_effect_ui_size)
        self.ui_manager.create_ui(throw_target_end_name, throw_target_end_pos, throw_target_end_img, throw_target_end_size, DYNAMIC, 1, False, throw_target_end_ui_size)
        self.ui_manager.create_ui(message_strike, message_strike_pos, message_strike_img, message_strike_size, DYNAMIC, 2, False, message_strike_ui_size)
        self.ui_manager.create_ui(message_strike_out, message_strike_out_pos, message_strike_out_img, message_strike_out_size, DYNAMIC,2, False, message_strike_out_ui_size)
        self.ui_manager.create_ui(message_ball, message_ball_pos, message_ball_img, message_ball_size, DYNAMIC, 2, False, message_ball_ui_size)

    # scene을 렌더링하는 함수. 현재 game_world 리스트 안에 들어있는 모든 객체를 렌더링한다.
    def render_world(self):
        clear_canvas()
        self.game_world.render_objects()
        self.ui_manager.render()
        update_canvas()

    # 게임 시스템을 계속해서 업데이트 하는 함수
    def update_world(self):
        if self.game_system:
            self.game_system.update()

        if self.ui_manager:
            self.ui_manager.update()

    # 게임을 실행하는 함수. 모든 scene을 render하고 이벤트를 지속적으로 받는다.
    def run(self):
        open_canvas()
        self.create_scenes()
        self.create_ui()
        self.init_setting()
        while self.running:
            self.update_world()
            self.render_world()
            self.handle_events()
        close_canvas()
