from gameObject import GameObject

'''
    Player 클래스 : GameObject 상속
    
'''
class Player(GameObject):
    def __int__(self, scene, pos, sprite, type, layout, bActive):
        super().scene = scene
        super().pos = pos
        super().sprite = sprite
        super().type = type
        super().bActive = bActive

    def Update(self):
        pass

    def Render(self):
        print('player 클래스입니다')
