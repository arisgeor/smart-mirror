import sqlite3 as sql
import tkMessageBox as messagebox  # python2


def user_data(user_id):
    #inner = ''
    data = ''
    con = sql.connect('finger_users.db')
    cur = con.cursor()
    cur.execute(
              "Select * from User_data where user_id=?;", (user_id,));
    res = cur.fetchall()
    if len(res)>0:
        for i in res:
            data += 'Date: ' + str(i[1]) + ', Heart rate: ' + str(i[2]) + ', SpO2: ' + str(i[3]) + ', Temp: ' + str(i[4]) + ', Weight: ' + str(i[5]) + '/n'
            print data
    	messagebox.showinfo("User " + str(user_id) + " Data", data)
    else:
        messagebox.showinfo("User " + str(user_id) + " Data", "No Data Found...... ")
