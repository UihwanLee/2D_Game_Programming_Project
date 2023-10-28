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

    def update(self):
        pass

    def render(self):
        bActive = super().get_object_var('bActive')
        if bActive == False : return

        pos = super().get_object_var('pos')
        size = super().get_object_var('size')

        self.sprite.clip_draw(0, 0, self.ui_size[0], self.ui_size[1], pos[0], pos[1], size[0], size[1])


class UIManager:
    def __init__(self):
        self.list_ui = []

    def create_ui(self, name, pos, sprite, size, type, layer, bActive, ui_size):
        self.list_ui.append(UI(name, pos, sprite, size, type, layer, bActive, ui_size))

    def render(self):
        for ui in self.list_ui:
            ui.update()
            ui.render()

     # ui 리스트에 들어있는 객체를 이름으로 찾기
    def find_ui(self, name):
        for ui in self.list_ui:
            if ui.name == name:
                return ui

        return None

