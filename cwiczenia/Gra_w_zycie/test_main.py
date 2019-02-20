from main import Game, Life


def test_possible_to_emerge():
    game = Game()
    game.add_lives(Life(0, 0))
    game.add_lives(Life(1, 0))
    game.add_lives(Life(2, 1))

    assert len(game.get_possible_to_emerge()) == 17
