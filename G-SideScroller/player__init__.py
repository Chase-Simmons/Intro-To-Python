class Player:
    def __init__(self):
        self.moving_right = False
        self.moving_left = False
        self.grounded = True
        self.x = 50
        self.y = 50
        self.vertical_momentum = 0
