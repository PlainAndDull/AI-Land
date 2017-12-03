import os
import sys
import pygame

class Window:
    
    TITLE = "AI-Land"
    ICON = "icon.bmp"
    WIDTH = 256
    HEIGHT = 192
    
    def __init__(self: 'Window', scale: 'int', transparent: 'str') -> 'None':
        
        self._layers = []
        self._updates = []
        
        if sys.platform == "win32":
            os.environ["SDL_VIDEODRIVER"] = "directx"
        elif sys.platform == "darwin":
            os.environ["SDL_VIDEODRIVER"] = "Quartz"
        else:
            pass
        pygame.display.init()
        pygame.display.set_caption(Window.TITLE)
        pygame.display.set_icon(pygame.image.load(Window.ICON))
        self._layers.append(pygame.display.set_mode((Window.WIDTH * scale, Window.HEIGHT * scale)))
        self._layers[0].fill(pygame.Color("black"))
        self._layers.append(self._layers[0].copy())
        self._layers.append(self._layers[0].copy())
        self._layers[2].fill(pygame.Color(transparent))
        self._layers[2].set_colorkey(pygame.Color(transparent))
        pygame.display.update()
        
        return None
    
    def draw(self: 'Window', layer: 'int', image: 'Surface', x: 'int', y: 'int', area: 'Rect') -> 'None':
        
        for i in range(200):
            self._layers[layer].blit(image, (x, y), area)
        self._updates.append(pygame.Rect(x, y, area.w, area.h))
        
        return None
    
    def update(self: 'Window') -> 'None':
        
        pygame.display.update()
        self._updates.clear()
        
        return None
    
    def close(self: 'Window') -> 'None':
        
        pygame.display.quit()
        
        return None