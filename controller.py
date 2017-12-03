import pygame

class Controller:
    
    def __init__(self: 'Controller') -> 'None':
        
        self.quit = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.QUIT)
        
        return None
    
    def update(self: 'Controller') -> 'None':
        
        event = pygame.event.poll()
        pressed = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT:
            
            self.quit = True
            
        self.up = pressed[pygame.K_UP]
        self.down = pressed[pygame.K_DOWN]
        self.left = pressed[pygame.K_LEFT]
        self.right = pressed[pygame.K_RIGHT]
        
        return None