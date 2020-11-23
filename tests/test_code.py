from code import somar, subtract, inner_product
import numpy as np
import unittest

class CodeTestCase(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(1,2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(2,1), 1)

    def test_inner_product(self):
        v = np.array([9,10])
        w = np.array([11, 12])
        result = 9*11 + 10*12
        self.assertEqual(inner_product(v,w), result)



if __name__ == "__main__":
    unittest.main(verbosity=1)
