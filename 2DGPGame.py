from gameEngine import GameEngine

class Game2DGP:
    def __init__(self):
        self.gameEngine = GameEngine()


    # gameEnigne 모듈의 run() 함수를 호출하여 게임을 실행한다.
    def run(self):
        self.gameEngine.run()


program = Game2DGP()
program.run()
