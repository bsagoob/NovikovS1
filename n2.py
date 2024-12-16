import unittest
import numpy as np


def mnk(x, y):
    X = np.vstack([x, np.ones(len(x))]).T
    beta = np.linalg.inv(X.T @ X) @ X.T @ y
    return beta[0], beta[1]


class TestMNK(unittest.TestCase):
    def test_1(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        slope, intercept = mnk(x, y)
        self.assertAlmostEqual(slope, 2.0)
        self.assertAlmostEqual(intercept, 0.0)

    def test_2(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2.1, 3.9, 6.2, 7.8, 9.9])
        slope, intercept = mnk(x, y)
        self.assertAlmostEqual(slope, 1.98, places=2)
        self.assertAlmostEqual(intercept, 0.08, places=2)

    def test_3(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 8, 6, 4, 2])
        slope, intercept = mnk(x, y)
        self.assertAlmostEqual(slope, -2.0)
        self.assertAlmostEqual(intercept, 12.0)

    def test_4(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([1, 2, 3, 4, 5])
        slope, intercept = mnk(x, y)
        self.assertAlmostEqual(slope, 1.0)
        self.assertAlmostEqual(intercept, 0.0)

    def test_5(self):
        x = np.array([1])
        y = np.array([2])
        with self.assertRaises(np.linalg.LinAlgError):
            mnk(x, y)

    def test_6(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 2, 2, 2, 2])
        slope, intercept = mnk(x, y)
        self.assertAlmostEqual(slope, 0.0)
        self.assertAlmostEqual(intercept, 2.0)


if __name__ == '__main__':
    unittest.main()
