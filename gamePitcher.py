from Define import se_throw_name
from gameObject import GameObject
from gameStateMachine import StateMachine_Pitcher
from gameTime import Time
import random

'''
    2DGP 야구 게임에서 활용될 Pitcher.
     - Player와 대비되는 역할 수행
      ex) player-> 투수 / ai -> 타자

'''


class Pitcher(GameObject):

    # 게임에서 활용될 GamePlayerAI 클래스 초기화:
    def __init__(self, scene, name, playMode, layer, bActive, frame):
        super().__init__(scene, name, playMode.pos, playMode.sprite_sheet, playMode.size, playMode.type, layer, bActive,None, None)
        self.frame = frame
        self.action = 0
        self.play_mode = playMode
        self.play_anim = playMode.anim
        self.state_machine = StateMachine_Pitcher(self)
        self.max_frame = len(playMode.anim[self.action].posX)

        self.game_system = None

        self.cool_time = 3.0
        self.remain_cool_time = self.cool_time
        self.isCoolTimeExpired = False

    def try_throw_ball(self, sound_manager):
        can_throw = self.isCoolTimeExpired

        if can_throw:
            self.throw_ball(sound_manager)

    def throw_ball(self, sound_manager):
        sound_manager.playSE(se_throw_name, 100)
        self.state_machine.handle_event(('THROW', 0))
        self.reset_cooltime()

    def update(self):
        active = super().get_object_var('bActive')
        if not active:
            return

        # playerAI state_machine 업데이트
        self.state_machine.update()

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        # Time.frame_time으로 애니메이션 frame 간 delay 구현
        ACTION_PER_TIME = 1.0 / self.play_anim[self.action].delay[int(self.frame)]
        self.frame = (self.frame + ACTION_PER_TIME * Time.frame_time) % self.max_frame

        # throw 쿨타임
        self.remain_cool_time -= Time.frame_time
        if self.remain_cool_time < 0.0:
            self.isCoolTimeExpired = True
            self.game_system.set_active_throw_ui(1.0)
        else:
            self.isCoolTimeExpired = False
            self.game_system.set_active_throw_ui(0.5)

    # playerAI 렌더링. play_Anim 리스트를 기준으로 렌더링 한다.
    def render(self):
        active = super().get_object_var('bActive')
        if not active:
            return

        frame = int(self.frame)
        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        sizeX, sizeY = self.play_mode.size[0], self.play_mode.size[1]
        sprite.clip_draw(frame * 100, self.action * 100, 100, 100, pos[0], pos[1], sizeX, sizeY)

    # 투수 AI가 공을 던지면 throw_event 시작
    def start_throw_event(self):
        if self.game_system:
            # 공 위치 생성
            self.game_system.generate_random_throw_target()

            # 공 애니메이션 시작

    def reset_cooltime(self):
        self.remain_cool_time = self.cool_time