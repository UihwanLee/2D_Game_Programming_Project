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
    return e[0] == 'SPACE_DOWN'

def skill_on(e):
    return e[0] == 'SKILL'

def home_run(e):
    return e[0] == 'HOME_RUN'

def time_out(e):
    return e[0] == 'TIME_OUT'

def AI_throw(e):
    return e[0] == 'THROW'

def defender_throw(e):
    return e[0] == 'Defender Throw'

def defender_idle(e):
    return e[0] == 'Defender IDLE'

def defender_run_right(e):
    return e[0] == 'Defender Run Right'

def defender_run_left(e):
    return e[0] == 'Defender Run Left'

def defender_throw(e):
    return e[0] == 'Defender Throw'


''' Player StateMachine '''


class Idle_Hitter:
    @staticmethod
    def enter(hitter, e):
        hitter.frame = 0
        hitter.action = 0
        hitter.time = 0
        hitter.max_frame = len(hitter.play_mode.anim[hitter.action].posX)  # max_frame 수정

    @staticmethod
    def do(hitter):
        pass

    @staticmethod
    def exit(hitter, e):
        pass


class Skill_Hitter:
    @staticmethod
    def enter(hitter, e):
        hitter.frame = 0
        hitter.action = 3
        hitter.time = 0
        hitter.max_frame = len(hitter.play_mode.anim[hitter.action].posX)  # max_frame 수정

    @staticmethod
    def do(hitter):
        pass

    @staticmethod
    def exit(hitter, e):
        pass


class Idle_Pitcher:
    @staticmethod
    def enter(hitter, e):
        hitter.frame = 0
        hitter.action = 0
        hitter.time = 0
        hitter.max_frame = len(hitter.play_mode.anim[hitter.action].posX)  # max_frame 수정

    @staticmethod
    def do(hitter):
        pass

    @staticmethod
    def exit(hitter, e):
        pass


class Hit:
    @staticmethod
    def enter(hitter, e):
        hitter.frame = 0
        hitter.action = 1
        hitter.time = 0
        hitter.max_frame = len(hitter.play_mode.anim[hitter.action].posX)  # max_frame 수정
        hitter.start_time = get_time()

    @staticmethod
    def do(hitter):
        # Hit 애니메이션 끝난 이벤트를 시간으로 체크하여 Idle로 돌아가기
        #  get_time() - player.start_time > 0.8:
        if get_time() - hitter.start_time > hitter.play_anim[hitter.action].total_delay:
            hitter.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def exit(player, e):
        pass

class Homr_Run:
    @staticmethod
    def enter(hitter, e):
        hitter.frame = 0
        hitter.action = 2
        hitter.time = 0
        hitter.max_frame = len(hitter.play_mode.anim[hitter.action].posX)  # max_frame 수정
        hitter.start_time = get_time()

    @staticmethod
    def do(hitter):
        # HOME_RUN 이펙트가 끝나고 홈런 진행
        if get_time() - hitter.start_time > hitter.play_anim[hitter.action].total_delay:
            hitter.state_machine.handle_event(('TIME_OUT', 0))
            hitter.game_system.ui_manager.is_effect_home_run = False
            hitter.game_system.ui_manager.start_show_home_run_message(hitter.game_system.scene04.home_run_msg)
            hitter.game_system.do_home_run()


    @staticmethod
    def exit(hitter, e):
        pass

class Throw:
    @staticmethod
    def enter(pitcher, e):
        pitcher.frame = 0
        pitcher.action = 1
        pitcher.time = 0
        pitcher.max_frame = len(pitcher.play_mode.anim[pitcher.action].posX)  # max_frame 수정
        pitcher.start_time = get_time()
        pitcher.throw_event = False

    @staticmethod
    def do(pitcher):
        # Throw 애니메이션 끝난 이벤트를 시간으로 체크하여 Idle로 돌아가기
        if get_time() - pitcher.start_time > pitcher.play_anim[pitcher.action].total_delay:
            pitcher.state_machine.handle_event(('TIME_OUT', 0))

        # 던진 특정 순간 공 위치 생성 : 투수가 playerAI 기준
        if get_time() - pitcher.start_time > sum(pitcher.play_anim[pitcher.action].delay[:6]):
            if pitcher.throw_event == False:
                pitcher.start_throw_event()
                pitcher.throw_event = True


    @staticmethod
    def exit(pitcher, e):
        pass


class StateMachine_Hitter:
    def __init__(self, hitter):
        self.hitter = hitter
        self.cur_state = Idle_Hitter
        self.transitions = {
            Idle_Hitter: {space_down: Hit, skill_on:Skill_Hitter, home_run: Homr_Run},
            Hit: {time_out: Idle_Hitter},
            Skill_Hitter: {space_down: Hit, home_run: Homr_Run},
            Homr_Run: {time_out: Idle_Hitter}
        }

    def start(self):
        self.cur_state.enter(self.hitter, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.hitter)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.hitter, e)
                self.cur_state = next_state
                self.cur_state.enter(self.hitter, e)
                return True

        return False

class StateMachine_Pitcher:
    def __init__(self, pitcher):
        self.pitcher = pitcher
        self.cur_state = Idle_Pitcher
        self.transitions = {
            Idle_Pitcher: {AI_throw: Throw},
            Throw: {time_out: Idle_Pitcher}
        }

    def start(self):
        self.cur_state.enter(self.pitcher, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pitcher)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pitcher, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pitcher, e)
                return True

        return False

class Idle_Defender:
    @staticmethod
    def enter(defender, e):
        defender.dir = 1.0
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

class RunRight_Defender:
    @staticmethod
    def enter(defender, e):
        defender.dir = 1.0
        defender.frame = 0
        defender.action = 2
        defender.time = 0
        defender.max_frame = len(defender.play_mode.anim[defender.action].posX)  # max_frame 수정

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def exit(player, e):
        pass

class RunLeft_Defender:
    @staticmethod
    def enter(defender, e):
        defender.dir = -1.0
        defender.frame = 0
        defender.action = 2
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
        defender.action = 3
        defender.time = 0
        defender.max_frame = len(defender.play_mode.anim[defender.action].posX)  # max_frame 수정
        defender.start_time = get_time()

    @staticmethod
    def do(defender):
        if get_time() - defender.start_time > defender.play_anim[defender.action].total_delay:
            print('컷')
            defender.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def exit(player, e):
        pass

class StatMachine_Defender:
    def __init__(self, defender):
        self.defender = defender
        self.cur_state = Idle_Defender
        self.transitions = {
            Idle_Defender: {defender_run_right: RunRight_Defender, defender_run_left: RunLeft_Defender, defender_throw: Throw_Defender},
            RunRight_Defender: {defender_idle: Idle_Defender, defender_throw: Throw_Defender},
            RunLeft_Defender: {defender_idle: Idle_Defender, defender_throw: Throw_Defender},
            Throw_Defender: {time_out: Idle_Defender}
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