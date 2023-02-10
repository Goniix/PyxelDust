import pyxel
class Game:
    def __init__(self):
        pyxel.init(720,480)
        pyxel.run(self._update, self._draw)
        
    def _update(self):
        pass

    def _draw(self):
        pass

Game()
