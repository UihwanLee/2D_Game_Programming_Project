from gameScene import *

# Scene03 : 경기 플레이 화면 01
class Scene03(Scene):
    def __init__(self, order, engine):
        super().__init__(order, engine)
        self.player = None

    # scene에서 초기 오브젝트 / UI 세팅
    def init(self):
        # GameOjbect
        super().create_object(background_name, background_pos, background_img, background_size, background_type, 0,
                              True)
        super().create_player(player_name, Hitter, 3, True, 0)
        super().create_playerAI(playerAI_name, Pitcher, 1, True, 0)
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

        self.player = super().find_object(player_name)

    # scene 전환 시 초기 함수
    def start(self):
        #초기 세팅
        pass

    # Scene에서 handle_event 처리
    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                super().quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                super().change_scene(SCENE_02) # 종료 canvas를 띄운다.
            else:
                if (self.player != None):
                    if (self.player.bActive):
                        self.player.handle_event(event)