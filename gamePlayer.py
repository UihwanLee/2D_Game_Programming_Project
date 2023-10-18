from Define import player_IDLE
from gameObject import *
from pico2d import delay

'''
    Player 클래스 : GameObject 상속
    
'''


class Player(GameObject):
    def __init__(self, scene, pos, sprite, type, layout, bActive, frame):
        super().__init__(scene, pos, sprite, type, layout, bActive)
        self.frame = frame

    def Update(self):
        self.frame = (self.frame + 1) % 3

        # 애니메이션의 다이나믹을 위해 delay 추가
        time = player_IDLE.delay[self.frame]
        delay(time)

    def Render(self):
        pos = super().Get('pos')
        sprite = super().Get('sprite')
        posX, posY = player_IDLE.posX[self.frame], player_IDLE.posY[self.frame]
        sprite.clip_draw(self.frame * 100, 0, 100, 100, posX, posY, 300, 300)
