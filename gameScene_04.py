from gameScene import *

# Scene04 : 경기 플레이 화면 02
class Scene04(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.ui_manager = super().get_object_var('ui_manager')
        self.cover = None
        self.base = None
        self.base_list = []
        self.base_ball = None
        self.Defender_List = []
        self.Striker_List = []
        self.home_run_msg = []

    # scene에서 초기 오브젝트 세팅
    def init(self):
        # GameObject
        super().create_object(background_base_02_name, background_base_02_pos, background_base_02_img, background_base_02_size, STATIC, 0, True)
        super().create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 1, True)

        # Defender
        super().create_defender(Defender_name+'0', [400, 330], Defender_Info, 1, True, 0)   # 투수
        super().create_defender(Defender_name+'1', [630, 330], Defender_Info, 1, True, 0)   # 1루수
        super().create_defender(Defender_name+'2', [500, 650], Defender_Info, 1, True, 0)   # 2루수
        super().create_defender(Defender_name+'3', [170, 330], Defender_Info, 1, True, 0)   # 3루수

        super().create_defender(Defender_name + '4', [300, 650], Defender_Info, 1, True, 0)  # 유격수
        super().create_defender(Defender_name + '5', [800, 900], Defender_Info, 1, True, 0)  # 우익수
        super().create_defender(Defender_name + '6', [400, 900], Defender_Info, 1, True, 0)  # 중견수
        super().create_defender(Defender_name + '7', [0, 900], Defender_Info, 1, True, 0)  # 좌익수

        # Striker
        super().create_striker(Striker_name+'0', [400, 70], Striker_Info, 1, True, 0)
        super().create_striker(Striker_name+'1', [630, 330], Striker_Info, 1, False, 0)
        super().create_striker(Striker_name+'2', [400, 580], Striker_Info, 1, False, 0)
        super().create_striker(Striker_name+'3', [170, 330], Striker_Info, 1, False, 0)

        # Base
        super().create_object('Base 1st', [630, 330], None, 0, STATIC, 1, True)
        super().create_object('Base 2st', [400, 580], None, 0, STATIC, 1, True)
        super().create_object('Base 3st', [170, 330], None, 0, STATIC, 1, True)
        super().create_object('Base 4st', [400, 70], None, 0, STATIC, 1, True)

        # cover
        super().create_object(bg_black_name, bg_black_pos, bg_black_img, bg_black_size, DYNAMIC, 0, False)
        self.cover = super().find_object(bg_black_name)
        self.cover.set_alpha(0.7)

        # HOME_RUN_MESSAGE
        super().create_ui(ui_msg_H, ui_msg_H_pos, ui_msg_H_img, ui_msg_H_size, DYNAMIC, 2, False, ui_msg_H_ui_size)
        super().create_ui(ui_msg_O, ui_msg_O_pos, ui_msg_O_img, ui_msg_O_size, DYNAMIC, 2, False, ui_msg_O_ui_size)
        super().create_ui(ui_msg_M, ui_msg_M_pos, ui_msg_M_img, ui_msg_M_size, DYNAMIC, 2, False, ui_msg_M_ui_size)
        super().create_ui(ui_msg_E, ui_msg_E_pos, ui_msg_E_img, ui_msg_E_size, DYNAMIC, 2, False, ui_msg_E_ui_size)
        super().create_ui(ui_msg_R, ui_msg_R_pos, ui_msg_R_img, ui_msg_R_size, DYNAMIC, 2, False, ui_msg_R_ui_size)
        super().create_ui(ui_msg_U, ui_msg_U_pos, ui_msg_U_img, ui_msg_U_size, DYNAMIC, 2, False, ui_msg_U_ui_size)
        super().create_ui(ui_msg_N, ui_msg_N_pos, ui_msg_N_img, ui_msg_N_size, DYNAMIC, 2, False, ui_msg_N_ui_size)
        self.home_run_msg.append(super().find_ui(ui_msg_H))
        self.home_run_msg.append(super().find_ui(ui_msg_O))
        self.home_run_msg.append(super().find_ui(ui_msg_M))
        self.home_run_msg.append(super().find_ui(ui_msg_E))
        self.home_run_msg.append(super().find_ui(ui_msg_R))
        self.home_run_msg.append(super().find_ui(ui_msg_U))
        self.home_run_msg.append(super().find_ui(ui_msg_N))

        self.base = super().find_object(background_base_02_name)
        self.base_ball = super().find_object(base_ball_name)

        self.base_list.append(super().find_object('Base 1st'))
        self.base_list.append(super().find_object('Base 2st'))
        self.base_list.append(super().find_object('Base 3st'))
        self.base_list.append(super().find_object('Base 4st'))

        for idx in range(0, 8):
            self.Defender_List.append(super().find_object(Defender_name + str(idx)))
            self.Defender_List[idx].set_base_list(self.base_list)

        for idx in range(0, 4):
            self.Striker_List.append(super().find_object(Striker_name + str(idx)))
            self.Striker_List[idx].set_base_list(self.base_list)


    # scene 전환 시 초기 함수
    def start(self):
        # 초기 세팅
        pass

    # defender에 game_system 넘기기
    def set_game_system(self, game_system):
        for defender in self.Defender_List:
            defender.set_game_system(game_system)
            defender.base = self.base
            defender.base_ball = self.base_ball
            defender.build_behavior_tree()

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                super().quit()
            else:
                pass

    # Scene04에 있는 모든 오브젝트 pos 갱신
    def move_all_defender(self, move_x, move_y):
        for defender in self.Defender_List:
            defender.pos[0] += move_x
            defender.pos[1] += move_y

        for base in self.base_list:
            base.pos[0] += move_x
            base.pos[1] += move_y

    def move_all_striker(self, move_x, move_y):
        for striker in self.Striker_List:
            striker.pos[0] += move_x
            striker.pos[1] += move_y


    # Scene04에 있는 모든 defender 위치 리셋
    def reset_all_defender(self):
        self.Defender_List[0].pos = [400, 330]
        self.Defender_List[1].pos = [630, 330]
        self.Defender_List[2].pos = [500, 650] # 2루 : 400, 580
        self.Defender_List[3].pos = [170, 330]

        self.Defender_List[4].pos = [300, 650]
        self.Defender_List[5].pos = [800, 900]
        self.Defender_List[6].pos = [400, 900]
        self.Defender_List[7].pos = [0, 900]

    def reset_all_striker(self):
        self.Striker_List[0].pos = [400, 70]
        self.Striker_List[1].pos = [630, 330]
        self.Striker_List[2].pos = [400, 580]  # 2루 : 400, 580
        self.Striker_List[3].pos = [170, 330]

        # 1루 띄기 시작
        self.Striker_List[0].bActive = True
        self.Striker_List[0].state_machine.handle_event(('Striker Run 1st', 0))

