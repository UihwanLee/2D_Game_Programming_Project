from gameEngine import GameEngine

class Game2DGP:
    def __init__(self):
        self.gameEngine = GameEngine()

    def Run(self):
        self.gameEngine.Run()


program = Game2DGP()
program.Run()
