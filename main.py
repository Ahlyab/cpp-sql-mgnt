from user import User
import db
from hashlib import sha256

print("""
Welcome! Please choose an option:
1. Sign in
2. Sign up
3. Exit
""")

choice = int(input("Enter your choice: "))

if choice != 1 and choice != 2 and choice != 3:
    print("Invalid choice")
    exit()

username = input("Enter your username: ")


if choice == 3:
    exit()
elif(choice == 1):
    if(db.checkIfUserExists(username)):
        password = input("Enter your password: ")
        user = User(username, password)
        user.login()
    else:
        print("User does not exist. Please sign up first.")
        exit()
elif(choice == 2):
    if(db.checkIfUserExists(username)):
        print("User already exists")
        exit()
    else:
        password = input("Enter your password: ")
        user = User(username, password)
        user.signup()

print("""Thank you for using our service. What would you like to do next?
1. Change password
2. Log out
""")

choice = int(input("Enter your choice: "))
if choice == 1:
    oldPassword = input("Enter your old password: ")
    if(user.password == sha256(oldPassword.encode()).hexdigest()):
        newPassword = input("Enter your new password: ")
        user.changePassword(newPassword)
elif choice == 2:
    user.logout()
