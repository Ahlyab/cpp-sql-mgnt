import db


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signup(self):
        print("Signing up")
        # TODO: Implement signup and save to database

    def login(self):
        print("Logging in")
        # TODO: Implement login and check against database
