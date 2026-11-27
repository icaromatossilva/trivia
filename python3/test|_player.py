from player import Player

def test_new_player():
    p = Player("Chet")
    assert (p.position, p.coins, p.in_penalty_box) == (0, 0, False)

def test_move_avanca():
    p = Player("Sheila")
    p.move(3)
    assert p.position == 3

def test_volta_no_tabuleiro():
    p = Player("Sue")
    p.position = 10
    p.move(5)
    assert p.position == 3

def test_vitoria():
    p = Player("Chet")
    for _ in range(5):
        p.add_coin()
    assert not p.has_won()
    p.add_coin()
    assert p.has_won()
    
def test_penalty_box():
    p = Player("Pat")
    p.send_to_penalty_box()
    assert p.in_penalty_box
