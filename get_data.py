import sqlite3 as sql
import tkMessageBox as messagebox  # python2


def user_data(user_id):
    data = ''
    con = sql.connect('finger_users.db')
    cur = con.cursor()
    cur.execute(
              "Select * from User_data where user_id=?;", (user_id,));
    res = cur.fetchall()
    if len(res)>0:
        for i in res:
            data += 'Data Measured on: ' + str(i[1]) + '\nHeart rate: ' + str(i[2]) + '\nSpO2: ' + str(i[3]) + '\nTemp: ' + str(i[4]) + '\nWeight: ' + str(i[5]) + '\n\n'
    	messagebox.showinfo("User " + str(user_id) + " Data", data)
    else:
        messagebox.showinfo("User " + str(user_id) + " Data", "No Data Found...... ")
