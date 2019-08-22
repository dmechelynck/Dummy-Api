#### The Functio itself:

def Squared_Function(number):
    return number*number

##### Unit testing:

import unittest

class Test_Squared_Fonctiun(unittest.TestCase):
    def test1(self):
        result = Squared_Function(5)
        self.assertEqual(result, 25)

    def test2(self):
        result = Squared_Function(2)
        self.assertEqual(result, 4)
"""
    def test3(self):
        result = Squared_Function(2)
        self.assertEqual(result, 5)
"""

if __name__ == '__main__':
    unittest.main()




