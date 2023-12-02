from gameScene import *

# Scene02 : 로비/팀 선택 화면
class Scene02(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.ui_manager = super().get_object_var('ui_manager')
        self.player_team = team_03_name
        self.mouse_point = [1000.0, 1000.0]
        self.fade_bg = None
        # self.font = load_font(FONT_STYLE_01, 16)

        self.button_gamestart = None
        self.button_return = None

    # scene에서 초기 오브젝트 세팅
    def init(self):
        # GameOjbect
        super().create_object(start_03_bg_name, start_03_bg_pos, start_03_bg_img, start_03_bg_size, start_03_bg_type, 0, True)

        # UI TEAM
        super().create_ui(team_01_name, team_01_pos, team_01_img, team_01_size, DYNAMIC, 0, True, team_01_ui_size)
        super().create_ui(team_02_name, team_02_pos, team_02_img, team_02_size, DYNAMIC, 0, True, team_02_ui_size)
        super().create_ui(team_03_name, team_03_pos, team_03_img, team_03_size, DYNAMIC, 0, True, team_03_ui_size)
        super().create_ui(team_04_name, team_04_pos, team_04_img, team_04_size, DYNAMIC, 0, True, team_04_ui_size)
        super().create_ui(team_05_name, team_05_pos, team_05_img, team_05_size, DYNAMIC, 0, True, team_05_ui_size)
        super().create_ui(team_select_name, team_select_pos, team_select_img, team_select_size, DYNAMIC, 1, True, team_select_ui_size)

        # UI TEAM SELECT POINT
        super().create_ui(team_select_point_name, team_select_point_pos, team_select_point_img, team_select_point_size, DYNAMIC,
                          1, True, team_select_point_ui_size)

        # UI BUTTON
        super().create_ui(button_empty_name, [400, 300], button_empty_img, [250, 100], DYNAMIC, 0, True,
                          button_empty_ui_size)
        super().create_ui(button_gamestart_name, [280, 40], button_gamestart_img, [250, 100], DYNAMIC, 2, True,
                          button_gamestart_ui_size)
        super().create_ui(button_return_name, [520, 40], button_return_img, [250, 100], DYNAMIC, 1, True,
                          button_return_ui_size)

        # button 초기화
        self.button_gamestart = self.ui_manager.find_ui(button_gamestart_name)
        self.button_return = self.ui_manager.find_ui(button_return_name)

        # Fade BG
        super().create_ui(bg_black_name, bg_black_pos, bg_black_img, bg_black_size, DYNAMIC, 3, False, bg_black_ui_size)
        self.fade_bg = self.ui_manager.find_ui(bg_black_name)

        # sound
        self.create_bgm(bgm_scene02_name, bgm_scene02_path)

    # scene 전환 시 초기 함수
    def start(self):
        self.select_team(team_03_name)
        # black_BG 지우기
        if self.fade_bg is not None:
            self.fade_bg.bActive = False

        self.sound_manager.setBGM(bgm_scene02_name)
        self.sound_manager.playBGM()

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                super().change_scene(SCENE_01, True)
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_point[0], self.mouse_point[1] = event.x, WINDOW_HEIGHT - 1 - event.y
                if self.ui_manager.check_click_button(button_gamestart_name, self.mouse_point[0], self.mouse_point[1]):
                    self.ui_manager.mouse_on_button(self.button_gamestart, [270, 120])
                else:
                    self.ui_manager.mouse_off_button(self.button_gamestart, [250, 100])
                if self.ui_manager.check_click_button(button_return_name, self.mouse_point[0], self.mouse_point[1]):
                    self.ui_manager.mouse_on_button(self.button_return, [270, 120])
                else:
                    self.ui_manager.mouse_off_button(self.button_return, [250, 100])
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:  # 마우스 왼쪽 버튼 클릭
                # 팀 선택 체크
                if self.ui_manager.check_click_button(team_01_name, self.mouse_point[0], self.mouse_point[1]): self.select_team(team_01_name)
                if self.ui_manager.check_click_button(team_02_name, self.mouse_point[0], self.mouse_point[1]): self.select_team(team_02_name)
                if self.ui_manager.check_click_button(team_03_name, self.mouse_point[0], self.mouse_point[1]): self.select_team(team_03_name)
                if self.ui_manager.check_click_button(team_04_name, self.mouse_point[0], self.mouse_point[1]): self.select_team(team_04_name)
                if self.ui_manager.check_click_button(team_05_name, self.mouse_point[0], self.mouse_point[1]): self.select_team(team_05_name)
                if self.ui_manager.check_click_button(button_gamestart_name, self.mouse_point[0], self.mouse_point[1]): self.start_game()
                if self.ui_manager.check_click_button(button_return_name, self.mouse_point[0],self.mouse_point[1]): super().change_scene(SCENE_01, True)
            else:
                pass

    # 팀 선택 시 구현
    def select_team(self, team):
        sl_team = self.ui_manager.find_ui(team)
        point = self.ui_manager.find_ui(team_select_point_name)
        cur_team = self.ui_manager.find_ui(team_select_name)

        self.player_team = sl_team.get_object_var('name')

        # TEAM_SELECT_POINT 위치 이동
        point.pos = sl_team.pos

        # 현재 선택 된 팀 로고 변경
        cur_team.change_sprite(sl_team.sprite_name)

    def start_game(self):
        fade_ui = self.ui_manager.find_ui(bg_black_name)
        self.ui_manager.start_fade_in(fade_ui, 500, self)
        #super().change_scene(SCENE_03)

    def fade_done(self, ui):
        super().change_scene(SCENE_05, True)

    def render(self):
        # self.font.draw(400, 300, self.player_team, (255, 255, 0))
        super().render()