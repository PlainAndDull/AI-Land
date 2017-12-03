import graphics
import audio
import controller
import data
import clock

class Game:
    
    def __init__(self: 'Game') -> 'None':
        
        self.graphics = graphics.Graphics()
        self.audio = audio.Audio()
        self.controller = controller.Controller()
        self.data = data.Data()
        self.clock = clock.Clock()
        
        return None
    
    def execute(self: 'Game') -> 'None':
        
        x = 0
        y = 0
        while True:
            dx = 0
            dy = 0
            self.clock.tick(60)
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
            x += dx
            y += dy
            self.graphics.draw(0, "player", "up", x, y)
            self.graphics.update()
            
        return None
    
    def terminate(self: 'Game') -> 'None':
        
        self.graphics.close()
        
        return None
    
if __name__ == "__main__":
        
    game = Game()
    game.execute()
    game.terminate()