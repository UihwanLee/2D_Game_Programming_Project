'''
    2DGPGame의 define 하기 위한 모듈
    게임 오브젝트 정보, 다른 객체의 정보를 저장한다.
'''

''' [ Object Info ] '''

#Window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

#Scene
SCENE_01 = 'scene_01'
SCENE_02 = 'scene_02'
SCENE_03 = 'scene_03'
SCENE_04 = 'scene_04'

#Mouse
mouse_arrow_img = 'Sprites/hand_arrow.png'

#Object Type
STATIC = 0
DYNAMIC = 1

#Start_Background
start_bg_name = 'Start_BG'
start_bg_pos = [400, 300]
start_bg_size = [800, 600]
start_bg_img = 'Sprites/BG/BG_Base_00.png'
start_bg_type = STATIC

#Start_Background
start_02_bg_name = 'Start_02_BG'
start_02_bg_pos = [400, 300]
start_02_bg_size = [800, 600]
start_02_bg_img = 'Sprites/BG/BG_Base_01.png'
start_02_bg_type = STATIC

#Team_Background
start_03_bg_name = 'Start_03_BG'
start_03_bg_pos = [400, 300]
start_03_bg_size = [800, 600]
start_03_bg_img = 'Sprites/BG/BG_Base_02.png'
start_03_bg_type = STATIC

#BackGround
background_name = 'BackGround'
background_pos = [400, 300]
background_size = [800, 600]
background_img = 'Sprites/BG/BG_Base_03.png'
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
background_base_02_img = 'Sprites/BG/BG_Base_04.png'
background_base_02_type = STATIC

''' [ UI Info ] '''

#TOUCH_SCREEN
touch_screen_name = 'Touch Screen'
touch_screen_pos = [400, 300]
touch_screen_size = [800, 600]
touch_screen_img = 'Sprites/UI/UI_TOUCH_SCREEN.png'
touch_screen_ui_size = [800, 600]

#BUTTON_EMTPY
button_empty_name = 'Button_Empty'
button_empty_pos = [400, 300]
button_empty_size = [200, 100]
button_empty_img = 'Sprites/UI/BUTTON/UI_BUTTON_EMPTY.png'
button_empty_ui_size = [200, 100]

#BUTTON_GAME_START
button_gamestart_name = 'Button_GameStart'
button_gamestart_pos = [640, 300]
button_gamestart_size = [200, 100]
button_gamestart_img = 'Sprites/UI/BUTTON/UI_BUTTON_GAME_START.png'
button_gamestart_ui_size = [200, 100]

#BUTTON_QUIT
button_quit_name = 'Button_Quit'
button_quit_pos = [400, 300]
button_quit_size = [200, 100]
button_quit_img = 'Sprites/UI/BUTTON/UI_BUTTON_QUIT.png'
button_quit_ui_size = [200, 100]

#BUTTON_RETURN
button_return_name = 'Button_Return'
button_return_pos = [400, 300]
button_return_size = [210, 100]
button_return_img = 'Sprites/UI/BUTTON/UI_BUTTON_RETURN.png'
button_return_ui_size = [200, 100]

#BUTTON_RETURN_LOGO
button_return_logo_name = 'Button_Quit'
button_return_logo_pos = [400, 300]
button_return_logo_size = [100, 100]
button_return_logo_img = 'Sprites/UI/BUTTON/UI_BUTTON_RETURN_LOGO.png'
button_return_logo_ui_size = [100, 100]

#TEAM_01
team_01_name = 'TEAM_01'
team_01_pos = [100, 180]
team_01_size = [150, 160]
team_01_img = 'Sprites/UI/TEAMS/UI_TEAM_01.png'
team_01_ui_size = [100, 100]

#TEAM_02
team_02_name = 'TEAM_02'
team_02_pos = [250, 180]
team_02_size = [150, 160]
team_02_img = 'Sprites/UI/TEAMS/UI_TEAM_02.png'
team_02_ui_size = [100, 100]

