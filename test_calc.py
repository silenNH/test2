import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(-1, 1), 5)
        self.assertEqual(calc.add(-1, -1), -2)


#if __name__ == '__main__':
#    unittest.main()