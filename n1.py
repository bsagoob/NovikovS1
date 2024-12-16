Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
... 
... 
... def p(n, d=2):
...     if not isinstance(n, int):
...         raise TypeError("n must be int")
...     if n == 1:
...         return []
... 
...     if n % d == 0:
...         return [d] + p(n // d, d)
...     else:
...         return p(n, d + 1)
... 
... 
... class TestPrimeFactors(unittest.TestCase):
...     def test_type_error(self):
...         with self.assertRaises(TypeError):
...             p("not an int")
... 
...     def test_1(self):
...         self.assertEqual(p(1), [])
... 
...     def test_2(self):
...         self.assertEqual(p(2), [2])
... 
...     def test_3(self):
...         self.assertEqual(p(3), [3])
... 
...     def test_4(self):
...         self.assertEqual(p(4), [2, 2])
... 
...     def test_5(self):
...         self.assertEqual(p(6), [2, 3])
... 
...     def test_6(self):
...         self.assertEqual(p(8), [2, 2, 2])

    def test_7(self):
        self.assertEqual(p(10), [2, 5])

    def test_8(self):
        self.assertEqual(p(15), [3, 5])

    def test_9(self):
        self.assertEqual(p(28), [2, 2, 7])

    def test_10(self):
        self.assertEqual(p(30), [2, 3, 5])

    def test_11(self):
        self.assertEqual(p(100), [2, 2, 5, 5])

    def test_12(self):
        self.assertEqual(p(101), [101])


if __name__ == '__main__':
    unittest.main()
