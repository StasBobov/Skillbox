import unittest
from lesson_014 import bowling


class BowlingTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(bowling.get_score('12X34-/1744XX23--'), 106)

    def test_max_scores(self):
        self.assertEqual(bowling.get_score('XXXXXXXXXX'), 200)

    def test_no_scores(self):
        self.assertEqual(bowling.get_score('--------------------'), 0)

    def test_2(self):
        self.assertEqual(bowling.get_score('1-X34-/1744XX32--'), 104)

    def test_3(self):
        self.assertEqual(bowling.get_score('-1X34-/1744XX32--'), 104)


if __name__ == "__main__":
    unittest.main()