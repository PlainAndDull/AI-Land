from graphics import Graphics
from audio import Audio
from controller import Controller
from data import Data
from clock import Clock

FRAMERATE = 60

class Game:
    
    def __init__(self: 'Game') -> 'None':
        
        self.graphics = Graphics()
        self.audio = Audio()
        self.controller = Controller()
        self.data = Data()
        self.clock = Clock()
        
        return None
    
    def execute(self: 'Game') -> 'None':
        
        x = 0
        y = 0
        for i in range(16):
            for j in range(12):
                if i % 2 == 0:
                    self.graphics.draw(0, "player", "left", i * 16, j * 16)
                else:
                    self.graphics.draw(0, "player", "right", i * 16, j * 16)
        self.graphics.update()
        while True:
            dx = 0
            dy = 0
            self.clock.tick(FRAMERATE)
            self.controller.update()
            if self.controller.quit:
                break
            if self.controller.up:
                dy = -1
            if self.controller.down:
                dy = 1
            if self.controller.left:
                dx = -1
            if self.controller.right:
                dx = 1
            self.graphics.erase(3, "player", "up", x, y)
            x += dx
            y += dy
            self.graphics.draw(3, "player", "up", x, y)
            self.graphics.draw(0, "player", "down", 64, 64)
            self.graphics.draw(0, "player", "down", 96, 64)
            self.graphics.update()
            
        return None
    
    def terminate(self: 'Game') -> 'None':
        
        self.graphics.close()
        
        return None
    
if __name__ == "__main__":
    game = Game()
    game.execute()
    game.terminate()