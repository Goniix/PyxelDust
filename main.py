import pyxel
class Game:
    def __init__(self) -> None:
        pyxel.init(720,480)
        pyxel.run(self._update, self._draw)
        
    def _update(self) -> None:
        pass

    def _draw(self) -> None:
        pass

Game()