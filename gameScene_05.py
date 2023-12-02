import random

from gameScene import *

# Scene01 : 시작 화면/옵션 선택
class Scene05(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)

        self.Team_Player_List = []
        self.Team_CPU_List = []

    def init(self):
        # background
        super().create_object(background_base_02_name, background_base_02_pos, background_base_02_img, background_base_02_size, STATIC, 0, True)

        # panel
        super().create_ui(panel_team_show, panel_team_show_pos, panel_team_show_img, panel_team_show_size, DYNAMIC, 1, True, panel_team_show_ui_size)

        # team_player
        super().create_ui(team_01_name + 'player', [200, 350], team_01_img, [200, 200], DYNAMIC, 2, False, team_01_ui_size)
        super().create_ui(team_02_name + 'player', [200, 350], team_02_img, [200, 200], DYNAMIC, 2, False, team_02_ui_size)
        super().create_ui(team_03_name + 'player', [200, 350], team_03_img, [200, 200], DYNAMIC, 2, False, team_03_ui_size)
        super().create_ui(team_04_name + 'player', [200, 350], team_04_img, [200, 200], DYNAMIC, 2, False, team_04_ui_size)
        super().create_ui(team_05_name + 'player', [200, 350], team_05_img, [200, 200], DYNAMIC, 2, False, team_05_ui_size)

        # team_computer
        super().create_ui(team_01_name + 'cpu', [600, 350], team_01_img, [200, 200], DYNAMIC, 2, False, team_01_ui_size)
        super().create_ui(team_02_name + 'cpu', [600, 350], team_02_img, [200, 200], DYNAMIC, 2, False, team_02_ui_size)
        super().create_ui(team_03_name + 'cpu', [600, 350], team_03_img, [200, 200], DYNAMIC, 2, False, team_03_ui_size)
        super().create_ui(team_04_name + 'cpu', [600, 350], team_04_img, [200, 200], DYNAMIC, 2, False, team_04_ui_size)
        super().create_ui(team_05_name + 'cpu', [600, 350], team_05_img, [200, 200], DYNAMIC, 2, False, team_05_ui_size)

        # UI
        super().create_ui(ui_player, ui_player_pos, ui_player_img, ui_player_size, DYNAMIC, 3, True, ui_player_ui_size)
        super().create_ui(ui_cpu, ui_cpu_pos, ui_cpu_img, ui_cpu_size, DYNAMIC, 3, True, ui_cpu_ui_size)

        self.Team_Player_List.append(super().find_ui(team_01_name + 'player'))
        self.Team_Player_List.append(super().find_ui(team_02_name + 'player'))
        self.Team_Player_List.append(super().find_ui(team_03_name + 'player'))
        self.Team_Player_List.append(super().find_ui(team_04_name + 'player'))
        self.Team_Player_List.append(super().find_ui(team_05_name + 'player'))

        self.Team_CPU_List.append(super().find_ui(team_01_name + 'cpu'))
        self.Team_CPU_List.append(super().find_ui(team_02_name + 'cpu'))
        self.Team_CPU_List.append(super().find_ui(team_03_name + 'cpu'))
        self.Team_CPU_List.append(super().find_ui(team_04_name + 'cpu'))
        self.Team_CPU_List.append(super().find_ui(team_05_name + 'cpu'))

        # fade
        super().create_ui(bg_black_name, bg_black_pos, bg_black_img, bg_black_size, DYNAMIC, 3, False, bg_black_ui_size)

        # sound
        self.create_bgm(bgm_scene03_name, bgm_scene03_path)


    # scene 전환 시 초기 함수
    def start(self):
        # 초기 세팅
        self.sound_manager.setBGM(bgm_scene03_name)
        self.sound_manager.playBGM()
        self.game_engine.game_system.reset_system()

        self.set_team_player()
        self.set_team_cpu()

        self.start_game()

    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                super().quit()
            else:
                pass

    def set_team_player(self):
        # 현재 고른 팀에 맞게 설정
        player_team = self.game_engine.game_system.get_choose_team()

        for player in self.Team_Player_List:
            if player.name == player_team + 'player':
                player.bActive = True

    def set_team_cpu(self):
        # 현재 고른 팀에 맞게 설정
        player_team = self.game_engine.game_system.get_choose_team()

        while(True):
            idx = random.randint(0, 4)
            if self.Team_CPU_List[idx].name != player_team + 'cpu':
                self.Team_CPU_List[idx].bActive = True
                break

    def start_game(self):
        fade_ui = self.ui_manager.find_ui(bg_black_name)
        self.ui_manager.start_fade_in(fade_ui, 3000, self)

    def fade_done(self, ui):
        super().change_scene(SCENE_03, True)
