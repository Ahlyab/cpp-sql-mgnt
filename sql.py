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
for row in cur.execute("SELECT * FROM user"):
    print(f"Username : {row[0]} \nPassword : {row[1]}" )
    print("----------------------------------")

tuple1 = ("car", "bike", "bus")
print(tuple1)

con.commit()
con.close()