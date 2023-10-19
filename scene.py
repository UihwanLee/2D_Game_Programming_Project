from pico2d import clear_canvas, update_canvas

from gameObject import GameObject
from gamePlayer import Player


class Scene:
    def __init__(self, order):
        self.order = order
        self.gameObjects = []

    def create_object(self, pos, sprite, type, layout, bActive):
        self.gameObjects.append(GameObject(self.order, pos, sprite, type, layout, bActive))

    def create_player(self, pos, sprite, type, layout, bActive):
        self.gameObjects.append(Player(self.order, pos, sprite, type, layout, bActive, 0))

    def render_objects(self):
        clear_canvas()
        for object in self.gameObjects:
            object.update()
            object.render()
        update_canvas()
