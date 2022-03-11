import user

print("""
Welcome! Please choose an option:
1. Sign in
2. Sign up
""")

choice = int(input("Enter your choice: "))

if choice != 1 and choice != 2:
    print("Invalid choice")
    exit()

username = input("Enter your username: ")

if(choice == 1):
    if(user.db.checkIfUserExists(username)):
        password = input("Enter your password: ")
        user.User(username, password).login()
    else:
        print("User does not exist. Please sign up first.")
elif(choice == 2):
    if(user.db.checkIfUserExists(username)):
        print("User already exists")
    else:
        password = input("Enter your password: ")
        user.User(username, password).signup()
