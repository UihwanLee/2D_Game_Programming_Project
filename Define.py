'''
    2DGPGame의 define 하기 위한 모듈
    게임 오브젝트 정보, 다른 객체의 정보를 저장한다.
'''

#Object Type
STATIC = 0
DYNAMIC = 1

#BackGround
background_pos = (400, 300)
background_img = 'Sprites/BG_Base.png'
background_type = STATIC

''' System'''
TOP = 0
BOTTOM = 1

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

Hitter_Anim.append(Hitter_IDLE)

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

Pitcher_Anim.append(Pitcher_IDLE)

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


