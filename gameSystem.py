import math

from Define import *
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
        self.throw_target_end = None
        self.throw_target_effect = None
        self.base_ball = None

        # 타자 hit 변수
        self.is_hit = False
        self.is_hit_ball_to_target_anim = False
        self.hit_target_pos = [0, 0]
        self.hit_target_depth = 0

        # 공 박자 변수
        self.is_check_throw_event_by_hit = False
        self.throw_event_rate = 0
        self.throw_hit_offset = 0.0
        self.throw_power = THROW_POWER_MIDDLE  # [능력치]에 따라 조정 : 1 ~ 3 정수 형태로 나타냄

        # 야구공 초기위치와 타켓 위치
        self.is_throw_ball_to_target_anim = False
        self.base_ball_pos_x = 400
        self.base_ball_pos_y = 300
        self.base_ball_target_x = 0
        self.base_ball_target_y = 0
        self.throw_angle = 0
        self.throw_speed = 0

        # 클래스
        self.ui_manager = None

        self.temp = 0
        self.throw_event_rate = 0

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

    # 플레이어가 SPACE 키 눌러 hit 하면 안타/홈런/스트라이크 체크 함수.
    def check_hit(self):
        hit_try = self.throw_target_effect.size[0]
        offset = abs(HIT_EXACT_SIZE - hit_try)

        # system에서 설정한 범위 값대로 홈런/안타/뜬볼/스트라이크 체크
        # 홈런이나 안타 시 IS_HIT 변수 변경
        if offset <= HOME_RUN_MAX_OFFSET:
            self.is_hit = True
            print('홈런!')
        elif offset <= HIT_MAX_OFFSET:
            self.is_hit = True
            print('안타!')
        elif offset <= FLYING_HIT_MAX_OFFSET:
            self.is_hit = True
            print('뜬 볼')
        else:
            self.is_hit = False
            print('헛 스윙!')

    # hit 할 시, 야구공 랜덤으로 위치 설정. 설정된 변수 대로 scene_01, scene_02 진행
    def start_hit(self, is_flying, is_home_run):
        # 랜덤으로 이동 방향, 높이, 깊이 설정
        # scene_01에서 보여줄 위치
        self.hit_target_pos[0] = random.randint(HIT_DIR_MIN_X, HIT_DIR_MAX_X)
        self.hit_target_pos[1] = random.randint(HIT_DIR_MIN_Y, HIT_DIR_MAX_Y)
        # scene_02에서 보여줄 깊이
        self.hit_target_depth = random.randint(HIT_DEPTH_MIN, HIT_DEPTH_MAX)

        # 홈런 or 뜬 볼 시 높이는 최대로 고정
        if is_flying or is_home_run:
            self.hit_target_pos[1] = HIT_DIR_MAX_Y

        # 랜덤으로 설정된 위치로 scene_01에서 애니메이션 보여줌
        self.is_hit_ball_to_target_anim = True

    # scene_01, scene_02에서
    def hit_ball_to_target_anim(self):
        pass

    # 투수 AI 공 던지기
    def throw_ball(self):
        self.playerAI.throw_ball()

    def generate_random_throw_target(self):
        # 던진 공 위치는 게임 내 사각 박스 내에 랜덤으로 생성
        pos_x = random.randint(THROW_MIN_X, THROW_MAX_X)
        pos_y = random.randint(THROW_MIN_Y, THROW_MAX_Y)

        self.throw_target.pos = [pos_x, pos_y]
        self.throw_target_end.pos = [pos_x, pos_y]
        self.throw_target_end.bActive = False

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
        if (pos_x > 420):
            offset_x = 10
        elif (pos_x <= 390):
            offset_x = -10
        self.base_ball_target_x = pos_x + offset_x
        self.base_ball_target_y = pos_y + offset_y

        distance = math.sqrt((self.base_ball_target_x - self.base_ball_pos_x) ** 2 + (
                self.base_ball_target_y - self.base_ball_pos_y) ** 2)
        self.throw_speed = distance / int(((12510 / self.throw_power) * 0.1) - 100)
        self.throw_angle = math.atan2(self.base_ball_target_y - self.base_ball_pos_y,
                                      self.base_ball_target_x - self.base_ball_pos_x)

    # 생성된 공 위치로 이동하는 애니메이션 진행
    def throw_ball_to_target_anim(self):
        angle = self.throw_angle
        distance = math.sqrt((self.base_ball_target_x - self.base_ball_pos_x) ** 2 + (
                self.base_ball_target_y - self.base_ball_pos_y) ** 2)

        self.base_ball_pos_x += self.throw_speed * math.cos(angle)
        self.base_ball_pos_y += self.throw_speed * math.sin(angle)

        self.base_ball.pos[0] = int(self.base_ball_pos_x)
        self.base_ball.pos[1] = int(self.base_ball_pos_y)

        # self.temp += 1

        if self.base_ball.size[0] < 110:
            self.base_ball.size[0] += 1
            self.base_ball.size[1] += 1

        # 타켓 위치로 왔을 때 종료
        if distance < 5:
            self.is_throw_ball_to_target_anim = False
            return

    # 공의 박자와 Hit하는 순간을 체크하는 함수.
    def check_throw_event_by_hit(self):
        decrease_size = self.throw_power * 0.1

        # self.throw_event_rate += 1

        # 공의 박자 offset은 계속 줄어듬
        size = self.throw_target_effect.size[0] - decrease_size
        self.throw_target_effect.size = [size, size]

        # 타자가 hit 했는지 체크 해야 함!
        if self.is_hit:
            print("공 던지기 끝!")
            self.throw_target.bActive = False
            self.is_check_throw_event_by_hit = False
            self.throw_target_effect.bActive = False
            self.is_hit = False
            return

        # 박자가 끝난 후에는 관련 ui를 비활성 후 스트라이크/볼 체크 처리
        if (size < 75):
            # 타자가 hit 했는지 체크 해야 함!
            if self.is_hit:
                return

            self.throw_target.bActive = False
            self.is_check_throw_event_by_hit = False
            self.throw_target_effect.bActive = False

            self.ui_manager.start_fade(self.throw_target_end, 1, 3000)  # throw_target_end 보여줬다가 없애기
            self.check_throw_result()
            return

    # 포수가 공을 잡은 뒤 스트라이크/볼인지 체크하는 함수
    # 1) 스트라이크 존 안에 있으면 스트라이크 아니면 볼
    def check_throw_result(self):
        IS_STRIKE = False
        if (STRIKE_MIN_X < self.throw_target.pos[0] < STRIKE_MAX_X) and (
                STRIKE_MIN_Y < self.throw_target.pos[1] < STRIKE_MAX_Y):
            IS_STRIKE = True

        if IS_STRIKE:
            self.strike()
        else:
            self.ball()

    # 히트 시 안타/파울/스트라이크인지 체크하는 함수
    # 1) 히트 존 안에 있어야 함
    # 2) 히트 offset에 따라 안타/파울/스트라이크 판정
    def check_hit_result(self):
        pass

    # 스트라이크 판정 시 작동하는 함수
    def strike(self):
        strike_ui = self.ui_manager.find_ui(message_strike)

        self.ui_manager.start_fade(strike_ui, 100, 3000)  # 스트라이크 메세지 띄우기
        GameSystem.STRIKE += 1  # 스트라이크 횟수 증가

        # 스트라이크 아웃 체크
        self.check_strike_out()

    # 볼 판정 시 작동하는 함수
    def ball(self):
        ball_ui = self.ui_manager.find_ui(message_ball)

        self.ui_manager.start_fade(ball_ui, 100, 3000)  # 볼 메세지 띄우기
        GameSystem.BALL += 1  # 볼 횟수 증가

        # 볼 넷으로 1루 진출 체크
        self.check_ball_four()

    def check_strike_out(self):
        if GameSystem.STRIKE >= 3:
            GameSystem.OUT += 1  # 아웃 횟수 증가

            # 쓰리 아웃으로 공수 교대인지 체크

    def check_ball_four(self):
        if GameSystem.BALL >= 4:
            GameSystem.BALL = 0
            pass

    def check_three_out(self):
        if GameSystem.OUT >= 3:
            pass
