from gameObject import GameObject
from gamePlayer import Player
from gameAI import GamePlayerAI


class Scene:

    # Scene 초기화. scene 번호와 scene 안에 생성할 game_objects 리스트를 초기화.
    def __init__(self, order):
        self.order = order
        self.game_objects = []

    # GameObject 생성. game_objects 리스트에 GameObject를 추가한다.
    def create_object(self, name, pos, sprite, type, layout, bActive):
        self.game_objects.append(GameObject(self.order, name, pos, sprite, type, layout, bActive))

    # Player 생성. game_objects 리스트에 Player 추가한다.
    def create_player(self, name, playMode, layer, bActive, frame):
        self.game_objects.append(Player(self.order, name, playMode, layer, bActive, frame))

    # PlayerAI 생성. game_objects 리스트에 PlayerAI 추가한다.
    def create_playerAI(self, name, playMode, layer, bActive, frame):
        self.game_objects.append(GamePlayerAI(self.order, name, playMode, layer, bActive, frame))

    # Scene 렌더링. scene 안에 담겨있는 모든 GameObjects를 game_objects 리스트를 통해 렌더링 한다.
    def render_objects(self):
        for object in self.game_objects:
            object.update()
            object.render()

    # scene 안에 game_objects 리스트에 들어있는 객체를 이름으로 찾기
    def fine_object(self, name):
        for object in self.game_objects:
            if object.name == name:
                return object

        return None
