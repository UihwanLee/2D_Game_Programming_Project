from gameObject import *

'''
    2DGP 게임에서 UI를 관리하는 모듈

    게임 UI Window
    게임 Loading Scene UI

'''

class UI(GameObject):
    def __init__(self, name, pos, sprite, size, type, layer, bActive, ui_size):
        super().__init__(-1, name, pos, sprite, size, type, layer, bActive)
        self.ui_size = ui_size
        self.alpha = 1.0        # 투명도

    # ui update 함수
    def update(self):
        pass

    # ui 렌더링 함수
    def render(self):
        bActive = super().get_object_var('bActive')
        if bActive == False : return

        pos = super().get_object_var('pos')
        size = super().get_object_var('size')

        self.sprite.clip_draw(0, 0, self.ui_size[0], self.ui_size[1], pos[0], pos[1], size[0], size[1])


class UIManager:
    def __init__(self):
        self.ui_list = []

        # fade_in/fade_out
        self.is_fade_anim = False
        self.fade_in_alpha = 0.0
        self.fade_out_alpha = 0.0
        self.fade_ui = None
        self.fade_sprite = None
        self.fade_in_done = False

    # ui 생성하는 함수, ui_list에 담는다.
    def create_ui(self, name, pos, sprite, size, type, layer, bActive, ui_size):
        self.ui_list.append(UI(name, pos, sprite, size, type, layer, bActive, ui_size))

    # ui_manager update 함수. fade_in/fade_out 같은 애니메이션 등을 처리한다.
    def update(self):
        if self.is_fade_anim:
            self.fade_in()
            self.fade_out()

    # ui_manager render 함수. ui_list에 담긴 ui를 그린다.
    def render(self):
        for ui in self.ui_list:
            ui.update()
            ui.render()

     # ui 리스트에 들어있는 객체를 이름으로 찾기
    def find_ui(self, name):
        for ui in self.ui_list:
            if ui.name == name:
                return ui

        return None

    # ui Fade in/Out 애니메이션
    def start_fade(self, ui, in_duration=100.0, out_duration=100.0):
        print('페이드 시작!')
        self.fade_ui = ui
        self.fade_sprite = ui.get_object_var('sprite')
        self.fade_in_alpha = 1.0 / in_duration
        self.fade_out_alpha = 1.0 / out_duration
        self.fade_ui.alpha = 0.0
        self.fade_in_done = False
        self.is_fade_anim = True

    def fade_in(self):
        if self.fade_in_done:
            return

        if self.fade_ui.alpha >= 1.0:
            self.fade_in_done = True
            print("페이드 인 끝")
            return

        self.fade_ui.alpha += self.fade_in_alpha
        self.fade_sprite.opacify(self.fade_ui.alpha)

    def fade_out(self):
        if self.fade_in_done == False:
            return

        if self.fade_ui.alpha <= 0.0:
            self.is_fade_anim = False
            print("페이드 아웃 끝")
            return

        self.fade_ui.alpha -= self.fade_out_alpha
        self.fade_sprite.opacify(self.fade_ui.alpha)


