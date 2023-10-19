from gameObject import GameObject
from gamePlayer import Player


class Scene:
    def __init__(self, order):
        self.order = order
        self.game_objects = []

    def create_object(self, pos, sprite, type, layout, bActive):
        self.game_objects.append(GameObject(self.order, pos, sprite, type, layout, bActive))

    def create_player(self, pos, sprite, type, layout, bActive):
        self.game_objects.append(Player(self.order, pos, sprite, type, layout, bActive, 0))

    def render_objects(self):
        for object in self.game_objects:
            object.update()
            object.render()
