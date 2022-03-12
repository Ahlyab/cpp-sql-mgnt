import db
import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(
            password.encode()).hexdigest()  # hashed password
        self.isLoggedIn = False

    def signup(self):
        db.createUser(self.username, self.password)

    def login(self):
        if(db.getUserPassword(self.username) == self.password):
            print("Login successful")
            self.isLoggedIn = True
        else:
            print("Incorrect password")

    def logout(self):
        self.isLoggedIn = False

    def changePassword(self, newPassword):
        db.changePassword(self.username, hashlib.sha256(
            newPassword.encode()).hexdigest())
