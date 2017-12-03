import pygame
import window
import image

class Graphics:
    
    SCALE = 4
    TRANSPARENT = "magenta"
    
    def __init__(self: 'Graphics') -> 'None':

        self._window = window.Window(Graphics.SCALE, Graphics.TRANSPARENT)
        self._images = {}
        
        self._images["player"] = image.Image("player.bmp", Graphics.SCALE, Graphics.TRANSPARENT)
        self._images["player"].areas["up"] = pygame.Rect(0, 0, 16 * Graphics.SCALE, 16 * Graphics.SCALE)
        
        return None
    
    def draw(self: 'Graphics', layer: 'int', image: 'str', area: 'str', x: 'int', y: 'int') -> 'None':
        
        self._window.draw(layer, self._images[image].image, x * Graphics.SCALE, y * Graphics.SCALE, self._images[image].areas[area])
        
        return None
    
    def update(self: 'Graphics') -> 'None':
        
        self._window.update()
        
        return None
    
    def close(self: 'Graphics') -> 'None':
        
        self._window.close()
        
        return None