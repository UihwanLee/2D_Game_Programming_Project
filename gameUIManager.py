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
        self.alpha = 1.0  # 투명도

        self.sprite_name = sprite

        # fade_in/out
        self.is_fade_in_anim = False
        self.is_fade_anim = False
        self.fade_in_alpha = 0.0
        self.fade_out_alpha = 0.0
        self.fade_ui = None
        self.fade_sprite = None
        self.fade_in_done = False

        # fade 결과를 보낼 scene
        self.scene = None

    # ui update 함수. fade_in/fade_out 같은 애니메이션 등을 처리한다.
    def update(self):
        if self.is_fade_anim:
            self.fade_in()
            self.fade_out()

    # ui 렌더링 함수
    def render(self):
        bActive = super().get_object_var('bActive')
        if bActive == False: return

        pos = super().get_object_var('pos')
        size = super().get_object_var('size')

        self.sprite.clip_draw(0, 0, self.ui_size[0], self.ui_size[1], pos[0], pos[1], size[0], size[1])

    # ui sprite 변경
    def change_sprite(self, new_sprite):
        super().change_sprite(new_sprite)

    # ui Sprite 투명도 조정
    def set_alpha(self, alpha):
        sprite = super().get_object_var('sprite')
        sprite.opacify(alpha)

    def is_fade_done(self):
        return self.is_fade_anim

    # ui Fade in 애니메이션
    def start_fade_in(self, ui, in_duration=100.0, scene = None):
        self.fade_ui = ui
        self.fade_ui.bActive = True
        self.fade_sprite = ui.get_object_var('sprite')
        self.fade_in_alpha = 1.0 / in_duration
        self.fade_ui.alpha = 0.0
        self.fade_in_done = False
        self.is_fade_in_anim = True
        self.is_fade_anim = True

        self.scene = scene

    # ui Fade in/Out 애니메이션
    def start_fade(self, ui, in_duration=100.0, out_duration=100.0, scene=None):
        self.fade_ui = ui
        self.fade_ui.bActive = True
        self.fade_sprite = ui.get_object_var('sprite')
        self.fade_in_alpha = 1.0 / in_duration
        self.fade_out_alpha = 1.0 / out_duration
        self.fade_ui.alpha = 0.0
        self.fade_in_done = False
        self.is_fade_in_anim = False
        self.is_fade_anim = True

        self.scene = scene

    # fade_in 함수 : 이미지 투명도를 0에서 1로 바꿔준다.
    def fade_in(self):
        if self.fade_in_done:
            return

        if self.fade_ui.alpha >= 1.0:
            if self.is_fade_in_anim:
                if self.scene is not None:
                    self.scene.fade_done()
                self.is_fade_anim = False
            else:
                self.fade_in_done = True
            return

        self.fade_ui.alpha += self.fade_in_alpha
        self.fade_sprite.opacify(self.fade_ui.alpha)

    # fade_out 함수 : 이미지 투명도를 1에서 0로 바꿔준다.
    def fade_out(self):
        if self.fade_in_done == False:
            return

        # fade_out 시 다시 이미지의 투명도를 1로 바꿔 준후 bActive = False로 해결해준다.
        if self.fade_ui.alpha <= 0.0:
            self.is_fade_anim = False
            self.fade_ui.bActive = False
            self.fade_sprite.opacify(1)

            # scene이 존재하면 fade가 끝났음을 알린다.
            if self.scene is not None:
                self.scene.fade_done()
            return

        self.fade_ui.alpha -= self.fade_out_alpha
        self.fade_sprite.opacify(self.fade_ui.alpha)


class UIManager:
    def __init__(self):
        self.ui_list = [[] for _ in range(4)]

        # fade_in/out
        self.is_fade_in_anim = False
        self.is_fade_anim = False
        self.fade_in_alpha = 0.0
        self.fade_out_alpha = 0.0
        self.fade_ui = None
        self.fade_sprite = None
        self.fade_in_done = False

    # ui 생성하는 함수, ui_list에 담는다.
    def create_ui(self, name, pos, sprite, size, type, layer, bActive, ui_size):
        self.ui_list[layer].append(UI(name, pos, sprite, size, type, layer, bActive, ui_size))

    # ui_manager update 함수. ui_list에 들어있는 ui를 update한다.
    def update(self):
       for layer in self.ui_list:
           for ui in layer:
                ui.update()

    # ui_manager render 함수. ui_list에 담긴 ui를 그린다.
    def render(self):
        for layer in self.ui_list:
            for ui in layer:
                ui.render()

    # ui 리스트에 들어있는 객체를 이름으로 찾기
    def find_ui(self, name):
        for layer in self.ui_list:
            for ui in layer:
                if ui.name == name:
                    return ui

        return None

    # ui 활성화/비활성화
    def set_bActive(self, name, bActive):
        for layer in self.ui_list:
            for ui in layer:
                if ui.name == name:
                    ui.bActive = bActive

    # 마우스 클릭했을 때 ui button를 클릭했는지 판단하는 함수
    def check_click_button(self, name, mx, my):
        button = self.find_ui(name)

        if button.bActive is False:
            return False

        bottom_x = button.pos[0] - button.size[0]/2
        bottom_y = button.pos[1] - button.size[1]/2
        top_x = button.pos[0] + button.size[0]/2
        top_y = button.pos[1] + button.size[1]/2

        if bottom_x > mx:return False
        if bottom_y > my: return False
        if top_x < mx: return False
        if top_y < my: return False

        return True

    # 마우스를 버튼 위에 올려놓을 시 버튼 사이즈 크기 조정 함수
    def mouse_on_button(self, button, size):
        button.size = size

    # 마우스를 버튼 위치를 벗어났을 시 버튼 사이즈 크기 조정 함수
    def mouse_off_button(self, button, size):
        button.size = size

    # ui Fade in 애니메이션
    def start_fade_in(self, ui, in_duration=100.0, scene = None):
        ui.start_fade_in(ui, in_duration, scene)

    # ui Fade in/Out 애니메이션
    def start_fade(self, ui, in_duration=100.0, out_duration=100.0, scene = None):
        ui.start_fade(ui, in_duration, out_duration, scene)

    def check_fade_anim_done(self, ui):
        return ui.is_fade_anim

    # 반짝반짝 애니메이션
    def start_twincle(self, name, in_duration, out_duration):
        pass

