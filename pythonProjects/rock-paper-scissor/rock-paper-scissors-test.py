import unittest
from rock_paper_scissor import game_play


class TestRockPaperScissorMethod(unittest.TestCase):
    def test_player_wins_with_rock(self):
        self.assertEqual(game_play('r', 's'), "You won!!!\nComputer played s!")


if __name__ == "__main__":
    unittest.main()
