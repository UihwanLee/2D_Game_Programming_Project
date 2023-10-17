from pico2d import load_image


class GameObject:
    sprite = None

    def __init__(self, scene, pos, sprite, layout, bActive):
        self.scene = scene
        self.pos = pos
        self.layout = layout
        self.bActive = bActive

        if GameObject.sprite == None:
            GameObject.sprite = load_image(sprite)

    def Update(self):
        pass

    def Draw(self):
        self.image.draw(self.pos.x, self.pos.y)
