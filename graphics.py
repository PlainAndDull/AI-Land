from window import Window
from image import Image

SCALE = 4
TRANSPARENT = "magenta"

class Graphics:
    
    def __init__(self: 'Graphics') -> 'None':

        self.window = Window(SCALE, TRANSPARENT)
        self.images = {}
        
        self._add_image("player", "player.bmp")
        self._add_area("player", "up", 0, 0, 16, 16)
        self._add_area("player", "down", 0, 16, 16, 16)
        self._add_area("player", "left", 0, 32, 16, 16)
        self._add_area("player", "right", 0, 48, 16, 16)
        
        return None
    
    def draw(self: 'Graphics', layer: 'int', image: 'str', area: 'str', x: 'int', y: 'int') -> 'None':
        
        self.window.draw(layer, self.images[image].get_image(), x * SCALE, y * SCALE, self.images[image].get_area(area))
        
        return None
    
    def erase(self: 'Graphics', layer: 'int', image: 'str', area: 'str', x: 'int', y: 'int') -> 'None':
        
        self.window.erase(layer, x * SCALE, y * SCALE, self.images[image].get_area(area).w, self.images[image].get_area(area).h)
        
        return None
    
    def update(self: 'Graphics') -> 'None':
        
        self.window.update()
        
        return None
    
    def close(self: 'Graphics') -> 'None':
        
        self.window.close()
        
        return None
    
    def _add_image(self: 'Graphics', image: 'str', path: 'str') -> 'None':
        
        self.images[image] = Image(path, SCALE, TRANSPARENT)
        
        return None
    
    def _add_area(self: 'Graphics', image: 'str', area: 'str', x: 'int', y: 'int', w: 'int', h: 'int') -> 'None':
        
        self.images[image].add_area(area, x * SCALE, y * SCALE, w * SCALE, h * SCALE)
        
        return None