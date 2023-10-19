from pico2d import SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE

'''

    2DGP 야구 게임에서 객체의 StateMachine을 관리하는 모듈
    애니메이션이나 시스템이 적용될 객체는 다음과 같다.

    1) Player
    2) SystemPlayer
    3) GamePlayerAI
    4) GameSystemAI

    이벤트 처리를 받아 동작하는 부분은 GameSystem 안에서 해결할 수 있도록 한다.

'''

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

''' Player StateMachine '''

class Idle:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.action = 0

    @staticmethod
    def exit(player, e):
        pass

class Hit:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.action = 1

    @staticmethod
    def exit(player, e):
        pass

class StateMachine_Player:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transitions = {
            Idle : {space_down: Hit}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        pass

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False