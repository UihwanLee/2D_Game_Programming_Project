from Define import player_Anim
from gameObject import *

'''
    Player 클래스 : GameObject 상속
    
'''


class Player(GameObject):

    # Player 클래스 초기화. 상속 받은 GameObject 클래스 초기화.
    # player의 frame, time, action, player_Anim 초기화 한다.
    def __init__(self, scene, pos, sprite, type, layer, bActive, frame):
        super().__init__(scene, pos, sprite, type, layer, bActive)
        self.frame = frame
        self.time = 0
        self.action = 0
        self.player_Anim = player_Anim

    # player 업데이트. time 변수를 기준으로 각족 이벤트를 처리한다.
    def update(self):
        bActive = super().get_object_var('bActive')
        if bActive is False: return

        self.time += 1

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        time = self.player_Anim[self.action].delay[self.frame]
        if self.time > time:
            self.frame = (self.frame + 1) % 3
            self.time = 0

    # player 렌더링. player_Anim 리스트를 기준으로 렌더링 한다.
    def render(self):
        bActive = super().get_object_var('bActive')
        if bActive is False: return

        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        posX, posY = self.player_Anim[self.action].posX[self.frame], self.player_Anim[self.action].posY[self.frame]
        sprite.clip_draw(self.frame * 100, 0, 100, 100, posX, posY, 300, 300)
