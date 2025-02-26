from settings import *
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('TetriPy')
        self.screen = pg.display.set_mode(PLAYAREA_RES)
        self.clock = pg.time.Clock()

    