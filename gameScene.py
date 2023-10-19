from gameObject import GameObject
from gamePlayer import Player


class Scene:

    # Scene 초기화. scene 번호와 scene 안에 생성할 game_objects 리스트를 초기화.
    def __init__(self, order):
        self.order = order
        self.game_objects = []

    # GameObject 생성. game_objects 리스트에 GameObject를 추가한다.
    def create_object(self, pos, sprite, type, layout, bActive):
        self.game_objects.append(GameObject(self.order, pos, sprite, type, layout, bActive))

    # Player 생성. game_objects 리스트에 Player 추가한다.
    def create_player(self, pos, sprite, type, layout, bActive):
        self.game_objects.append(Player(self.order, pos, sprite, type, layout, bActive, 0))

    # Scene 렌더링. scene 안에 담겨있는 모든 GameObjects를 game_objects 리스트를 통해 렌더링 한다.
    def render_objects(self):
        for object in self.game_objects:
            object.update()
            object.render()
