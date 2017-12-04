import pygame

class Clock:
    
    def __init__(self: 'Clock') -> 'None':
        
        self.clock = pygame.time.Clock()
        
        return None
    
    def tick(self: 'Clock', framerate: 'int') -> 'None':
        
        self.clock.tick(framerate)
        
        return None