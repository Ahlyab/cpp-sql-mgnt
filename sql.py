import sqlite3

con = sqlite3.connect('test.db')
print("DataBase connection Successful")
cur = con.cursor()
print("Cursor created successful")
#curr.execute('''CREATE TABLE (user TEXT, password TEXT);''')
cur.execute('''CREATE TABLE IF NOT EXISTS  user
               (user_id text, password text);''')
print("Table Created Successful \n")

n = int(input("Enter number of users : "))

for i in range(0, n):
    uname = input("Enter username : ")
    upass = input("Enter your password : ")

    cur.execute(f"INSERT INTO user VALUES ('{uname}', '{upass}');")
    print("information inserted successfully")

#printing rows
for row in cur.execute("SELECT user_id FROM user"):
    print(row)

#cur.execute("DROP TABLE user")

con.commit()
con.close()