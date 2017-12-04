import pygame

class Image:
    
    def __init__(self: 'Image', path: 'str', scale: 'int', transparent: 'str') -> 'None':
        
        self.image = pygame.image.load(path).convert()
        self.areas = {}

        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()) * scale, int(self.image.get_height()) * scale))
        self.image.set_colorkey(pygame.Color(transparent))
        
        return None
    
    def get_image(self: 'Image') -> 'Surface':
        
        return self.image
    
    def get_area(self: 'Image', area: 'str') -> 'Rect':
        
        return self.areas[area]
    
    def add_area(self: 'Image', area: 'str', x: 'int', y: 'int', w: 'int', h: 'int') -> 'None':
        
        self.areas[area] = pygame.Rect(x, y, w, h)