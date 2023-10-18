from gameObject import *

'''
    Player 클래스 : GameObject 상속
    
'''


class Player(GameObject):
    def __init__(self, scene, pos, sprite, type, layout, bActive, frame):
        super().__init__(scene, pos, sprite, type, layout, bActive)
        self.frame = frame

    def Update(self):
        pass

    def Render(self):
        pos = super().Get('pos')
        sprite = super().Get('sprite')
        sprite.clip_draw(self.frame * 100, 0, 100, 100, pos[0], pos[1], 300, 300)
