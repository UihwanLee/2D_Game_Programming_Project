import math

from gameObject import *
from gameStateMachine import StatMachine_Defender
from gameBehaviorTree import BehaviorTree, Action, Sequence, Condition, Selector
from gameTime import Time
from Define import *

'''
  <class Defender>
     - 전반적으로 게임 필요한 AI 역할
     - 2DGP 야구 게임 수비 역할
'''

# Defender Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# BASEBALL SPEED
THROW_SPEED_KMPH = 15.0  # Km / Hour
THROW_SPEED_MPM = (THROW_SPEED_KMPH * 1000.0 / 60.0)
THROW_SPEED_MPS = (THROW_SPEED_MPM / 60.0)
THROW_SPEED_PPS = (THROW_SPEED_KMPH * PIXEL_PER_METER)

class Defender(GameObject):

    # 게임에서 활용될 Defender 클래스 초기화:
    def __init__(self, scene, name, pos, playMode, layer, bActive, frame):
        super().__init__(scene, name, pos, playMode.sprite_sheet, playMode.size, playMode.type, layer, bActive)
        self.frame = frame
        self.action = 0
        self.dir = 1.0
        self.play_mode = playMode
        self.play_anim = playMode.anim
        self.state_machine = StatMachine_Defender(self)
        self.max_frame = len(playMode.anim[self.action].posX)

        self.tx, self.ty = 1000, 1000

        self.game_system = None

        self.base = None
        self.base_ball = None
        self.base_posX, self.base_posY = 0.0, 0.0
        self.bt = None

        # Base
        self.base_list = []
        self.own_base_idx = -1

        # 자기가 한 역할이 모두 수행됐는지 체크하는 변수
        # 다른 수비수에게 공을 던지면 자기의 할 일을 끝나는 것을 알리는 변수
        self.idx_receive_defender = 0
        self.is_throwing = False
        self.is_play_done = False
        self.having_ball = False

    def update(self):
        active = super().get_object_var('bActive')
        if not active:
            return

        # state_machine 업데이트
        self.state_machine.update()

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        # Time.frame_time으로 애니메이션 frame 간 delay 구현
        ACTION_PER_TIME = 1.0 / self.play_anim[self.action].delay[int(self.frame)]
        self.frame = (self.frame + ACTION_PER_TIME * Time.frame_time) % self.max_frame

        # BehaviorTree 작동
        if self.bt:
            self.bt.run()

    # 렌더링
    def render(self):
        active = super().get_object_var('bActive')
        if not active:
            return

        frame = int(self.frame)
        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        sizeX, sizeY = self.play_mode.size[0], self.play_mode.size[1]
        if self.dir == 1.0:
            sprite.clip_draw(frame * 100, self.action * 100, 100, 100, pos[0], pos[1], sizeX, sizeY)
        elif self.dir == -1.0:
            sprite.clip_composite_draw(frame * 100, self.action * 100, 100, 100, 0, 'h', pos[0], pos[1], sizeX, sizeY)

    def set_game_system(self, game_system):
        self.game_system = game_system

    def set_base_list(self, base_list):
        self.base_list = base_list

    def do_IDLE(self):
        # 아무것도 안하는 statemachine
        self.state_machine.handle_event(('Defender IDLE', 0))

        return BehaviorTree.SUCCESS

    # 홈런인지 아닌지 체크 홈런 일 시 아무런 행동을 취하지 않음
    def is_home_run(self):
        if self.game_system.is_home_run:
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS


    # Defender 중 공을 찾으러 갈 사람 찾기
    def is_baseball_nearby(self, r):

        # 자기의 할 일이 모두 끝나면 시행 안함
        if self.is_play_done:
            return BehaviorTree.FAIL

        # 던지는 중이면 넘어감
        if self.is_throwing:
            return BehaviorTree.SUCCESS

        # 거리 체크 후
        # 모든 defender 중 가장 가까운 defender만 SUCCESS 할 수 있도록 변경
        name = self.game_system.find_defender_shortest_distance_from_baseball()

        if self.name == name:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    # 떨어진 공 위치를 설정 해줌.
    def set_baseball_location(self, tx, ty):
        self.tx, self.ty = tx, ty
        return BehaviorTree.SUCCESS

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < 0.001

    def move_slightly_to(self, tx, ty):
        self.angle = math.atan2(ty-self.pos[1], tx-self.pos[0])
        self.speed = RUN_SPEED_PPS
        self.pos[0] += self.speed * math.cos(self.angle) * Time.frame_time
        self.pos[1] += self.speed * math.sin(self.angle) * Time.frame_time

    # 설정된 공 위치로 이동
    def move_to_baseball(self, r = 0.5):
        # 움직임에 따라 stateMachine 업데이트
        if self.pos[0] <= self.base_ball.pos[0]:
            self.state_machine.handle_event(('Defender Run Right', 0))
        else:
            self.state_machine.handle_event(('Defender Run Left', 0))

        # 던지는 중이면 넘어감
        if self.is_throwing:
            return BehaviorTree.SUCCESS

        # 이동
        self.move_slightly_to(self.base_ball.pos[0], self.base_ball.pos[1])
        if self.distance_less_than(self.base_ball.pos[0], self.base_ball.pos[1], self.pos[0], self.pos[1], r):
            self.base_ball.bActive = False
            self.having_ball = True
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    # 잡은 공을 상황에 따라 1루, 2루, 3루, 홈으로 던짐
    def find_defender_to_throw(self):
        # 1루수로 세팅
        self.state_machine.handle_event(('Defender Throw', 0))
        self.idx_receive_defender = self.game_system.find_defender_receive_baseball(self.pos)
        return self.idx_receive_defender

    def throw_slightly_to(self, tx, ty):
        self.angle = math.atan2(self.game_system.scene04.Defender_List[self.idx_receive_defender].pos[1]-self.base_ball.pos[1],
                                self.game_system.scene04.Defender_List[self.idx_receive_defender].pos[0]-self.base_ball.pos[0])
        self.speed = THROW_SPEED_PPS

        # base 이동
        self.base.pos[0] -= 1.0 * math.cos(self.angle)
        self.base.pos[1] -= 1.0 * math.sin(self.angle)

        # 야구공 이동
        self.base_ball.pos[0] += self.speed * math.cos(self.angle) * Time.frame_time
        self.base_ball.pos[1] += self.speed * math.sin(self.angle) * Time.frame_time

        # 씬 Defender 이동
        if self.base.pos[0] <= 600 and self.base.pos[0] >= 200:
            self.game_system.scene04.move_all_defender(-1.0 * math.cos(self.angle), (-1.0 * math.sin(self.angle)))
            self.game_system.scene04.move_all_striker(-1.0 * math.cos(self.angle), (-1.0 * math.sin(self.angle)))
        else:
            self.game_system.scene04.move_all_defender(0, (-1.0 * math.sin(self.angle)))
            self.game_system.scene04.move_all_striker(0, (-1.0 * math.sin(self.angle)))

    def throw_baseball_to_defender(self):
        # 이동
        self.is_throwing = True
        self.base_ball.bActive = True
        # self.having_ball = False
        self.throw_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.game_system.scene04.Defender_List[self.idx_receive_defender].pos[0],
                                   self.game_system.scene04.Defender_List[self.idx_receive_defender].pos[1],
                                   self.base_ball.pos[0], self.base_ball.pos[1], 0.5):
            self.throw_done = False

            # 공을 던진 후에는 자기에 할일이 모두 끝나는 것을 알림
            self.is_play_done = True
            self.is_throwing = False
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

        # return BehaviorTree.SUCCESS

    def is_base_defender(self):
        # 자기 위치가 아닐 때만 행동

        if self.name == Defender_name + '1':
            self.own_base_idx = 0
        elif self.name == Defender_name + '2':
            self.own_base_idx = 1
        elif self.name == Defender_name + '3':
            self.own_base_idx = 2

        if self.own_base_idx != -1:
            if self.distance_less_than(self.base_list[self.own_base_idx].pos[0], self.base_list[self.own_base_idx].pos[1], self.pos[0], self.pos[1], 0.5):
                return BehaviorTree.FAIL
            else:
                return BehaviorTree.SUCCESS

    def move_own_base(self):
        if self.own_base_idx == -1:
            return BehaviorTree.FAIL

        # 움직임에 따라 stateMachine 업데이트
        if self.pos[0] <= self.base_list[self.own_base_idx].pos[0]:
            self.state_machine.handle_event(('Defender Run Right', 0))
        else:
            self.state_machine.handle_event(('Defender Run Left', 0))

        # 이동
        self.move_slightly_to(self.base_list[self.own_base_idx].pos[0], self.base_list[self.own_base_idx].pos[1])
        if self.distance_less_than(self.base_list[self.own_base_idx].pos[0], self.base_list[self.own_base_idx].pos[1], self.pos[0], self.pos[1], 0.5):
            # 아웃인지 세이프인지 판단하고 scene 전환
            if self.having_ball:
                print('1루 도착')
                self.game_system.check_out_or_safe(self.own_base_idx)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING



    def build_behavior_tree(self):
        a0 = Action('Do nothing', self.do_IDLE)
        c1 = Condition('Check Hitter Home Run', self.is_home_run)
        c2 = Condition('Is baseball nearby', self.is_baseball_nearby, 10)
        a1 = Action('Set baseball location', self.set_baseball_location, self.base_ball.pos[0], self.base_ball.pos[1])
        a2 = Action('Move to baseball', self.move_to_baseball, 0.5)
        a3 = Action('Find receive Defender', self.find_defender_to_throw)
        a4 = Action('Throw baseball to Defender', self.throw_baseball_to_defender)


        SEQ_chase_baseball = Sequence('chase baseball', c1, c2, a1, a2, a3, a4)

        c3 = Condition('Is Base Defender', self.is_base_defender)
        a5 = Action('Move Own Base', self.move_own_base)

        SEQ_move_own_base = Sequence('move own base', c3, a5)

        root = SEL_actionORnoting = Selector('action or noting', SEQ_chase_baseball, SEQ_move_own_base, a0)

        self.bt = BehaviorTree(root)

