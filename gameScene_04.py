from gameScene import *

# Scene04 : 경기 플레이 화면 02
class Scene04(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)

        self.Defender_List = []

    # scene에서 초기 오브젝트 세팅
    def init(self):
        # GameObject
        super().create_object(background_base_02_name, background_base_02_pos, background_base_02_img, background_base_02_size, STATIC, 0, True)
        super().create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 1, True)

        # Defender
        super().create_defender(Defender_name+'1', [630, 330], Defender_Info, 1, True, 0)   # 1루수
        super().create_defender(Defender_name+'2', [400, 580], Defender_Info, 1, True, 0)   # 2루수
        super().create_defender(Defender_name+'3', [170, 330], Defender_Info, 1, True, 0)   # 3루수

        for idx in range(1, 4):
            self.Defender_List.append(super().find_object(Defender_name + str(idx)))


    # scene 전환 시 초기 함수
    def start(self):
        # 초기 세팅
        pass

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

    # Scene04에 있는 모든 defender 위치 리셋
    def reset_all_defender(self):
        self.Defender_List[0].pos = [630, 330]  # 1루수
        self.Defender_List[1].pos = [400, 580]  # 2루수
        self.Defender_List[2].pos = [170, 330]  # 3루수