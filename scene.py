from pico2d import clear_canvas, update_canvas

from gameObject import GameObject

class Scene:
    def __init__(self, order):
        self.order = order
        self.gameObjects = []

    def CreateObject(self, pos, sprite, layout, bActive):
        self.gameObjects.append(GameObject(self.order, pos, sprite, layout, bActive))

    def Render(self):
        clear_canvas()
        for object in self.gameObjects:
            object.Render()
        update_canvas()
