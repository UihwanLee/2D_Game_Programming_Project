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


''' Animation '''
class anim_frame():
    posX = []
    posY = []
    delay = []

player_Anim = []

player_IDLE = anim_frame()
player_IDLE.posX = [275, 275, 275]
player_IDLE.posY = [200, 200, 200]
player_IDLE.delay = [0.5, 0.3, 0.5]

player_Anim.append(player_IDLE)


