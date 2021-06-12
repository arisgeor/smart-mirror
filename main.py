from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
import test_fing
import random
from max30102_fd.heartrate_monitor import HeartRateMonitor as HRM
con=sql.connect('finger_users.db')
cur=con.cursor()
cur.execute("Create Table IF NOT EXISTS Users (User_id number primary key, E_Date Date);");

def toggle_window(event):
    window.attributes("-fullscreen", False)
    window.geometry("1224x650+50+0")


bgcolor = 'Black'
bg_color1 = 'Black'
text_color = 'white'                        # text colors
font_name = 'Time New Roman'                # font name
window = Tk()                               # Window variable
window.attributes("-fullscreen", True)
window.bind('<Escape>', toggle_window)
# Window Size
window.title("Title")                       # Title
window.config(background=bgcolor)           # Applying background color in window

home_page_title = "Title"
home_page_heading = " Sologon if you have any"


def back():
    main_frame.pack(pady=30)
    Body_frame.pack_forget()




def menu_bar(window_name):
    ######## bar menu
    my_menu = Menu(window_name)
    window_name.config(menu=my_menu)
    window_menu = Menu(my_menu)
    my_menu.add_cascade(label="Window", menu=window_menu)
    window_menu.add_command(label="Maximized", command=lambda: window.attributes('-fullscreen', True))
    window_menu.add_separator()
    window_menu.add_command(label="For Minimized Press Esc key", command=lambda: messagebox.showinfo())
    window_menu.add_separator()
    window_menu.add_command(label="Back", command=lambda: back())
    window_menu.add_separator()
    window_menu.add_command(label="Exit", command=lambda: window.quit())


################

######## Header function ############
def Header_part(window_name, Title, Heading):
    logo_frame = Frame(window_name, bg=bgcolor)
    logo_frame.pack(side=TOP, fill='x')
    logo_text_frame = Frame(logo_frame, bg=bgcolor)
    logo_text_frame.pack(side=LEFT, padx=5)
    Label(logo_text_frame, text=Title, font=(font_name, 28, 'bold', 'italic'), bg=bgcolor,
          fg=text_color).pack(side=TOP, anchor=NW, pady=5)
    Label(logo_text_frame, text=Heading,
          font=(font_name, 16), bg=bgcolor, fg=text_color).pack(side=TOP, pady=2)
    # Labels
    from datetime import datetime
    today_date = datetime.now().strftime('%d-%m-%Y (%A)')
    logo_label = Label(logo_frame, text=today_date, bg=bgcolor, fg=text_color, font=(font_name, 28, 'bold', 'italic'))
    logo_label.pack(side=RIGHT, anchor=NE, padx=5)
    Canvas(window_name, height=10, bg='Red').pack(fill='x')


######## footer function ############

def footer(window_name, footer_text):
    Label(window_name, text=footer_text, font=(font_name, 12), justify=LEFT, bg=bgcolor, fg=text_color).pack(
        side=BOTTOM, anchor=NE, padx=30)
    Canvas(window_name, height=10, bg='Blue').pack(side=BOTTOM, fill='x', pady=5)


#######################

##################################
########## Main Window #########
#################################
menu_bar(window)
Header_part(window, home_page_title, home_page_heading)
main_frame = Frame(window, bg=bgcolor)
main_frame.pack(pady=30)
Label(main_frame, text='MENU', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor, pady=20,
      fg=text_color).pack(side=TOP, pady=10)
Button(main_frame, text='Home', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: body_code()).pack(side=TOP, pady=10)
Button(main_frame, text='Add User', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: add_users()).pack(side=TOP, pady=10)
Button(main_frame, text='Restart', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: None).pack(side=TOP, pady=10)
Button(main_frame, text='Power Off', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: None).pack(side=TOP, pady=10)
Button(main_frame, text='Window maximize', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: window.attributes('-fullscreen', True)).pack(side=TOP, pady=10)

