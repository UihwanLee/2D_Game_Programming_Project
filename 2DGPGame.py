from gameEngine import GameEngine

class Game2DGP:
    def __init__(self):
        self.gameEngine = GameEngine()

    def run(self):
        self.gameEngine.run()


program = Game2DGP()
program.run()
