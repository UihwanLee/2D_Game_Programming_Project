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

#BackGround2
background_base_02_name = 'Background_Base_02'
background_base_02_pos = [400, 600]
background_base_02_size = [1200, 1400]
background_base_02_img = 'Sprites/BG_Base_2.png'
background_base_02_type = STATIC

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

# Hit_Box
hit_box = 'Hit_Box'
hit_box_pos = [400, 150]
hit_box_size = [80, 80]
hit_box_img = 'Sprites/Hit_Box.png'
hit_box_ui_size = [100, 100]


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

# 투수 던지는 파워 범위(1, 2, 3)
THROW_POWER_LOW = 1
THROW_POWER_MIDDLE = 2
THROW_POWER_HIGH = 3

# 타자 hit 시 판단 변수
HIT_EXACT_SIZE = 100
FLYING_HIT_MAX_OFFSET = 14  # 뜬볼 최소 offset 값
HIT_MAX_OFFSET = 10         # 안타 최소 offset 값
HOME_RUN_MAX_OFFSET = 1.0   # 홈런 최소 offset 값

HIT_DIR_MIN_X = 200         # hit 시 야구공 이동 방향 최소 x값
HIT_DIR_MAX_X = 600         # hit 시 야구공 이동 방향 최대 x값
HIT_DIR_MIN_Y = 300         # hit 시 야구공 이동 방향 최소 y값
HIT_DIR_MAX_Y = 400         # hit 시 야구공 이동 방향 최대 y값
HIT_DEPTH_MIN = 500         # hit 시 야구공 이동 깊이 최소 값
HIT_DEPTH_MAX = 700         # hit 시 야구공 이동 깊이 최대 값


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
# Hitter_HIT.delay = [5, 5, 5, 50, 50, 120
Hitter_HIT.delay = [5, 5, 5, 50, 50, 70]
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
# Picher_THROW.delay = [70, 70, 30, 30, 30, 30, 30, 30, 50, 70]

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


