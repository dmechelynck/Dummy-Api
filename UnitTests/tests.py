import unittest
from Squared import Squared_Function

class Test_Squared_Fonctiun(unittest.TestCase):
    def test1(self):
        result = Squared_Function(5)
        self.assertEqual(result, 25)

    def test2(self):
        result = Squared_Function(2)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()



