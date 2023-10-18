from pico2d import clear_canvas, update_canvas

from gameObject import GameObject
from gamePlayer import Player

class Scene:
    def __init__(self, order):
        self.order = order
        self.gameObjects = []

    def CreateObject(self, pos, sprite, type, layout, bActive):
        self.gameObjects.append(GameObject(self.order, pos, sprite, type, layout, bActive))

    def CreatePlayer(self, pos, sprite, type, layout, bActive):
        self.gameObjects.append(Player(self.order, pos, sprite, type, layout, bActive, 0))


    def Render(self):
        clear_canvas()
        for object in self.gameObjects:
            object.Render()
        update_canvas()
