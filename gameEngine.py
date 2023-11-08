from pico2d import *

from Define import *
from gameScene import Scene
from gameScene import Scene01
from gameScene import Scene02
from gameScene import Scene03
from gameScene import Scene04
from gameSystem import GameSystem
from gameUIManager import UIManager

from gameTime import Time

# 게임 내 모든 씬, 오브젝트, 시스템 관리할 클래스
class GameEngine:
    # 게임에서 몇 개의 scene을 사용할 것인지 정하고 초기에 보여줄 scene을 game_world로 설정한다.
    def __init__(self):
        self.running = True

        # Scene 생성
        self.scene_01 = Scene01(1, self)
        self.scene_02 = Scene02(2, self)
        self.scene_03 = Scene03(3, self)
        self.scene_04 = Scene04(4, self)

        # 현재 게임 엔진에서 첫번째로 불러올 씬
        self.game_world = self.scene_01

        # 게임에서 사용할 player
        self.player = None

        # 클래스
        self.game_system = GameSystem()
        self.time = Time()

    # 게임 내에서 사용할 game_system, player, playerAI 등을 초기화
    def init_setting(self):
        # scene03
        self.game_system.playerAI = self.scene_03.find_object(playerAI_name)
        self.game_system.base_ball = self.scene_03.find_object(base_ball_name)
        self.game_system.throw_target = self.scene_03.find_ui(throw_target_name)
        self.game_system.throw_target_effect = self.scene_03.find_ui(throw_target_effect_name)
        self.game_system.throw_target_end = self.scene_03.find_ui(throw_target_end_name)
        self.player = self.scene_03.find_object(player_name)
        self.player.game_system = self.game_system
        self.playerAI = self.game_system.playerAI
        self.playerAI.game_system = self.game_system

        # scene04
        self.game_system.base = self.scene_04.find_object(background_base_02_name)
        self.game_system.base_ball_base = self.scene_04.find_object(base_ball_name)

        # module
        self.game_system.ui_manager = self.game_world.ui_manager
        self.game_system.game_engine = self

    # 이벤트 처리 함수. 각 Scene마다 handle_event 처리 방식이 다르다.
    def handle_events(self):
        self.game_world.handle_event()

    # scene을 초기화 함수. scene에 그릴 scene 정보/오브젝트 정보를 전달한다.
    def create_scenes(self):
        self.scene_01.start()
        self.scene_02.start()
        self.scene_03.start()
        self.scene_04.start()

    # 씬 변경 함수
    def change_scene(self, scene):
        if hasattr(self, scene):
            self.game_world = getattr(self, scene)
            self.game_system.ui_manager = self.game_world.ui_manager # ui_manager도 바꿔줄 수 있도록 함.

    # scene을 렌더링하는 함수. 현재 game_world 리스트 안에 들어있는 모든 객체를 렌더링한다.
    def render_world(self):
        clear_canvas()
        self.game_world.render()
        #self.ui_manager.render()
        update_canvas()

    # 게임 시스템을 계속해서 업데이트 하는 함수
    def update_world(self):
        if self.game_system:
            self.game_system.update()

        self.game_world.update()

    # 게임을 실행하는 함수. 모든 scene을 render하고 이벤트를 지속적으로 받는다.
    def run(self):
        open_canvas()
        self.create_scenes()
        self.init_setting()
        while self.running:
            self.update_world()
            self.render_world()
            self.handle_events()
            self.time.update()
        close_canvas()

    def quit(self):
        self.running = False

