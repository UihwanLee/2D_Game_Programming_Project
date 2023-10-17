import GameObject

class Scene:
    def __init__(self, order):
        self.order = order
        self.gameObjects = []

    def BuildObjects(self):
        self.gameObjects.append(GameObject(self.order, (0,0), 'Sprites/BG_Base.png', 0, True))
