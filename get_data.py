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
            data += 'Date: ' + res[i][1] + ', Heart rate: ' + res[i][2] + ', SpO2: ' + res[i][3] + ', Temp: ' + res[i][4] + ', Weight: ' + res[i][5] + '/n'
    	messagebox.showinfo("User " + user_id + " Data", data)
    else:
        messagebox.showinfo("User " + user_id + " Data", "No Data Found...... ")