footer(window, 'Contact us | © Copyright arisgeor@ece.auth.gr')
Body_frame = Frame(window, bg=bgcolor)

User_frame = Frame(Body_frame, bg=bgcolor)
User_frame.pack(side=LEFT, padx=30)
Text_frame = Frame(Body_frame, bg=bgcolor)
Text_frame.pack(side=RIGHT, padx=100)
User_id_lb=Label(User_frame, text='Username: User_1', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
      fg=text_color)
User_id_lb.pack(side=TOP, pady=10)
Label(Text_frame, text='Data Analysis', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
      fg=text_color).pack(side=TOP, pady=10)

Heart_rate = Label(Text_frame, text='Heart-rate : 000', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Heart_rate.pack(side=TOP, pady=10)
Sp02 = Label(Text_frame, text='Sp02 : 0000', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Sp02.pack(side=TOP, pady=10)
Temp = Label(Text_frame, text='Temp : 00 C', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Temp.pack(side=TOP, pady=10)
Weight = Label(Text_frame, text='Weight : 00 KG', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Weight.pack(side=TOP, pady=10)


def body_code():
    main_frame.pack_forget()
    import time
    Place_sensor_lb=Label(window, text='Place your finger on the sensor.....', bg=bgcolor, fg=text_color, font=(font_name,45))
    Place_sensor_lb.pack(side=TOP)
    r=test_fing.VerifyUser()
    cur.execute('Select * from Users where user_id=?',(r,))
    res=cur.fetchall()
    if len(res)>0:
        Place_sensor_lb.pack_forget()
        User_id_lb.config(text="Username : "+str(res[0][0]))
        Body_frame.pack(side=TOP, pady=30, fill='x')
        #HRM_data=HRM.run_sensor()
        #HRM.start_sensor()
        #if len(HRM_data)>0:
        if True:
            #Heart_rate.config(text='Heart-rate : '+str(HRM_data[0]))
            #Sp02.config(text='Sp02 : '+str(HRM_data[1]))
            Heart_rate.config(text='Heart-rate : '+str(random.randint(70, 90)))
            Sp02.config(text='Sp02 : '+str(random.randint(95,99)))
    #######################


def add_users():
    new_window = Toplevel()
    new_window.title("New Users")  # Title
    new_window.config(background=bgcolor)  # Applying background color in window
    new_window.geometry('500x400+450+100')
    Label(new_window, text='Place your finger on the scanner after that press start.....')
    frame1 = LabelFrame(new_window, text='Add User', font=(font_name, 18, 'bold'), bg=bgcolor, fg=text_color, padx=80,
                        pady=10)
    frame1.pack(pady=50)
    Label(frame1, text='User ID', font=(font_name, 12, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
          fg=text_color).pack(side=TOP, pady=2)
    User_id = Entry(frame1, font=(font_name, 12), bg='gray', fg=text_color, bd=3)
    User_id.pack(pady=2)
    Label(frame1, text='Username', font=(font_name, 12, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
          fg=text_color).pack(side=TOP, pady=2)
    User_name = Entry(frame1, font=(font_name, 12), bg='gray', fg=text_color, bd=3)
    User_name.pack(pady=2)
    Button(frame1, text='Clear', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
           command=lambda: None).pack(side=TOP, pady=2)
    footer(new_window, 'Contact us | © Copyright by your name or company name')
    r=''#test_fing.AddUser()
    if len(r)>1:
        User_id.insert(0, r[1])
        from datetime import datetime
        con = sql.connect('finger_users.db')
        cur = con.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        cur.execute("insert into Users Values (?,?);", (r[1], today))
        messagebox.showinfo("Success", "User Added Successfully")
        con.commit()
    else:
        Label(new_window, text=r, font=(font_name, 12, 'bold'), bg=bgcolor, fg='red').pack(side=BOTTOM, fill='x')


window.mainloop()
