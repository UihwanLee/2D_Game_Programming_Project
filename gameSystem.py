import math

from Define import *
from gamePitcher import *
from Define import BOTTOM
import random

'''
    2DGP 게임에서 야구 시스템을 동작하는 클래스
    
    다음과 같은 기능을 수행 한다.
    
    야구 게임 시스템 관리.
    
    투수 AI 던지는 경로 지정.
    투수 AI 던지는 경로 대로 base_ball 위치 이동
    투수 AI 가 던질 시 hit 검사
    
    타자 홈런/안타/뜬 볼/스트라이크 체크
    
    [타자 홈런/안타/뜬 볼/스트라이크 체크 알고리즘]
    1) 투수가 공을 던지면 공의 던져질 target이 표시되고 이 target 중심으로 원 고리의 크기가 점점 줄어든다.
    2) 타자가 SPACE키를 누르면 방망이를 휘두르는데 이때 줄어든 원 고리 크기와 target 원의 크기 offset을 구한다.
    3) Define.py에서 정한 (홈런/안타/스트라이크) 범위에 맞는 offset을 판단한다.
    4) hit시(홈런/안타) scene_04로 넘어 가며 애니메이션이 진행되고 아니면 스트라이크 처리 
    
    투수 스트라이크/볼/스트라이크 아웃 체크
    
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
        self.is_home_run = False
        self.is_hit = False
        self.is_hit_anim = False
        self.is_hit_anim2 = False
        self.hit_target_pos = [0, 0]
        self.hit_target_depth = 0
        self.hit_angle = 0

        # 공 박자 변수
        self.is_throw_Done = False
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

        # scene_04 글로벌 변수

        # base
        self.base = None
        self.base_camera_target_x = 0
        self.base_camera_target_y = 0
        self.base_camera_angle = 0
        self.camera_pos_x = 0.0
        self.camera_pos_y = 0.0
        self.camera_dir = 1.0

        # 야구공
        self.base_ball_base = None
        self.base_ball_base_speed = 0.5
        self.base_ball_base_target_x = 0.0
        self.base_ball_base_target_y = 0.0
        self.base_ball_base_angle = 0.0
        self.base_ball_base_dir = 1.0

        # Defender move_offset
        self.defender_move_offset = [0.0, 0.0]

        # 스트라이크, 볼, 아웃 전등
        self.ui_strike = []
        self.ui_ball = []
        self.ui_out = []

        # 타자 hit 시 판단 변수
        self.home_run_max_offset = 3.0
        self.hit_max_offset = 50

        # 클래스
        self.game_engine = None
        self.ui_manager = None

        self.scene03 = None
        self.scene04 = None

        self.temp = 0
        self.throw_event_rate = 0

    # GameSystem update 함수 특정 이벤트를 검사하는 일을 수행한다.
    # 타자가 방망이를 휘둘렸는지, 그 결과가 어떤지 처리
    # 투수가 공 던지는 애니메이션 수행
    # 타자 공 히트해서 공 날아가는 애니메이션 수행
    def update(self):
        if self.is_check_throw_event_by_hit:
            self.check_throw_event_by_hit()

        if self.is_throw_ball_to_target_anim:
            self.throw_ball_to_target_anim()

        if self.is_hit_anim:
            self.hit_ball_to_target_anim()

        if self.is_hit_anim2:
            self.hit_ball_to_target_anim_in_base()

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

    # 투수가 던지고 나서 안타/홀런/스트라이크 됐을 때 변수 초기화
    def reset_throw(self):
        self.base_ball.bActive = False
        self.throw_target_effect.size = [200, 200]
        self.throw_event_rate = 0
        self.throw_hit_offset = 0.0

        self.is_throw_Done = False
        self.is_hit_anim = False
        self.is_hit_anim2 = False

        self.home_run_max_offset = 3.0

        if self.scene03.cover.bActive:
            self.scene03.cover.bActive = False


    # Player 공/수 선택 공->타자 / 수->투수로 시스템 설정 하기
    def SetPlayMode(self):
        pass

    # 플레이어가 SPACE 키 눌러 hit 하면 안타/홈런/스트라이크 체크 함수.
    def check_hit(self):
        hit_try = self.throw_target_effect.size[0]
        offset = abs(HIT_EXACT_SIZE - hit_try)

        # 투수가 이미 던져서 스트라이크/볼 처리 된 경우 예외처리
        if self.is_throw_Done:
            return

        # system에서 설정한 범위 값대로 홈런/안타/뜬볼/스트라이크 체크
        # 홈런이나 안타 시 IS_HIT 변수 변경
        if offset <= self.home_run_max_offset:
            self.is_hit = True
            self.is_home_run = True
            print('홈런!')
        elif offset <= self.hit_max_offset:
            self.is_hit = True
            print('안타!')
        else:
            self.is_hit = False
            print('헛 스윙!')

    def do_home_run(self):
        # 투수가 이미 던져서 스트라이크/볼 처리 된 경우 예외처리
        if self.is_throw_Done:
            return

        self.start_hit(False, True)

    def do_hit(self):
        # 투수가 이미 던져서 스트라이크/볼 처리 된 경우 예외처리
        if self.is_throw_Done:
            return
        self.start_hit(False, False)

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

        # 야구공 중앙 배치
        self.base_ball_pos_x = 400
        self.base_ball_pos_y = 150

        self.hit_angle = math.atan2(self.hit_target_pos[1] - self.base_ball_pos_y, self.hit_target_pos[0] - self.base_ball_pos_x)
        self.is_hit_anim = True

    def hit_ball_to_target_anim(self):
        hit_speed = 1.0
        angle = self.hit_angle

        distance = math.sqrt(
            (self.hit_target_pos[0] - self.base_ball_pos_x) ** 2 + (self.hit_target_pos[1] - self.base_ball_pos_y) ** 2)

        self.base_ball_pos_x += hit_speed * math.cos(angle)
        self.base_ball_pos_y += hit_speed * math.sin(angle)

        self.base_ball.pos[0] = int(self.base_ball_pos_x)
        self.base_ball.pos[1] = int(self.base_ball_pos_y)

        if self.base_ball.size[0] < 110:
            self.base_ball.size[0] += 1.0 * Time.frame_rate
            self.base_ball.size[1] += 1.0 * Time.frame_rate

        # 타켓 위치로 왔을 때 종료
        # scene_04로 change
        if distance < 5:
            self.is_hit_anim = False
            self.set_hit_ball_to_target_anim_in_base()
            self.game_engine.change_scene(SCENE_04)
            return

    def set_hit_ball_to_target_anim_in_base(self):
        self.is_hit_anim2 = True

        # 야구공 세트
        self.base_ball_base_speed = 0.5
        self.base_ball_base.size[0] = 50
        self.base_ball_base.size[1] = 50
        self.base_ball_base.pos[0] = 400
        self.base_ball_base.pos[1] = 70

        # 선형 보간으로 base_ball x 위치 구하기 (100 ~ 400 : 오른쪽, 400 ~ 700 : 왼쪽)
        self.base_ball_target_x = CAMERA_DIR_MIN_X - ((self.hit_target_pos[0] - HIT_DIR_MIN_X) / (HIT_DIR_MAX_X - HIT_DIR_MIN_X)) * (CAMERA_DIR_MIN_X - CAMERA_DIR_MAX_X)
        self.base_ball_target_y = 400
        self.base_ball_base_angle = math.atan2(self.base_ball_target_y - self.base_ball_base.pos[1], self.base_ball_target_x - self.base_ball_base.pos[0])

        # 카메라
        self.camera_pos_x = 400.0
        self.camera_pos_y = 600.0
        self.base_camera_target_x = 600

        # 카메라 깊이
        self.base_camera_target_y = random.randint(CAMERA_DEPTH_MAX, CAMERA_DEPTH_MIN)        # (MAX : -100 ~ MIN : 350)

        # defender 위치 초기화
        self.scene04.reset_all_defender()

        # striker 정리
        self.scene04.reset_all_striker()

        # 홈런 -> depth: -100 고정, base_ball speed: 0.8
        # 그 외 -> depth: (-100 ~ 350), base_ball speed: 0.5
        if self.is_home_run:
            self.scene04.cover.bActive = True
            self.base_camera_target_y = -100
            self.base_ball_base_speed = 0.8

        self.base_camera_angle = math.atan2(background_base_02_pos[1] - self.base_camera_target_y,
                                            self.base_camera_target_x - background_base_02_pos[0])

    # scene_04에서 공이 홈런/안타/뜬볼 처리 애니메이션
    def hit_ball_to_target_anim_in_base(self):
        # 설정된 hit_target_pos에 따라 base_ball_base, camera 이동
        camera_speed = 1.0
        angle = self.base_ball_base_angle

        distance = math.sqrt(
            (self.base_camera_target_x - self.camera_pos_x) ** 2 + (self.base_camera_target_y - self.camera_pos_y) ** 2)

        # 타켓 위치로 왔을 때 종료
        # scene_02로 change
        if distance < 5.0 or (self.base_camera_target_y - self.camera_pos_y) ** 2 < 5:
            self.is_hit_anim2 = False
            # 홈런이면 홈런 표시하고 넘어가기

            # 안타 / 아웃은 수비 선수들의 움직임으로 판단하여 구현

            # 변수 초기화
            # self.reset_throw()

            # 씬 변경
            # self.game_engine.change_scene(SCENE_03)
            return

        self.camera_pos_x += 1.0 * math.cos(angle)
        self.camera_pos_y -= 1.0 * math.sin(angle)

        self.base_ball_base.pos[0] -= self.base_ball_base_speed * math.cos(angle)
        self.base_ball_base.pos[1] += self.base_ball_base_speed * math.sin(angle)

        # scene04에 있는 모든 오브젝트 위치 갱신
        if self.camera_pos_x <= 600 and self.camera_pos_x >= 200:
            self.scene04.move_all_defender(math.cos(angle), (-1.0 * math.sin(angle)))
            self.scene04.move_all_striker(math.cos(angle), (-1.0 * math.sin(angle)))
            self.defender_move_offset[0] += math.cos(angle)
            self.defender_move_offset[1] += -1.0 * math.sin(angle)
        else:
            self.scene04.move_all_defender(0, (-1.0 * math.sin(angle)))
            self.scene04.move_all_striker(0, (-1.0 * math.sin(angle)))
            self.defender_move_offset[1] += -1.0 * math.sin(angle)

        if self.camera_pos_x > 600:
            self.camera_pos_x = 600
        elif self.camera_pos_x < 200:
            self.camera_pos_x = 200

        self.base.pos[0] = int(self.camera_pos_x)
        self.base.pos[1] = int(self.camera_pos_y)

        if self.base.pos[1] < -100:
            self.base.pos[1] = -100

    # 투수 AI 공 던지기
    def throw_ball(self):
        self.playerAI.throw_ball()

    def generate_random_throw_target(self):
        # hit 변수 초기회
        self.is_hit = False
        self.is_throw_Done = False

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

        # 타자가 hit 했는지 체크 해야 함!
        if self.is_hit:
            self.is_throw_ball_to_target_anim = False
            return

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
            self.throw_target.bActive = False
            self.is_check_throw_event_by_hit = False
            self.throw_target_effect.bActive = False
            self.is_hit_ball_to_target_anim = False
            return

        # 박자가 끝난 후에는 관련 ui를 비활성 후 스트라이크/볼 체크 처리
        if (size < 75):
            # 타자가 hit 했는지 체크 해야 함!
            if self.is_hit:
                return

            self.is_throw_Done = True
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

        # if GameSystem.STRIKE < 2:
        #     for idx in range(0, GameSystem.STRIKE+1):
        #         print(UI_LIGHT_POS_X[idx])
        #         # 스트라이크 전등 추가
        #         self.ui_strike[idx].pos[0] = UI_LIGHT_POS_X[idx]
        #         self.ui_strike[idx].pos[1] = 520
        #         self.ui_strike[idx].bActive = True

        GameSystem.STRIKE += 1  # 스트라이크 횟수 증가

        # 스트라이크 아웃 체크
        self.check_strike_out()

    # 볼 판정 시 작동하는 함수
    def ball(self):
        ball_ui = self.ui_manager.find_ui(message_ball)

        # if GameSystem.BALL < 3:
        #     self.ui_ball[GameSystem.BALL].pos[0] = UI_LIGHT_POS_X[GameSystem.BALL]
        #     self.ui_ball[GameSystem.BALL].pos[1] = 500
        #     self.ui_ball[GameSystem.BALL].bActive = True

        self.ui_manager.start_fade(ball_ui, 100, 3000)  # 볼 메세지 띄우기
        GameSystem.BALL += 1  # 볼 횟수 증가

        # 볼 넷으로 1루 진출 체크
        self.check_ball_four()

    def check_strike_out(self):
        if GameSystem.STRIKE >= 3:
            GameSystem.STRIKE = 0
            GameSystem.OUT += 1  # 아웃 횟수 증가

            # if GameSystem.OUT < 2:
            #     self.ui_out[GameSystem.OUT].pos[0] = UI_LIGHT_POS_X[GameSystem.OUT]
            #     self.ui_out[GameSystem.OUT].pos[1] = 480
            #     self.ui_out[GameSystem.OUT].bActive = True

            # 스트라이크 / 볼 모두 비활성화
            #for strike in self.ui_strike: strike.bActvie = False
            #for ball in self.ui_ball: ball.bActvie = False

            # 쓰리 아웃으로 공수 교대인지 체크
            if GameSystem.OUT >= 3:
                GameSystem.BALL = 0
                GameSystem.OUT = 0
                # 스트라이크 / 볼 / 아웃 모두 비활성화
                #for strike in self.ui_strike: strike.bActvie = False
                #for ball in self.ui_ball: ball.bActvie = False
                #for out in self.ui_out: out.bActvie = False

    def check_ball_four(self):
        if GameSystem.BALL >= 4:
            GameSystem.BALL = 0
            GameSystem.STRIKE = 0
            # 스트라이크 / 볼 모두 비활성화
            #for strike in self.ui_strike: strike.bActvie = False
            #for ball in self.ui_ball: ball.bActvie = False
            pass

    def check_three_out(self):
        if GameSystem.OUT >= 3:
            pass


    # Defender 중 BaseBall과의 거리가 가장 짧은 Defender 이름 반환
    def find_defender_shortest_distance_from_baseball(self):
        cur_name = ""
        cur_dist = 100000000
        for defender in self.scene04.Defender_List:
            posX = defender.pos[0]
            posY = defender.pos[1]

            distance2 = (self.base_ball_base.pos[0] - posX) ** 2 + (self.base_ball_base.pos[1] - posY) ** 2
            if cur_dist > distance2:
                cur_dist = distance2
                cur_name = defender.name

        return cur_name

    # Defender 중 야구공 받을 Defender 찾아서 위치 반환
    def find_defender_receive_baseball(self, cur_pos):
        # striker 수 세기
        num = 0
        for striker in self.scene04.Striker_List:
            if striker.bActive:
                num += 1

        if num == 1:
            return 1
        elif num == 2:
            # 가장 가까운 base 부터 던짐
            return 2
        elif num == 3:
            return 3

        return 1
