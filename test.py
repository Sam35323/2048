from logika import ssussyy, playable, move_forward
import unittest


class G2048(unittest.TestCase):
    def test01(self):
        d = [[0, 0000, 0000, 79796213456874680],
             [7, 60, 904, 3453450],
             [46370, 230, 70346, 123023557],
             [99990, -0.9, 235730, 80]]
        a = [(-0, 0), (0, 1), (0, 2)]
        self.assertEqual(ssussyy(d), a)

    def test02(self):
        p = [[0, 3450567000, 30000, 79796213456874680],
             [7, 60, 904, 3453450],
             [46370, 230, 70346, 123023557],
             [99990, -0.9, 235730, 0]]
        b = [(0, 0), (3, 3)]
        self.assertEqual(ssussyy(p), b)

    def test03(self):
        a = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, -0, 0, 0]]
        b = True
        self.assertEqual(playable(a), b)

    def test14(self):
        a = [[2, 4, 0, 4],
             [8, 32, 0, 16],
             [1, 1, 0, 0],
             [0, -0, 0, 0]]
        av = [[0, 0, 2, 8],
              [0, 8, 32, 16],
              [0, 0, 0, 2],
              [0, -0, 0, 0]]
        self.assertEqual(move_forward(a), av)
