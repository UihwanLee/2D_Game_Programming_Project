from pico2d import *

class Game2DGP:
    def __init__(self):
        self.running = True

    def Run(self):
        open_canvas()
        while self.running:
            clear_canvas()

        close_canvas()

program = Game2DGP()
program.Run()


