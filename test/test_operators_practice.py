import unittest

class operatorsTest(unittest.TestCase):
    def test_equal_operator(self):
        a = -2
        b = -2
        self.assertFalse(a == b)

    def test_notequal_operator(self):
        a = 6
        b = 7
        self.assertFalse(a != b)

    def test_greaterthan_operator(self):
        a = 8
        b = 7
        self.assertFalse(a > b)

    def test_lessthan_operator(self):
        a = -42
        b = -2
        self.assertFalse(a < b)

    def test_greaterthan_or_equalto_operator(self):
        a = 9
        b = 7
        self.assertFalse(a >= b)

    def test_lessthan_or_equalto_operator(self):
        a = -2
        b = -2
        self.assertFalse(a <= b)


if __name__ == '__main__':
    unittest.main()
