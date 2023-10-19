from gameObject import GameObject

'''
    2DGP 야구 게임에서 활용될 AI 모듈.
    크게 2가지 역할을 수행한다.

    <class GamePlayerAI>
     - Player와 대비되는 역할 수행
      ex) player-> 투수 / ai -> 타자

    <class GameSystemAI>
     - 전반적으로 게임에서 필요한 AI 역할
     - 2DGP 야구 게임에서 수비 역할

'''


class GamePlayerAI(GameObject):

    # 게임에서 활용될 GamePlayerAI 클래스 초기화:
    def __init__(self, scene, name, playMode, layer, bActive, frame):
        super().__init__(scene, name, playMode.pos, playMode.sprite_sheet, playMode.type, layer, bActive)
        self.play_Mode = playMode
        self.frame = frame
        self.time = 0
        self.action = 0
        self.play_Anim = self.play_Mode.anim

    def update(self):
        bActive = super().get_object_var('bActive')
        if bActive is False: return

        self.time += 1

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        time = self.play_Anim[self.action].delay[self.frame]

        if self.time > time:
            self.frame = (self.frame + 1) % 3
            self.time = 0

    # playerAI 렌더링. play_Anim 리스트를 기준으로 렌더링 한다.
    def render(self):
        bActive = super().get_object_var('bActive')
        if bActive is False: return

        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        posX, posY = self.play_Anim[self.action].posX[self.frame], self.play_Anim[self.action].posY[self.frame]
        sizeX, sizeY = self.play_Mode.size[0], self.play_Mode.size[1]
        sprite.clip_draw(self.frame * 100, 0, 100, 100, posX, posY, sizeX, sizeY)

class GameSystemAI:

    # 게임에서 활용될 GamePlayerAI 클래스 초기화:
    def __init__(self):
        pass