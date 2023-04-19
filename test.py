from logika import *
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

    def test_11(self):
        mas = [[2, 2, 0, 0],
               [0, 4, 4, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        rez = [[4, 0, 0, 0],
               [8, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        self.assertEqual(move_left(mas), (rez, 12))

    def test_12(self):
        mas = [[2, 4, 4, 2],
               [4, 0, 0, 2],
               [0, 32, 0, 0],
               [8, 8, 4, 4]]
        rez = [[2, 8, 2, 0],
               [4, 2, 0, 0],
               [32, 0, 0, 0],
               [16, 8, 0, 0]]
        self.assertEqual(move_left(mas), (rez, 32))

    def test_13(self):
        mas = [[2, 4, 4, 2],
               [4, 0, 0, 2],
               [0, 4, 0, 0],
               [8, 4, 4, 0]]
        rez = [[2, 8, 8, 4],
               [4, 4, 0, 0],
               [8, 0, 0, 0],
               [0, 0, 0, 0]]
        self.assertEqual(move_up(mas), (rez, 20))

    def test_14(self):
        mas = [[2, 4, 4, 2],
               [4, 4, 0, 2],
               [4, 4, 2, 2],
               [8, 4, 4, 0]]
        rez = [[2, 8, 4, 4],
               [8, 8, 2, 2],
               [8, 0, 4, 0],
               [0, 0, 0, 0]]
        self.assertEqual(move_up(mas), (rez, 28))