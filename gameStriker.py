import math

from gameObject import *
from gameStateMachine import StatMachine_Striker
from gameBehaviorTree import BehaviorTree, Action, Sequence, Condition, Selector
from gameTime import Time

'''
  <class Striker>
     - 전반적으로 게임 필요한 AI 역할
     - 2DGP 야구 게임 공격 역할
'''

# Striker Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Striker(GameObject):

    # 게임에서 활용될 Defender 클래스 초기화:
    def __init__(self, scene, name, pos, playMode, layer, bActive, frame):
        super().__init__(scene, name, pos, playMode.sprite_sheet, playMode.size, playMode.type, layer, bActive)
        self.frame = frame
        self.action = 0
        self.dir = 1.0
        self.play_mode = playMode
        self.play_anim = playMode.anim
        self.state_machine = StatMachine_Striker(self)
        self.max_frame = len(playMode.anim[self.action].posX)

        self.tx, self.ty = 1000, 1000

        self.game_system = None

        self.base = None
        self.base_ball = None
        self.base_posX, self.base_posY = 0.0, 0.0
        self.bt = None

        self.running = False

        # Base 리스트
        self.base_list = []

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
            # self.bt.run()
            pass

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

    def set_base_list(self, base_list):
        self.base_list = base_list

    def do_IDLE(self):
        # 아무것도 안하는 statemachine
        self.state_machine.handle_event(('Striker IDLE', 0))

        return BehaviorTree.SUCCESS

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < 0.001

    def move_slightly_to(self, tx, ty):
        self.angle = math.atan2(ty-self.pos[1], tx-self.pos[0])
        self.speed = RUN_SPEED_PPS
        self.pos[0] += self.speed * math.cos(self.angle) * Time.frame_time
        self.pos[1] += self.speed * math.sin(self.angle) * Time.frame_time

    def build_behavior_tree(self):
        a0 = Action('Do nothing', self.do_IDLE)

        root = SEL_actionORnoting = Selector('action or noting', a0)

        self.bt = BehaviorTree(root)