from pico2d import load_image
from Define import STATIC, DYNAMIC


class GameObject:

    # 게임 오브젝트 초기화 (씬 정보, 위치, 이미지, 타입, 레이어, 활성화) 정보를 초기화 한다.
    def __init__(self, scene, name, pos, sprite, size, type, layer, bActive):
        self.scene = scene
        self.name = name
        self.pos = pos
        self.sprite = load_image(sprite)
        self.size = size
        self.type = type
        self.layer = layer
        self.bActive = bActive

    # 게임 오브젝트 업데이트. 활성화 된 오브젝트만 업데이트 한다.
    def update(self):
        if self.bActive is False: return
        pass

    # 게임 오브젝트 렌더링. 활성화 된 오브젝트만 렌더링 한다.
    def render(self):
        if self.bActive is False: return

        if self.type == STATIC:
            self.sprite.draw(self.pos[0], self.pos[1])
        elif self.type == DYNAMIC:
            self.sprite.clip_draw(0, 0, 100, 100, self.pos[0], self.pos[1], self.size[0], self.size[1])

    # 게임 오브젝트 sprite 변경
    def change_sprite(self, new_sprite):
        self.sprite = load_image(new_sprite)

    # 오브젝트 Sprite 투명도 조정
    def set_alpha(self, alpha):
        self.sprite.opacify(alpha)

    # 게임 오브젝트 멤버변수 get 함수. GameObject 클래스를 상속 받은 클래스가 GameObject 멤버 변수에 접근할 때 사용 한다.
    def get_object_var(self, var):
        if hasattr(self, var):
            return getattr(self, var)
        else:
            print('No var in Object')
            return None
