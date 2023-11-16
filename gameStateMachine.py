from pico2d import SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, get_time

'''

    2DGP 야구 게임에서 객체의 StateMachine을 관리하는 모듈
    애니메이션이나 시스템이 적용될 객체는 다음과 같다.

    1) Hitter
    2) Pitcher
    3) Defender
    4) GameSystemAI

    이벤트 처리를 받아 동작하는 부분은 GameSystem 안에서 해결할 수 있도록 한다.

'''


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'

def AI_throw(e):
    return e[0] == 'THROW'

def defender_throw(e):
    return e[0] == 'Defender Throw'


''' Player StateMachine '''


class Idle_Hitter:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.action = 0
        player.time = 0
        player.max_frame = len(player.play_mode.anim[player.action].posX)  # max_frame 수정

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def exit(player, e):
        pass


class Idle_Pitcher:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.action = 0
        player.time = 0
        player.max_frame = len(player.play_mode.anim[player.action].posX)  # max_frame 수정

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def exit(player, e):
        pass


class Hit:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.action = 1
        player.time = 0
        player.max_frame = len(player.play_mode.anim[player.action].posX)  # max_frame 수정
        player.start_time = get_time()

        # system hit offset
        player.game_system.check_hit()

    @staticmethod
    def do(player):
        # Hit 애니메이션 끝난 이벤트를 시간으로 체크하여 Idle로 돌아가기
        #  get_time() - player.start_time > 0.8:
        if get_time() - player.start_time > player.play_anim[player.action].total_delay:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def exit(player, e):
        pass

class Throw:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.action = 1
        player.time = 0
        player.max_frame = len(player.play_mode.anim[player.action].posX)  # max_frame 수정
        player.start_time = get_time()
        player.throw_event = False

    @staticmethod
    def do(player):
        # Throw 애니메이션 끝난 이벤트를 시간으로 체크하여 Idle로 돌아가기
        if get_time() - player.start_time > player.play_anim[player.action].total_delay:
            player.state_machine.handle_event(('TIME_OUT', 0))

        # 던진 특정 순간 공 위치 생성 : 투수가 playerAI 기준
        if get_time() - player.start_time > sum(player.play_anim[player.action].delay[:6]):
            if player.throw_event == False:
                player.start_throw_event()
                player.throw_event = True


    @staticmethod
    def exit(player, e):
        pass


class StateMachine_Hitter:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle_Hitter
        self.transitions = {
            Idle_Hitter: {space_down: Hit},
            Hit: {time_out: Idle_Hitter}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True

        return False

class StateMachine_Pitcher:
    def __init__(self, player_AI):
        self.playerAI = player_AI
        self.cur_state = Idle_Pitcher
        self.transitions = {
            Idle_Pitcher: {AI_throw: Throw},
            Throw: {time_out: Idle_Pitcher}
        }

    def start(self):
        self.cur_state.enter(self.playerAI, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.playerAI)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.playerAI, e)
                self.cur_state = next_state
                self.cur_state.enter(self.playerAI, e)
                return True

        return False

class Idle_Defender:
    @staticmethod
    def enter(defender, e):
        defender.frame = 0
        defender.action = 0
        defender.time = 0
        defender.max_frame = len(defender.play_mode.anim[defender.action].posX)  # max_frame 수정

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def exit(player, e):
        pass

class Throw_Defender:
    @staticmethod
    def enter(defender, e):
        defender.frame = 0
        defender.action = 0
        defender.time = 0
        defender.max_frame = len(defender.play_mode.anim[defender.action].posX)  # max_frame 수정

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def exit(player, e):
        pass

class StatMachine_Defender:
    def __init__(self, defender):
        self.defender = defender
        self.cur_state = Idle_Defender
        self.transitions = {
            Idle_Defender: { }
        }

    def start(self):
        self.cur_state.enter(self.defender, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.defender)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.defender, e)
                self.cur_state = next_state
                self.cur_state.enter(self.defender, e)
                return True

        return False