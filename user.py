import db
import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(
            password.encode()).hexdigest()  # hashed password

    def signup(self):
        db.createUser(self.username, self.password)

    def login(self):
        if(db.getUserPassword(self.username) == self.password):
            print("Login successful")
        else:
            print("Incorrect password")
