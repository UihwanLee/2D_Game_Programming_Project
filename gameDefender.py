from gameObject import *
from gameStateMachine import StatMachine_Defender
from gameTime import Time

'''
  <class Defender>
     - 전반적으로 게임 필요한 AI 역할
     - 2DGP 야구 게임 수비 역할
'''
class Defender(GameObject):

    # 게임에서 활용될 GamePlayerAI 클래스 초기화:
    def __init__(self, scene, name, pos, playMode, layer, bActive, frame):
        super().__init__(scene, name, pos, playMode.sprite_sheet, playMode.size, playMode.type, layer, bActive)
        self.frame = frame
        self.action = 0
        self.play_mode = playMode
        self.play_anim = playMode.anim
        self.state_machine = StatMachine_Defender(self)
        self.max_frame = len(playMode.anim[self.action].posX)

        self.game_system = None

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