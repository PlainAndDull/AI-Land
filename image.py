import pygame

class Image:
    
    def __init__(self: 'Image', path: 'str', scale: 'int', transparent: 'str') -> 'None':
        
        self.image = pygame.image.load(path).convert()
        self.areas = {}

        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()) * scale, int(self.image.get_height()) * scale))
        self.image.set_colorkey(pygame.Color(transparent))
        
        return None