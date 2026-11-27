class Player:

    BOARD_SIZE = 12
    COINS_TO_WIN = 6

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.coins = 0
        self.in_penalty_box = False

    def move(self, steps):
        self.position = (self.position + steps) % self.BOARD_SIZE
    def add_coin(self):
            self.coins += 1

    def send_to_penalty_box(self):
         self.in_penalty_box = True

    def has_won(self):
        return self.coins == self.COINS_TO_WIN 
