

class Player:
    def __init__(self):
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.grounded = False
        self.x = 50
        self.y = 50
        self.vertical_momentum = 0


def jump(player):
    jump_state = [1, 2, 3]
    player.jumping = False
    print(player)
