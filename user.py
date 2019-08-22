import pandas as pd

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authentificate(self):
        RegistredUserFile = pd.read_csv("Data/UsersFile.csv")
        UserRow = RegistredUserFile[RegistredUserFile["Username"] == self.username]
        if not UserRow.empty:
            if UserRow["Password"].iloc[0] == self.password:
                return "Authentification successful"
            else:
                return "User exists but wrong password"
        else:
            return "User does not exist"