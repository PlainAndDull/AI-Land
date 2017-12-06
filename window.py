import os
import sys
import pygame

TITLE = "AI-Land"
ICON = "icon.bmp"
WIDTH = 256
HEIGHT = 192
LAYERS = 4

class Window:
    
    def __init__(self: 'Window', scale: 'int', transparent: 'str') -> 'None':
        
        self.display = None
        self.layers = []
        self.updates = []
        
        if sys.platform == "win32":
            os.environ["SDL_VIDEODRIVER"] = "directx"
        elif sys.platform == "darwin":
            os.environ["SDL_VIDEODRIVER"] = "Quartz"
        pygame.display.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(ICON))
        self.display = pygame.display.set_mode((WIDTH * scale, HEIGHT * scale))
        self.display.fill(pygame.Color(transparent))
        for layer in range(LAYERS):
            self.layers.append(self.display.copy())
            self.layers[layer].set_colorkey(pygame.Color(transparent))
        pygame.mouse.set_visible(False)
        
        return None
    
    def draw(self: 'Window', layer: 'int', image: 'Surface', x: 'int', y: 'int', area: 'Rect') -> 'None':
        
        self.layers[layer].blit(image, (x, y), area)
        self._add_update(pygame.Rect(x, y, area.w, area.h))
        
        return None
    
    def erase(self: 'Window', layer: 'int', x: 'int', y: 'int', w: 'int', h: 'int') -> 'None':
        
        update = pygame.Rect(x, y, w, h)
        self.layers[layer].fill(self.layers[layer].get_colorkey(), update)
        self._add_update(update)
        
        return None
    
    def update(self: 'Window') -> 'None':
        
        for update in self.updates:
            for layer in range(LAYERS):
                self.display.blit(self.layers[layer], (update.x, update.y), update)
        pygame.display.update(self.updates)
        self.updates.clear()
        
        return None
    
    def close(self: 'Window') -> 'None':
        
        pygame.display.quit()
        
        return None
    
    def _add_update(self: 'Window', update: 'Rect') -> 'None':
        
        rectangles = []
        indices = update.collidelistall(self.updates)
        for index in indices:
            rectangles.append(self.updates.pop(index))
        update.unionall_ip(rectangles)
        union = True
        while union:
            union = False
            for index in range(len(self.updates)):
                if update.centerx == self.updates[index].centerx:
                    if update.width == self.updates[index].width:
                        if update.top == self.updates[index].bottom or update.bottom == self.updates[index].top:
                            update.union_ip(self.updates.pop(index))
                            union = True
                            break
                elif update.centery == self.updates[index].centery:
                    if update.height == self.updates[index].height:
                        if update.right == self.updates[index].left or update.left == self.updates[index].right:
                            update.union_ip(self.updates.pop(index))
                            union = True
                            break
        self.updates.append(update)
        
        return None