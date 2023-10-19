from pico2d import load_image


class GameObject:
    def __init__(self, scene, pos, sprite, type, layout, bActive):
        self.scene = scene
        self.pos = pos
        self.sprite = load_image(sprite)
        self.type = type
        self.layout = layout
        self.bActive = bActive

    def update(self):
        pass

    def render(self):
        self.sprite.draw(self.pos[0], self.pos[1])

    def get(self, var):
        if hasattr(self, var):
            return getattr(self, var)
        else:
            print('No var in Object')
            return None
