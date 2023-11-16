import math

from gameObject import *
from gameStateMachine import StatMachine_Defender
from gameBehaviorTree import BehaviorTree, Action, Sequence, Condition, Selector
from gameTime import Time

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

class Defender(GameObject):

    # 게임에서 활용될 Defender 클래스 초기화:
    def __init__(self, scene, name, pos, playMode, layer, bActive, frame):
        super().__init__(scene, name, pos, playMode.sprite_sheet, playMode.size, playMode.type, layer, bActive)
        self.frame = frame
        self.action = 0
        self.play_mode = playMode
        self.play_anim = playMode.anim
        self.state_machine = StatMachine_Defender(self)
        self.max_frame = len(playMode.anim[self.action].posX)

        self.game_system = None

        self.tx, self.ty = 1000, 1000

        self.game_system = None

        self.base_posX, self.base_posY = 0.0, 0.0
        self.bt = None
        self.build_behavior_tree()

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

        if self.game_system:
            self.base_posX = self.game_system.base_ball_base.pos[0]
            self.base_posY = self.game_system.base_ball_base.pos[1]

    # 렌더링
    def render(self):
        active = super().get_object_var('bActive')
        if not active:
            return

        frame = int(self.frame)
        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        sizeX, sizeY = self.play_mode.size[0], self.play_mode.size[1]
        sprite.clip_draw(frame * 100, self.action * 100, 100, 100, pos[0], pos[1], sizeX, sizeY)

    def set_game_system(self, game_system):
        self.game_system = game_system

    def do_IDLE(self):
        # 아무것도 안하는 statemachine
        pass

    # 홈런인지 아닌지 체크 홈런 일 시 아무런 행동을 취하지 않음
    def is_home_run(self):
        pass


    # Defender 중 공을 찾으러 갈 사람 찾기
    def is_baseball_nearby(self, r):
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
        return distance2 < (r * PIXEL_PER_METER) ** 2

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty-self.pos[1], tx-self.pos[0])
        self.speed = RUN_SPEED_PPS
        self.pos[0] += self.speed * math.cos(self.dir) * Time.frame_time
        self.pos[1] += self.speed * math.sin(self.dir) * Time.frame_time

    # 설정된 공 위치로 이동
    def move_to_baseball(self, r = 0.5):
        # 움직임에 따라 stateMachine 업데이트

        # 이동
        self.move_slightly_to(self.base_posX, self.base_posY)
        if self.distance_less_than(self.base_posX, self.base_posY, self.pos[0], self.pos[1], r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        c1 = Condition('Is baseball nearby', self.is_baseball_nearby, 10)
        a1 = Action('Find chase defender', self.set_baseball_location, self.base_posX, self.base_posY)
        a2 = Action('Move to baseball', self.move_to_baseball, 0.5)

        a3 = Action('Do nothing', self.do_IDLE)

        SEQ_chase_baseball = Sequence('chase baseball', c1, a1, a2)
        root = SEL_actionORnoting = Selector('action or noting', SEQ_chase_baseball, a3)

        self.bt = BehaviorTree(root)

