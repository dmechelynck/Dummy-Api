import pandas as pd
import os

dirpath = os.path.dirname(os.path.realpath(__file__))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authentificate(self):
        RegistredUserFile = pd.read_csv(dirpath+"/Data/UsersFile.csv")
        UserRow = RegistredUserFile[RegistredUserFile["Username"] == self.username]
        if not UserRow.empty:
            if UserRow["Password"].iloc[0] == self.password:
                return "Authentification successful"
            else:
                return "User exists but wrong password"
        else:
            return "User does not exist"


##### Unit testing:

import unittest

class Test_User_Class(unittest.TestCase):
    def test1(self):
        User1=User("Diego", "Agilytic123")
        result = User1.authentificate()
        self.assertEqual(result, "Authentification successful")

    def test2(self):
        User2=User("Diego9", "Agilytic123")
        result = User2.authentificate()
        self.assertEqual(result, "User does not exist")

    def test3(self):
        User3=User("Diego", "Agilytic123u")
        result = User3.authentificate()
        self.assertEqual(result, "User exists but wrong password")

if __name__ == '__main__':
    unittest.main()