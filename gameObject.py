from pico2d import load_image


class GameObject:
    sprite = None

    def __init__(self, scene, pos, sprite, type, layout, bActive):
        self.scene = scene
        self.pos = pos
        self.type = type
        self.layout = layout
        self.bActive = bActive

        if GameObject.sprite == None:
            GameObject.sprite = load_image(sprite)

    def Update(self):
        pass

    def Render(self):
        self.sprite.draw(self.pos[0], self.pos[1])
