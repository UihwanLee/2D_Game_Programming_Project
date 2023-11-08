from gameScene import *

# Scene04 : 경기 플레이 화면 02
class Scene04(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)

    # scene에서 초기 오브젝트 세팅
    def init(self):
        super().create_object(background_base_02_name, background_base_02_pos, background_base_02_img, background_base_02_size, STATIC, 0, True)
        super().create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 1, True)

    # scene 전환 시 초기 함수
    def start(self):
        # 초기 세팅
        pass

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            pass