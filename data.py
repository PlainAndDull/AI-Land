import world
import player

class Data:
    
    def __init__(self: 'Data') -> 'None':
        
        self.world = world.World()
        self.player = player.Player()
        
        return None