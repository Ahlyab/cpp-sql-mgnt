import db
import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(
            password.encode()).hexdigest()  # hashed password

    def signup(self):
        if(db.checkIfUserExists(self.username)):
            print("User already exists")
        else:
            db.createUser(self.username, self.password)
            print("User created")

    def login(self):
        if(db.checkIfUserExists(self.username)):
            if(db.getUserPassword(self.username) == self.password):
                print("Login successful")
            else:
                print("Incorrect password")
        else:
            print("User does not exist")
