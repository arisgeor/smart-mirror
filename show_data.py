import sqlite3 as sql
con = sql.connect('finger_users.db')
cur = con.cursor()
cur.execute("Select * from User_data;");
res=cur.fetchall()
for i in range(len(res)):
    print(res[i])
    print('-----------------------------------')
