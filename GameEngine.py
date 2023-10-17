from scene import Scene

# 게임 내 모든 씬, 오브젝트, 시스템 관리할 클래스
class GameEngine:
    def __init__(self):
        self.scene_01 = Scene(1)
        self.curScene = self.scene_01
        pass

    def BuildScenes(self):
        self.scene_01.CreateObject((400, 300), 'Sprites/BG_Base.png', 0, True)
        pass

    def RenderScenes(self):
        self.curScene.Render()

