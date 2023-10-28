'''
    2DGPGame의 define 하기 위한 모듈
    게임 오브젝트 정보, 다른 객체의 정보를 저장한다.
'''

''' [ Object Info ] '''

#Object Type
STATIC = 0
DYNAMIC = 1

#BackGround
background_name = 'BackGround'
background_pos = [400, 300]
background_size = [800, 600]
background_img = 'Sprites/BG_Base.png'
background_type = STATIC

#Player
player_name = 'player'

#AI
playerAI_name = 'playerAI'

#Base Ball
base_ball_name = 'base_ball'
base_ball_pos = [400, 300]
base_ball_size = [100, 100]
base_ball_img = 'Sprites/BaseBall.png'

''' [ UI Info ] '''

#Throw_Target
throw_target_name = 'Throw_Target'
throw_target_pos = [400, 300]       # x: 360 ~ 450, y : 90 ~ 210
throw_target_size = [200, 200]
throw_target_img = 'Sprites/Throw_Target.png'
throw_target_ui_size = [100, 100]

#Throw_Target_Effect
throw_target_effect_name = 'Throw_Target_Effect'
throw_target_effect_pos = [400, 300]
throw_target_effect_size = [200, 200]
throw_target_effect_img = 'Sprites/Throw_Target_Effect.png'
throw_target_effect_ui_size = [100, 100]

#Throw_Target_End
throw_target_end_name = 'Throw_Target_End'
throw_target_end_pos = [400, 300]
throw_target_end_size = [200, 200]
throw_target_end_img = 'Sprites/Throw_Target_End.png'
throw_target_end_ui_size = [100, 100]

#Message_Strike
message_strike = 'Message_Strike'
message_strike_pos = [400, 300]
message_strike_size = [400, 200]
message_strike_img = 'Sprites/Ui/Msg_Strike.png'
message_strike_ui_size = [400, 200]

#Message_Strike_Out
message_strike_out = 'Message_Strike_Out'
message_strike_out_pos = [400, 300]
message_strike_out_size = [400, 200]
message_strike_out_img = 'Sprites/Ui/Msg_Strike_Out.png'
message_strike_out_ui_size = [400, 200]

#Message_Ball
message_ball = 'Message_Ball'
message_ball_pos = [400, 300]
message_ball_size = [400, 200]
message_ball_img = 'Sprites/Ui/Msg_Ball.png'
message_ball_ui_size = [400, 200]


''' [ System ] '''

# 이닝 초/말
TOP = 0
BOTTOM = 1

# 공 생성 위치 범위
THROW_MAX_X = 460
THROW_MAX_Y = 220
THROW_MIN_X = 350
THROW_MIN_Y = 80

# 스트라이크 존
STRIKE_MAX_X = 440
STRIKE_MAX_Y = 200
STRIKE_MIN_X = 370
STRIKE_MIN_Y = 100

''' PlayModeInfo '''
class PlayMode_Info():
    pos = []
    size = []
    sprite_sheet = None
    type = None
    anim = {}

''' Animation '''
class anim_frame():
    posX = []
    posY = []
    delay = []

''' Hitter '''

Hitter_Anim = []

# IDLE
Hitter_IDLE = anim_frame()
Hitter_IDLE.posX = [275, 275, 275]
Hitter_IDLE.posY = [200, 200, 200]
Hitter_IDLE.delay = [200, 250, 150]

# HIT
Hitter_HIT = anim_frame()
Hitter_HIT.posX = [275, 275, 275, 345, 345, 275]
Hitter_HIT.posY = [200, 200, 200, 200, 200, 200]
Hitter_HIT.delay = [5, 5, 5, 50, 50, 120]
Hitter_HIT.max_frame = 6

Hitter_Anim.append(Hitter_IDLE)
Hitter_Anim.append(Hitter_HIT)

# Hitter 구조체
Hitter = PlayMode_Info()
Hitter.pos = [275, 200]
Hitter.size = [300, 300]
Hitter.sprite_sheet = 'Sprites/Hitter/Sprite_Sheet_Hitter.png'
Hitter.type = DYNAMIC
Hitter.anim = Hitter_Anim

''' Pitcher '''

Pitcher_Anim = []

# IDLE
Pitcher_IDLE = anim_frame()
Pitcher_IDLE.posX = [400, 400, 400, 400, 400]
Pitcher_IDLE.posY = [270, 270, 270, 270, 270]
Pitcher_IDLE.delay = [100, 100, 100, 100, 100]

# Throw
Picher_THROW = anim_frame()
Picher_THROW.posX = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400]
Picher_THROW.posY = [270, 270, 270, 270, 270, 270, 270, 270, 270, 270]
Picher_THROW.delay = [100, 100, 100, 100, 100, 50, 30, 30, 50, 100]

Pitcher_Anim.append(Pitcher_IDLE)
Pitcher_Anim.append(Picher_THROW)

# Pitcher 구조체
Pitcher = PlayMode_Info()
Pitcher.pos = [400, 270]
Pitcher.size = [100, 100]
Pitcher.sprite_sheet = 'Sprites/Pitcher/Sprite_Sheet_Pitcher.png'
Pitcher.type = DYNAMIC
Pitcher.anim = Pitcher_Anim


''' PlayMode'''
HITTER = 0
PITCHER = 1
PlayMode = {HITTER: Hitter, PITCHER: Pitcher}



'''///////////////////////////////////////////////////////////////////////////////'''

''' 능력치가 바뀔 시 조정해야 하는 변수 정의 '''

''' GameSystem Class '''
# def check_throw_event_by_hit(self) : decrease_size


