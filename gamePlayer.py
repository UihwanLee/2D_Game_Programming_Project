from gameObject import *

'''
    Player 클래스 : GameObject 상속
    
    2DGP 야구 게임에서 사용자가 플레이할 Player.
    Player 객체는 2가지로 수행 된다.

    <class Player>
     - 야구 게임에서 타자/투수를 수행

    <class SystemPlayer>
     - 안타/홈런을 치고 scene_02 에서 수행될 Player 객체
    
'''


class Player(GameObject):

    # Player 클래스 초기화. 상속 받은 GameObject 클래스 초기화.
    # player의 frame, time, action, player_Anim 초기화 한다.
    def __init__(self, scene, playMode, layer, bActive, frame):
        super().__init__(scene, playMode.pos, playMode.sprite_sheet, playMode.type, layer, bActive)
        self.playMode = playMode
        self.play_Anim = playMode.anim
        self.frame = frame
        self.time = 0
        self.action = 0

    # player 업데이트. time 변수를 기준으로 각족 이벤트를 처리한다.
    def update(self):
        bActive = super().get_object_var('bActive')
        if bActive is False: return

        self.time += 1

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        time = self.play_Anim[self.action].delay[self.frame]
        if self.time > time:
            self.frame = (self.frame + 1) % 3
            self.time = 0

    # player 렌더링. player_Anim 리스트를 기준으로 렌더링 한다.
    def render(self):
        bActive = super().get_object_var('bActive')
        if bActive is False: return

        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        posX, posY = self.play_Anim[self.action].posX[self.frame], self.play_Anim[self.action].posY[self.frame]
        sizeX, sizeY = self.playMode.size[0], self.playMode.size[1]
        sprite.clip_draw(self.frame * 100, 0, 100, 100, posX, posY, sizeX, sizeY)
