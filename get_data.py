import sqlite3 as sql
import tkMessageBox as messagebox  # python2


def user_data(user_id):
    con = sql.connect('finger_users.db')
    cur = con.cursor()
    cur.execute(
              "Select * from User_data where user_id=?;", (user_id,));
    res = cur.fetchall()
    if len(res)>0:
    	messagebox.showinfo("Data !", res)
    else:
        messagebox.showinfo("Data !", "No Data Found...... ")
