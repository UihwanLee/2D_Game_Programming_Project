from gameScene import *

# Scene01 : 시작 화면/옵션 선택
class Scene01(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.ui_manager = super().get_object_var('ui_manager')
        self.touch_screen = False
        self.touch_screen_ui = None
        self.mouse_point = [1000.0, 1000.0]

    # scene에서 초기 오브젝트 세팅
    def init(self):
        # GameOjbect
        super().create_object(start_bg_name, start_bg_pos, start_bg_img, start_bg_size, start_bg_type, 2, True)
        super().create_ui(start_02_bg_name, start_02_bg_pos, start_02_bg_img, start_02_bg_size, start_02_bg_type, 2, False,
                          [800, 600])

        # UI
        super().create_ui(touch_screen_name, touch_screen_pos, touch_screen_img, touch_screen_size, DYNAMIC, 1, True,
                          touch_screen_ui_size)
        super().create_ui(button_empty_name, [565, 470], button_empty_img, [210, 100], DYNAMIC, 3, False,
                          button_empty_ui_size)
        super().create_ui(button_empty_name, [620, 390], button_empty_img, [210, 100], DYNAMIC, 3, False,
                          button_empty_ui_size)
        super().create_ui(button_gamestart_name, [640, 300], button_gamestart_img, [210, 100], DYNAMIC,3, False,
                          button_gamestart_ui_size)
        super().create_ui(button_quit_name, [560, 120], button_quit_img, [210, 100], DYNAMIC, 3, False,
                          button_quit_ui_size)
        super().create_ui(button_return_name, [620, 210], button_return_img, [210, 100], DYNAMIC, 3, False,
                          button_return_ui_size)

        # touch_screen 반짝이기
        self.touch_screen_ui = self.ui_manager.find_ui(touch_screen_name)
        self.ui_manager.start_fade(self.touch_screen_ui, 200, 200, self)

    # scene 전환 시 초기 함수
    def start(self):
        self.return_start()
        # touch_screen 반짝이기
        self.touch_screen_ui = self.ui_manager.find_ui(touch_screen_name)
        self.ui_manager.start_fade(self.touch_screen_ui, 200, 200, self)

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                if self.touch_screen is False:
                    super().quit()
                else:
                    self.return_start()
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_point[0], self.mouse_point[1] = event.x, WINDOW_HEIGHT - 1 - event.y
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:  # 마우스 왼쪽 버튼 클릭
                if self.touch_screen is False:
                    self.start_option()
                else:
                    # UI 버튼 클릭 체크
                    if self.ui_manager.check_click_button(button_gamestart_name, self.mouse_point[0], self.mouse_point[1]): super().change_scene(SCENE_02)
                    if self.ui_manager.check_click_button(button_quit_name, self.mouse_point[0], self.mouse_point[1]): super().quit()
                    if self.ui_manager.check_click_button(button_return_name, self.mouse_point[0], self.mouse_point[1]): self.return_start()
            else:
                pass

    # 게임 옵션 선택 창으로 이동
    def start_option(self):
        self.touch_screen = True
        super().set_object_bActive(start_bg_name, False)
        self.ui_manager.set_bActive(start_02_bg_name, True)
        self.ui_manager.set_bActive(touch_screen_name, False)

        self.ui_manager.set_bActive(button_empty_name, True)
        self.ui_manager.set_bActive(button_gamestart_name, True)
        self.ui_manager.set_bActive(button_quit_name, True)
        self.ui_manager.set_bActive(button_return_name, True)

    # 게임 터치 화면으로 이동
    def return_start(self):
        self.touch_screen = False
        super().set_object_bActive(start_bg_name, True)
        self.ui_manager.set_bActive(start_02_bg_name, False)
        self.ui_manager.set_bActive(touch_screen_name, True)

        self.ui_manager.set_bActive(button_empty_name, False)
        self.ui_manager.set_bActive(button_gamestart_name, False)
        self.ui_manager.set_bActive(button_quit_name, False)
        self.ui_manager.set_bActive(button_return_name, False)

    def fade_done(self):
        self.ui_manager.start_fade(self.touch_screen_ui, 200, 200, self)