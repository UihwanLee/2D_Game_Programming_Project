from sdl2 import SDLK_s

from gameScene import *

# Scene03 : 경기 플레이 화면 01
class Scene03(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.player = None
        self.cover = None
        self.strike_ui = []
        self.ball_ui = []
        self.out_ui = []

    # scene에서 초기 오브젝트 / UI 세팅
    def init(self):
        # GameOjbect
        super().create_object(background_name, background_pos, background_img, background_size, background_type, 0,
                              True)
        super().create_hitter(player_name, Hitter_Info, 3, True, 0)
        super().create_pitcher(playerAI_name, Pitcher_Info, 1, True, 0)
        super().create_object(base_ball_name, base_ball_pos, base_ball_img, base_ball_size, DYNAMIC, 2, False)

        # UI
        super().create_ui(throw_target_name, throw_target_pos, throw_target_img, throw_target_size, DYNAMIC, 1, False,
                          throw_target_ui_size)
        super().create_ui(throw_target_effect_name, throw_target_effect_pos, throw_target_effect_img,
                          throw_target_effect_size, DYNAMIC, 1, False, throw_target_effect_ui_size)
        super().create_ui(throw_target_end_name, throw_target_end_pos, throw_target_end_img, throw_target_end_size,
                          DYNAMIC, 1, False, throw_target_end_ui_size)
        super().create_ui(message_strike, message_strike_pos, message_strike_img, message_strike_size, DYNAMIC, 2,
                          False, message_strike_ui_size)
        super().create_ui(message_strike_out, message_strike_out_pos, message_strike_out_img, message_strike_out_size,
                          DYNAMIC, 2, False, message_strike_out_ui_size)
        super().create_ui(message_ball, message_ball_pos, message_ball_img, message_ball_size, DYNAMIC, 2, False,
                          message_ball_ui_size)

        # SKILL
        super().create_ui(ui_skill_name, ui_skill_pos, ui_skill_img, ui_skill_size, DYNAMIC, 2, True, ui_strike_ui_size)
        super().create_object(bg_black_name, bg_black_pos, bg_black_img, bg_black_size, DYNAMIC, 0, False)
        self.cover = super().find_object(bg_black_name)
        self.cover.set_alpha(0.5)

        # EFFECT
        super().create_ui(effect_home_run_01_name, effect_home_run_01_pos, effect_home_run_01_img, effect_home_run_01_size, DYNAMIC, 3, False,
                          effect_home_run_01_ui_size)
        super().create_ui(effect_home_run_02_name, effect_home_run_02_pos, effect_home_run_02_img, effect_home_run_02_size, DYNAMIC, 3, False,
                          effect_home_run_02_ui_size)

        # 스트라이크 2개 / 볼 3개 / 아웃 2개
        super().create_ui(ui_strike_name + '1', ui_strike_pos1, ui_strike_img, ui_strike_size, DYNAMIC, 2, False, ui_strike_ui_size)
        super().create_ui(ui_strike_name + '2', ui_strike_pos2, ui_strike_img, ui_strike_size, DYNAMIC, 2, False, ui_strike_ui_size)
        super().create_ui(ui_ball_name + '1', ui_ball_pos1, ui_ball_img, ui_ball_size, DYNAMIC, 2, False, ui_ball_ui_size)
        super().create_ui(ui_ball_name + '2', ui_ball_pos2, ui_ball_img, ui_ball_size, DYNAMIC, 2, False,ui_ball_ui_size)
        super().create_ui(ui_ball_name + '3', ui_ball_pos3, ui_ball_img, ui_ball_size, DYNAMIC, 2, False, ui_ball_ui_size)
        super().create_ui(ui_out_name + '1', ui_out_pos1, ui_out_img, ui_out_size, DYNAMIC, 2, False, ui_out_ui_size)
        super().create_ui(ui_out_name + '2', ui_out_pos2, ui_out_img, ui_out_size, DYNAMIC, 2, False, ui_out_ui_size)

        for idx in range(1, 3):
            ui_strike = self.ui_manager.find_ui(ui_strike_name + str(idx))
            ui_ball = self.ui_manager.find_ui(ui_ball_name + str(idx))
            ui_out = self.ui_manager.find_ui(ui_out_name + str(idx))
            self.strike_ui.append(ui_strike)
            self.ball_ui.append(ui_ball)
            self.out_ui.append(ui_out)

        self.ball_ui.append(self.ui_manager.find_ui(ui_ball_name + '3'))

        self.player = super().find_object(player_name)

        # sound
        self.create_bgm(bgm_scene03_name, bgm_scene03_path)

        self.create_sound_effect(se_throw_name, se_throw_path)
        self.create_sound_effect(se_strike_name, se_strike_path)
        self.create_sound_effect(se_ball_name, se_ball_path)
        self.create_sound_effect(se_strike_out_name, se_strike_out_path)
        self.create_sound_effect(se_hit_name, se_hit_path)
        self.create_sound_effect(se_hit_home_run_name, se_hit_home_run_path)



    # scene 전환 시 초기 함수
    def start(self):
        ui_skill = self.ui_manager.find_ui(ui_skill_name)
        ui_skill.set_alpha(1.0)

        self.game_engine.game_system.reset_hit()
        self.game_engine.game_system.reset_throw()

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                super().change_scene(SCENE_02, True) # 종료 canvas를 띄운다.
            elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
                self.sound_manager.playSE(se_throw_name, 100)
                self.game_engine.game_system.throw_ball()
            else:
                if (self.player != None):
                    if (self.player.bActive):
                        self.player.handle_event(event)