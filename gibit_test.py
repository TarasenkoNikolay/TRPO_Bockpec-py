import unittest

from main import Gibit


class MyTestCase(unittest.TestCase):
    def test_gibit_load(self):
        g = Gibit()
        self.assertIsNotNone(g)
        self.assertIsNotNone(g.man)
        self.assertIsNotNone(g.word)


if __name__ == '__main__':
    unittest.main()
