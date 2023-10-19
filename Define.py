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

#Player
player_pos = (275, 200)
player_img = 'Sprites/Hitter/Sprite_Sheet_Hitter.png'
player_type = DYNAMIC

''' System'''
TOP = 0
BOTTOM = 1


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

''' Pitcher '''
Pitcher_Anim = []

# IDLE




