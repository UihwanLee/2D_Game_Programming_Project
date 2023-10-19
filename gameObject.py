from pico2d import load_image


class GameObject:

    # 게임 오브젝트 초기화 (씬 정보, 위치, 이미지, 타입, 레이어, 활성화) 정보를 초기화 한다.
    def __init__(self, scene, pos, sprite, type, layer, bActive):
        self.scene = scene
        self.pos = pos
        self.sprite = load_image(sprite)
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

        self.sprite.draw(self.pos[0], self.pos[1])

    # 게임 오브젝트 멤버변수 get 함수. GameObject 클래스를 상속 받은 클래스가 GameObject 멤버 변수에 접근할 때 사용 한다.
    def get_object_var(self, var):
        if hasattr(self, var):
            return getattr(self, var)
        else:
            print('No var in Object')
            return None
