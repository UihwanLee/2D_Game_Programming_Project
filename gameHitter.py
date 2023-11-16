from sdl2 import SDL_KEYDOWN, SDLK_s

from gameObject import *
from gameStateMachine import StateMachine_Hitter
from gameTime import Time

'''
    Hitter 클래스 : GameObject 상속
    
    2DGP 야구 게임 사용자가 플레이 할 Hitter.
    
'''


class Hitter(GameObject):

    # Player 클래스 초기화. 상속 받은 GameObject 클래스 초기화.
    # player의 playMode를 통해 GameObject, play_Anim 등을 초기화 한다.
    # player StateMachine을 받아 처리할 수 있도록 한다.
    def __init__(self, scene, name, playMode, layer, bActive, frame):
        super().__init__(scene, name, playMode.pos, playMode.sprite_sheet, playMode.size, playMode.type, layer, bActive)
        self.play_mode = playMode
        self.play_anim = playMode.anim
        self.frame = frame
        self.action = 0
        self.state_machine = StateMachine_Hitter(self)
        self.max_frame = len(playMode.anim[self.action].posX)

        self.game_system = None

    # player 이벤트 처리 함수. 이벤트에 따른 애니메이션/동작을 StateMachine을 통해 처리한다.
    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

        # 임시
        if self.game_system:
            if event.type == SDL_KEYDOWN and event.key == SDLK_s:
                self.game_system.throw_ball()


    # player 업데이트. time 변수를 기준으로 각족 이벤트를 처리한다.
    def update(self):
        # player가 활성화 할 때만 시행
        active = super().get_object_var('bActive')
        if not active:
            return

        # player state_machine 업데이트
        self.state_machine.update()

        # 애니메이션의 다이나믹을 위해 delay : delay 함수를 호출하면 Frame이 떨어지므로 time으로 구현
        # Time.frame_time으로 애니메이션 frame 간 delay 구현
        ACTION_PER_TIME = 1.0 / self.play_anim[self.action].delay[int(self.frame)]
        self.frame = (self.frame + ACTION_PER_TIME * Time.frame_time) % self.max_frame

    # player 렌더링. player_Anim 리스트를 기준으로 렌더링 한다.
    def render(self):
        active = super().get_object_var('bActive')
        if not active:
            return

        frame = int(self.frame)
        pos = super().get_object_var('pos')
        sprite = super().get_object_var('sprite')
        posX, posY = self.play_anim[self.action].posX[frame], self.play_anim[self.action].posY[frame]
        sizeX, sizeY = self.play_mode.size[0], self.play_mode.size[1]
        sprite.clip_draw(frame * 100, self.action * 100, 100, 100, posX, posY, sizeX, sizeY)
