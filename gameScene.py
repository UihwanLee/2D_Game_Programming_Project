from gameObject import GameObject
from gamePlayer import Hitter
from gameAI import Pitcher, Defender
from gameUIManager import UIManager

from Define import *

from pico2d import get_events, load_image, load_font
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT

'''
    2DGP Scene을 구현하는 모듈
    
    Scene은 다음과 같이 정의한다.
    
    Scene01 : 시작 화면/옵션 선택
    Scene02 : 로비/팀 선택 화면
    Scene03 : 경기 플레이 화면 01
    Scene04 : 경기 플레이 화면 02

'''


class Scene:

    # Scene 초기화. scene 번호와 scene 안에 생성할 game_objects 리스트를 초기화.
    def __init__(self, order, engine):
        self.order = order
        self.ui_manager = UIManager()
        self.game_engine = engine
        self.game_objects = [[] for _ in range(4)]

    # GameObject 생성. game_objects 리스트에 GameObject를 추가한다.
    def create_object(self, name, pos, sprite, size, type, layer, bActive):
        self.game_objects[layer].append(GameObject(self.order, name, pos, sprite, size, type, layer, bActive))

    # Player 생성. game_objects 리스트에 Player 추가한다.
    def create_hitter(self, name, playMode, layer, bActive, frame):
        self.game_objects[layer].append(Hitter(self.order, name, playMode, layer, bActive, frame))

    # PlayerAI 생성. game_objects 리스트에 PlayerAI 추가한다.
    def create_pitcher(self, name, playMode, layer, bActive, frame):
        self.game_objects[layer].append(Pitcher(self.order, name, playMode, layer, bActive, frame))

    def create_defender(self, name, pos, playMode, layer, bActive, frame):
        self.game_objects[layer].append(Defender(self.order, name, pos, playMode, layer, bActive, frame))

    # ui를 생성하는 함수. scene에서 사용할 ui 오브젝트를 관리하는 클래스를 생성한다
    def create_ui(self, name, pos, sprite, size, type, layer, bActive, ui_size):
        self.ui_manager.create_ui(name, pos, sprite, size, type, layer, bActive, ui_size)

    # Scene에서 handle_event 처리(오버라이딩 처리)
    def handle_event(self, event):
        pass

    def update(self):
        for layer in self.game_objects:
            for object in layer:
                object.update()
        self.ui_manager.update()

    # Scene 렌더링. scene 안에 담겨있는 모든 GameObjects / ui를 game_objects 리스트를 통해 렌더링 한다.
    def render(self):
        for layer in self.game_objects:
            for object in layer:
                object.render()
        self.ui_manager.render()

    # scene 안에 game_objects 리스트에 들어있는 객체를 이름으로 찾기
    def find_object(self, name):
        for layer in self.game_objects:
            for object in layer:
                if object.name == name:
                    return object

        return None

    # scene 안에 ui_manager 클래스의 ui_list에서 ui 이름으로 찾기
    def find_ui(self, ui):
        return self.ui_manager.find_ui(ui)

    # 오브젝트 활성화/비활성화 설정
    def set_object_bActive(self, name, bActive):
        for layer in self.game_objects:
            for object in layer:
                if object.name == name:
                    object.bActive = bActive

    # 씬 전환
    def change_scene(self, scene):
        self.game_engine.change_scene(scene)

    # 게임 종료
    def quit(self):
        if self.game_engine is not None:
            self.game_engine.quit()

    # scene 멤버변수 get 함수
    def get_object_var(self, var):
        if hasattr(self, var):
            return getattr(self, var)
        else:
            print('No var in Object')
            return None
