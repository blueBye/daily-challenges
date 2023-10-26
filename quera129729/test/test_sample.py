import unittest
import sys
sys.path.append('../Initial_project')
from chain import Chain

class TestFind(unittest.TestCase):
    def test0(self):
        self.assertEqual(Chain(-2.5)(2)(-2)(2.5), 0)
    
    def test1(self):
        self.assertEqual(Chain(3)(1.5)(2)(3), 9.5)

    def test2(self):
        self.assertEqual(Chain(64), 64)

    def test3(self):
        self.assertEqual(Chain('Ali')('Safinal')('is')('the')('best.'), 'Ali Safinal is the best.')

    def test4(self):
        self.assertEqual(Chain('abc')('defg'), 'abc defg')

    def test5(self):
        with self.assertRaises(Exception) as e:
            Chain('Ali')(5)
        self.assertTrue("invalid operation" in str(e.exception))

    def test6(self):
        with self.assertRaises(Exception) as e:
            Chain(9)([1, 2])
        self.assertTrue("invalid operation" in str(e.exception))

    def test7(self):
        with self.assertRaises(Exception) as e:
            Chain(0)('5')
        self.assertTrue("invalid operation" in str(e.exception))

    def test8(self):
        self.assertEqual(Chain(64) == 64, True)

    def test9(self):
        self.assertEqual(Chain('abc')('defg') == 'abc defg', True)

    def test10(self):
        with self.assertRaises(Exception) as e:
            Chain([0, 1])
        self.assertTrue("invalid operation" in str(e.exception))

    def test11(self):
        with self.assertRaises(Exception) as e:
            Chain(True)
        self.assertTrue("invalid operation" in str(e.exception))

    def test12(self):
        with self.assertRaises(Exception) as e:
            Chain()
        self.assertTrue("invalid operation" in str(e.exception))

if __name__ == '__main__':
    unittest.main()