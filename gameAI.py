from gameObject import GameObject
from Define import Pitcher_Anim

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


class GamePlayerAI(GameObject)

    # 게임에서 활용될 GamePlayerAI 클래스 초기화:
    def __init__(self, scene, pos, sprite, type, layer, bActive, frame):
        super().__init__(scene, pos, sprite, type, layer, bActive)
        self.frame = frame
        self.time = 0
        self.action = 0
        self.ai_Anim = Pitcher_Anim

class GameSystemAI

    # 게임에서 활용될 GamePlayerAI 클래스 초기화:
    def __init__(self):
        pass