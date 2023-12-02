import random

from gameScene import *

class Scene06(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)

        self.Team_Player_List = []
        self.Team_CPU_List = []

        self.Defender_List = []

    def init(self):
        # background
        super().create_object(background_base_02_name, background_base_02_pos, background_base_02_img, background_base_02_size, STATIC, 0, True)

        # panel
        super().create_ui(panel_change, panel_change_pos, panel_change_img, panel_change_size, DYNAMIC, 1, True, panel_change_ui_size)

        # team_player
        player_pos, cpu_pos, team_size = [85, 530], [85, 490], [40, 40]
        super().create_ui(team_01_name + 'player', player_pos, team_01_img, team_size, DYNAMIC, 2, False, team_01_ui_size)
        super().create_ui(team_02_name + 'player', player_pos, team_02_img, team_size, DYNAMIC, 2, False, team_02_ui_size)
        super().create_ui(team_03_name + 'player', player_pos, team_03_img, team_size, DYNAMIC, 2, False, team_03_ui_size)
        super().create_ui(team_04_name + 'player', player_pos, team_04_img, team_size, DYNAMIC, 2, False, team_04_ui_size)
        super().create_ui(team_05_name + 'player', player_pos, team_05_img, team_size, DYNAMIC, 2, False, team_05_ui_size)

        # team_computer
        super().create_ui(team_01_name + 'cpu', cpu_pos, team_01_img, team_size, DYNAMIC, 2, False, team_01_ui_size)
        super().create_ui(team_02_name + 'cpu', cpu_pos, team_02_img, team_size, DYNAMIC, 2, False, team_02_ui_size)
        super().create_ui(team_03_name + 'cpu', cpu_pos, team_03_img, team_size, DYNAMIC, 2, False, team_03_ui_size)
        super().create_ui(team_04_name + 'cpu', cpu_pos, team_04_img, team_size, DYNAMIC, 2, False, team_04_ui_size)
        super().create_ui(team_05_name + 'cpu', cpu_pos, team_05_img, team_size, DYNAMIC, 2, False, team_05_ui_size)

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

        # defender
        super().create_defender(Defender_name + 'change0', [400, 330], Defender_Info, 1, True, 0)  # 투수
        super().create_defender(Defender_name + 'change1', [630, 330], Defender_Info, 1, True, 0)  # 1루수
        super().create_defender(Defender_name + 'change2', [400, 70], Defender_Info, 1, True, 0)  # 2루수
        super().create_defender(Defender_name + 'change3', [170, 330], Defender_Info, 1, True, 0)  # 3루수

        for idx in range(0, 4):
            self.Defender_List.append(super().find_object(Defender_name + 'change' + str(idx)))

        # sound
        self.create_sound_effect(se_change_team_name, se_change_team_path)


    # scene 전환 시 초기 함수
    def start(self):
        # 초기 세팅
        self.sound_manager.playSE(se_change_team_name, 64)

        self.set_team_player()
        self.set_team_cpu()

        self.set_defender_pos()
        self.play_anim_defender_changing()

        self.resume_game()

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
        player_team = self.game_engine.game_system.get_player_team()

        for player in self.Team_Player_List:
            if player.name == player_team:
                player.bActive = True

    def set_team_cpu(self):
        cpu_team = self.game_engine.game_system.get_cpu_team()

        for cpu in self.Team_CPU_List:
            if cpu.name == cpu_team:
                cpu.bActive = True

    def set_defender_pos(self):
        for defender in self.Defender_List:
            defender.state_machine.handle_event(('Defender Idle', 0))

        self.Defender_List[0].pos = [400, 330]
        self.Defender_List[1].pos = [630, 330]
        self.Defender_List[2].pos = [400, 70]
        self.Defender_List[3].pos = [170, 330]

    def play_anim_defender_changing(self):
        for defender in self.Defender_List:
            defender.state_machine.handle_event(('Defender Change', 0))

    def resume_game(self):
        fade_ui = self.ui_manager.find_ui(bg_black_name)
        self.ui_manager.start_fade_in(fade_ui, 2000, self)

    def fade_done(self, ui):
        super().change_scene(SCENE_03, False)
