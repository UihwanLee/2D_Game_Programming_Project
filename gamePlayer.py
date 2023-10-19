from Define import player_Anim
from gameObject import *

'''
    Player 클래스 : GameObject 상속
    
'''


class Player(GameObject):
    def __init__(self, scene, pos, sprite, type, layout, bActive, frame):
        super().__init__(scene, pos, sprite, type, layout, bActive)
        self.frame = frame
        self.time = 0
        self.action = 0

    def update(self):
        self.time += 1

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        time = player_Anim[self.action].delay[self.frame]
        if self.time > time:
            self.frame = (self.frame + 1) % 3
            self.time = 0

    def render(self):
        bActive = super().get('bActive')
        if bActive is False: return

        pos = super().get('pos')
        sprite = super().get('sprite')
        posX, posY = player_Anim[self.action].posX[self.frame], player_Anim[self.action].posY[self.frame]
        sprite.clip_draw(self.frame * 100, 0, 100, 100, posX, posY, 300, 300)