#TEAM_03
team_03_name = 'TEAM_03'
team_03_pos = [400, 180]
team_03_size = [150, 160]
team_03_img = 'Sprites/UI/TEAMS/UI_TEAM_03.png'
team_03_ui_size = [100, 100]

#TEAM_04
team_04_name = 'TEAM_04'
team_04_pos = [550, 180]
team_04_size = [150, 160]
team_04_img = 'Sprites/UI/TEAMS/UI_TEAM_04.png'
team_04_ui_size = [100, 100]

#TEAM_05
team_05_name = 'TEAM_05'
team_05_pos = [700, 180]
team_05_size = [150, 160]
team_05_img = 'Sprites/UI/TEAMS/UI_TEAM_05.png'
team_05_ui_size = [100, 100]

#SELECT_TEAM
team_select_name = 'TEAM_SELECT'
team_select_pos = [400, 400]
team_select_size = [200, 200]
team_select_img = 'Sprites/UI/TEAMS/UI_TEAM_01.png'
team_select_ui_size = [100, 100]

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
message_strike_img = 'Sprites/UI/Msg_Strike.png'
message_strike_ui_size = [400, 200]

#Message_Strike_Out
message_strike_out = 'Message_Strike_Out'
message_strike_out_pos = [400, 300]
message_strike_out_size = [400, 200]
message_strike_out_img = 'Sprites/UI/Msg_Strike_Out.png'
message_strike_out_ui_size = [400, 200]

#Message_Ball
message_ball = 'Message_Ball'
message_ball_pos = [400, 300]
message_ball_size = [400, 200]
message_ball_img = 'Sprites/UI/Msg_Ball.png'
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
STRIKE_MAX_X = 450
STRIKE_MAX_Y = 205
STRIKE_MIN_X = 360
STRIKE_MIN_Y = 95

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
HIT_DIR_MAX_X = 800         # hit 시 야구공 이동 방향 최대 x값
HIT_DIR_MIN_Y = 300         # hit 시 야구공 이동 방향 최소 y값
HIT_DIR_MAX_Y = 400         # hit 시 야구공 이동 방향 최대 y값

HIT_DEPTH_MIN = 500         # hit 시 야구공 이동 깊이 최소 값
HIT_DEPTH_MAX = 700         # hit 시 야구공 이동 깊이 최대 값

# scene_02
CAMERA_DIR_MIN_X = 700      # camera 이동 방향 최소 x값
CAMERA_DIR_MAX_X = 100      # camera 이동 방향 최대
CAMERA_DEPTH_MIN = 350      # hit 시 야구공 이동 깊이 최소 값
CAMERA_DEPTH_MAX = -100     # hit 시 야구공 이동 깊이 최대 값




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
    total_delay = 0.0

''' Hitter '''

Hitter_Anim = []

# IDLE
Hitter_IDLE = anim_frame()
Hitter_IDLE.posX = [275, 275, 275]
Hitter_IDLE.posY = [200, 200, 200]
Hitter_IDLE.delay = [0.5, 0.5, 0.5]
Hitter_IDLE.total_delay = sum(Hitter_IDLE.delay)

# HIT
Hitter_HIT = anim_frame()
Hitter_HIT.posX = [275, 275, 275, 345, 345, 275]
Hitter_HIT.posY = [200, 200, 200, 200, 200, 200]
Hitter_HIT.delay = [0.01, 0.1, 0.1, 0.05, 0.05, 0.2]
Hitter_HIT.total_delay = sum(Hitter_HIT.delay)
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
Pitcher_IDLE.delay = [0.3, 0.3, 0.3, 0.3, 0.3]
Pitcher_IDLE.total_delay = sum(Pitcher_IDLE.delay)

# Throw
Picher_THROW = anim_frame()
Picher_THROW.posX = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400]
Picher_THROW.posY = [270, 270, 270, 270, 270, 270, 270, 270, 270, 270]
Picher_THROW.delay = [0.1, 0.1, 0.1, 0.1, 0.1, 0.15, 0.1, 0.1, 0.15, 0.3]
Picher_THROW.total_delay = sum(Picher_THROW.delay)

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


