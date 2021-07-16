import unittest
import rock_paper_scissor


class TestRockPaperScissorMethod(unittest.TestCase):
    def test_player_wins_rock(self):
        self.assertEqual(rock_paper_scissor.game_play(
            'r', 's'), "You won!!!\nComputer played s!")

    def test_player_loses_rock(self):
        self.assertEqual(rock_paper_scissor.game_play(
            'r', 'r'), "It's a tie!!!Computer also played r!")

    def test_player_tie_rock(self):
        self.assertEqual(rock_paper_scissor.game_play(
            'r', 'p'), "You lost!!!\n\\\\\\\\Computer played p!\\\\\\\\")

    def test_player_wins_paper(self):
        self.assertEqual(rock_paper_scissor.game_play(
            'p', 'r'), "You won!!!\nComputer played r!")

    def test_player_tie_paper(self):
        self.assertEqual(rock_paper_scissor.game_play(
            'p', 'p'), "It's a tie!!!Computer also played p!")

    def test_player_loses_paper(self):
        self.assertEqual(rock_paper_scissor.game_play(
            'p', 's'), "You lost!!!\n\\\\\\\\Computer played s!\\\\\\\\")

    def test_player_loses_scissors(self):
        self.assertEqual(rock_paper_scissor.game_play(
            's', 'r'), "You lost!!!\n\\\\\\\\Computer played r!\\\\\\\\")

    def test_player_wins_scissors(self):
        self.assertEqual(rock_paper_scissor.game_play(
            's', 'p'), "You won!!!\nComputer played p!")

    def test_player_tie_scissors(self):
        self.assertEqual(rock_paper_scissor.game_play(
            's', 's'), "It's a tie!!!Computer also played s!")

    def test_player_no_input(self):
        self.assertEqual(rock_paper_scissor.play(''), 'x')


if __name__ == "__main__":
    unittest.main()
