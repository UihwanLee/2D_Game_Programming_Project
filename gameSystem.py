from Define import TOP
from gameAI import *
from Define import BOTTOM

'''
    2DGP 게임에서 야구 시스템을 동작하는 클래스
    
    야구 룰
    야구 애니메이션
    
'''


class GameSystem:
    INNING = 0  # 이닝
    INNING_STATE = TOP  # 초/말 (TOP/BOTTOM)

    OUT = 0  # 아웃 횟수
    STRIKE = 0  # 스트라이크 횟수
    BALL = 0  # 볼 횟수

    SCORE_TEAM_01 = 0  # 팀1 점수
    SCORE_TEAM_02 = 0  # 팀2 점수

    def __int__(self):
        self.playerAI = None
        self.throw_target = None
        self.throw_target_effect = None

    # GameSystem 리셋. 모든 System 변수를 초기화 한다.
    def reset_system(self):
        GameSystem.INNING = 0
        GameSystem.INNING_STATE = TOP

        GameSystem.OUT = 0
        GameSystem.STRIKE = 0
        GameSystem.BALL = 0

        GameSystem.SCORE_TEAM_01 = 0
        GameSystem.SCORE_TEAM_02 = 0
    
    # Player 공/수 선택 공->타자 / 수->투수로 시스템 설정 하기
    def SetPlayMode(self):
        pass

    # 투수 AI 공 던지기
    def throw_ball(self):
        self.playerAI.throw_ball()

    def generate_random_throw_target(self):
        # 던진 공 위치는 게임 내 사각 박스 내에 랜덤으로 생성
        pos_x = random.randint(360, 450)
        pos_y = random.randint(90, 210)

        self.throw_target.pos = [pos_x, pos_y]

        self.throw_target_effect.pos = [pos_x, pos_y]
        self.throw_target_effect.size = [300, 300]

        # 공 위치를 표시하고 이펙트를 나타낼 오브젝트 활성화
        self.throw_target.bActive = True
        self.throw_target_effect.bActive = True