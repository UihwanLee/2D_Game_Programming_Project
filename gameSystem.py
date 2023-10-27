import math

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

    def __init__(self):
        self.playerAI = None
        self.throw_target = None
        self.throw_target_effect = None
        self.base_ball = None

        # 공 박자 변수
        self.is_check_throw_event_by_hit = False
        self.throw_event_rate = 0
        self.throw_hit_offset = 0.0

        # 야구공 초기위치와 타켓 위치
        self.is_throw_ball_to_target_anim = False
        self.base_ball_pos_x = 400
        self.base_ball_pos_y = 300
        self.base_ball_target_x = 0
        self.base_ball_target_y = 0
        self.throw_angle = 0
        self.throw_speed = 0

        self.temp = 0

    # GameSystem update 함수 특정 이벤트를 검사하는 일을 수행한다.
    def update(self):
        if self.is_check_throw_event_by_hit:
            self.check_throw_event_by_hit()

        if self.is_throw_ball_to_target_anim:
            self.throw_ball_to_target_anim()

    # GameSystem 리셋. 모든 System 변수를 초기화 한다.
    def reset_system(self):
        GameSystem.INNING = 0
        GameSystem.INNING_STATE = TOP

        GameSystem.OUT = 0
        GameSystem.STRIKE = 0
        GameSystem.BALL = 0

        GameSystem.SCORE_TEAM_01 = 0
        GameSystem.SCORE_TEAM_02 = 0

        self.throw_event_rate = 0
        self.throw_hit_offset = 0.0
    
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
        self.throw_target_effect.size = [200, 200]

        # 공 위치를 표시하고 이펙트를 나타낼 오브젝트 활성화
        self.throw_target.bActive = True
        self.throw_target_effect.bActive = True

        self.is_check_throw_event_by_hit = True

        # 야구공 활성화 및 타겟 위치 세팅
        self.base_ball.bActive = True
        self.throw_ball_to_target_anim()

        self.base_ball_pos_x = 380
        self.base_ball_pos_y = 300
        self.base_ball.size = [60, 60]

        self.calculate_throw_angle(pos_x, pos_y)

        self.is_throw_ball_to_target_anim = True

    # 지정된 공 위치에 따른 공 던지는 각도, 위치 등 계산
    def calculate_throw_angle(self, pos_x, pos_y):
        # 지정된 공 위치에 따라 조금 벗어난 위치로 설정
        offset_x, offset_y = 0, -10
        if(pos_x > 420): offset_x = 10
        elif(pos_x <= 390) : offset_x = -10
        self.base_ball_target_x = pos_x + offset_x
        self.base_ball_target_y = pos_y + offset_y

        distance = math.sqrt((self.base_ball_target_x - self.base_ball_pos_x) ** 2 + (
                    self.base_ball_target_y - self.base_ball_pos_y) ** 2)
        self.throw_speed = distance/1151
        self.throw_angle = math.atan2(self.base_ball_target_y - self.base_ball_pos_y, self.base_ball_target_x - self.base_ball_pos_x)

    # 생성된 공 위치로 이동하는 애니메이션 진행
    def throw_ball_to_target_anim(self):
        angle = self.throw_angle
        distance = math.sqrt((self.base_ball_target_x - self.base_ball_pos_x) ** 2 + (
                    self.base_ball_target_y - self.base_ball_pos_y) ** 2)

        self.base_ball_pos_x += self.throw_speed * math.cos(angle)
        self.base_ball_pos_y += self.throw_speed * math.sin(angle)

        self.base_ball.pos[0] = int(self.base_ball_pos_x)
        self.base_ball.pos[1] = int(self.base_ball_pos_y)

        #self.temp += 1

        if self.base_ball.size[0] < 110:
            self.base_ball.size[0] += 1
            self.base_ball.size[1] += 1

        # 타켓 위치로 왔을 때 종료
        if distance < 5:
            self.is_throw_ball_to_target_anim = False
            return

    # 공의 박자와 Hit하는 순간을 체크하는 함수.
    def check_throw_event_by_hit(self):
        decrease_size = 0.1 # [능력치]에 따라 조정

        #self.throw_event_rate += 1

        # 공의 박자 offset은 계속 줄어듬
        size = self.throw_target_effect.size[0] - decrease_size
        self.throw_target_effect.size = [size, size]

        # 박자가 끝난 후에는 스트라이크 처리
        if(size < 75) :
            self.is_check_throw_event_by_hit = False
            self.throw_target_effect.bActive = False
            print('스트라이크!')
            return