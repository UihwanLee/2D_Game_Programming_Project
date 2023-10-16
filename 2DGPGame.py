from pico2d import *

class Game2DGP:
    def __init__(self):
        self.running = True

    def Handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                self.running = False

    def Run(self):
        open_canvas()
        while self.running:
            clear_canvas()
            self.Handle_events()

        close_canvas()

program = Game2DGP()
program.Run()


