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
        print("Logging in")
        # TODO: Implement login and check against database


user = User("joe", "mama")
user.signup()
