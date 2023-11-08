from gameObject import GameObject
from gamePlayer import Player
from gameAI import GamePlayerAI
from gameUIManager import UIManager

from Define import *

from pico2d import get_events
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE

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
        self.game_engine = engine
        self.game_objects = [[] for _ in range(4)]

    # GameObject 생성. game_objects 리스트에 GameObject를 추가한다.
    def create_object(self, name, pos, sprite, size, type, layer, bActive):
        self.game_objects[layer].append(GameObject(self.order, name, pos, sprite, size, type, layer, bActive))

    # Player 생성. game_objects 리스트에 Player 추가한다.
    def create_player(self, name, playMode, layer, bActive, frame):
        self.game_objects[layer].append(Player(self.order, name, playMode, layer, bActive, frame))

    # PlayerAI 생성. game_objects 리스트에 PlayerAI 추가한다.
    def create_playerAI(self, name, playMode, layer, bActive, frame):
        self.game_objects[layer].append(GamePlayerAI(self.order, name, playMode, layer, bActive, frame))

    # Scene에서 handle_event 처리
    def handle_event(self, event):
        pass

    # Scene 렌더링. scene 안에 담겨있는 모든 GameObjects를 game_objects 리스트를 통해 렌더링 한다.
    def render_objects(self):
        for layer in self.game_objects:
            for object in layer:
                object.update()
                object.render()

    # scene 안에 game_objects 리스트에 들어있는 객체를 이름으로 찾기
    def find_object(self, name):
        for layer in self.game_objects:
            for object in layer:
                if object.name == name:
                    return object

        return None

    # 게임 종료
    def quit(self):
        if self.game_engine is not None:
            self.game_engine.quit()


class Scene03(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.ui_manager = UIManager()
        self.player = None

    # scene에서 초기 오브젝트 세팅
    def start(self):
        super().create_object(background_name, background_pos, background_img, background_size, background_type, 0,
                              True)
        super().create_player(player_name, Hitter, 3, True, 0)
        super().create_playerAI(playerAI_name, Pitcher, 1, True, 0)
        super().create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 2, False)

        self.player = super().find_object(player_name)

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                super().quit()
            else:
                if (self.player != None):
                    if (self.player.bActive):
                        self.player.handle_event(event)

    # Scene 렌더링. scene 안에 담겨있는 모든 GameObjects를 game_objects 리스트를 통해 렌더링 한다.
    def render_objects(self):
        super().render_objects()

    # scene 안에 game_objects 리스트에 들어있는 객체를 이름으로 찾기
    def find_object(self, name):
        return super().find_object(name)


class Scene04(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.ui_manager = UIManager()

    # scene에서 초기 오브젝트 세팅
    def start(self):
        super().create_object(background_base_02_name, background_base_02_pos, background_base_02_img,
                              background_base_02_size, STATIC, 0, True)
        super().create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 1, True)

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                self.running = False
            else:
                pass

    # Scene 렌더링. scene 안에 담겨있는 모든 GameObjects를 game_objects 리스트를 통해 렌더링 한다.
    def render_objects(self):
        super().render_objects()

    # scene 안에 game_objects 리스트에 들어있는 객체를 이름으로 찾기
    def find_object(self, name):
        return super().find_object(name)
