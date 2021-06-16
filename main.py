from Tkinter import *       #python2 
import tkMessageBox         #python2 
import sqlite3 as sql
import test_fing
import test_scale as Scale
from mlx90614.get_temp import get_temp
from max30102_fd.heart_main import heart_sensor as HRM
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
#window.attributes("-fullscreen", True)
window.bind('<Escape>', toggle_window)
# Window Size
window.title("Title")                       # Title
window.config(background=bgcolor)           # Applying background color in window

home_page_title = "Smart-Mirror"
home_page_heading = "Measure yourself"

global after_v
def back():
    global after_v
    main_frame.pack(pady=30)
    print(after_v)
    window.after_cancel(after_v)
    print('cancle')
    Body_frame.pack_forget()


def menu_bar(window_name):
    
    ''' Menu Bar of the Application '''

    my_menu = Menu(window_name)
    window_name.config(menu=my_menu)
    window_menu = Menu(my_menu)
    my_menu.add_cascade(label="Window", menu=window_menu)
    window_menu.add_command(label="Maximized", command=lambda: window.attributes('-fullscreen', True))
    window_menu.add_separator()
    window_menu.add_command(label="For Minimized Press Esc key", command=lambda: tkMessageBox.showinfo('Info', "Press Ecs Key for minimize"))
    window_menu.add_separator()
    window_menu.add_command(label="Back", command=lambda: back())
    window_menu.add_separator()
    window_menu.add_command(label="Exit", command=lambda: window.quit())

def Header_part(window_name, Title, Heading):

    ''' Header function of the Application '''

    logo_frame = Frame(window_name, bg=bgcolor)
    logo_frame.pack(side=TOP, fill='x')
    logo_text_frame = Frame(logo_frame, bg=bgcolor)
    logo_text_frame.pack(side=LEFT, padx=5)
    Label(logo_text_frame, text=Title, font=(font_name, 28, 'bold', 'italic'), bg=bgcolor,
          fg=text_color).pack(side=TOP, anchor=NW, pady=5)
    Label(logo_text_frame, text=Heading,
          font=(font_name, 16), bg=bgcolor, fg=text_color).pack(side=TOP, pady=2)
    #Labels
    from datetime import datetime
    today_date = datetime.now().strftime('%d-%m-%Y (%A)')
    logo_label = Label(logo_frame, text=today_date, bg=bgcolor, fg=text_color, font=(font_name, 28, 'bold', 'italic'))
    logo_label.pack(side=RIGHT, anchor=NE, padx=5)
    Canvas(window_name, height=10, bg='Red').pack(fill='x')


def footer(window_name, footer_text):

    ''' Footer function of the Application '''

    Label(window_name, text=footer_text, font=(font_name, 12), justify=LEFT, bg=bgcolor, fg=text_color).pack(
        side=BOTTOM, anchor=NE, padx=30)
    Canvas(window_name, height=10, bg='Blue').pack(side=BOTTOM, fill='x', pady=5)


#*********************************************************************************
#********************************** Main Window **********************************
#*********************************************************************************

menu_bar(window)
Header_part(window, home_page_title, home_page_heading)
main_frame = Frame(window, bg=bgcolor)
main_frame.pack(pady=30)
Label(main_frame, text='MENU', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor, pady=20,
      fg=text_color).pack(side=TOP, pady=10)
Button(main_frame, text='Login', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: body_code()).pack(side=TOP, pady=10)
Button(main_frame, text='Add User', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: add_users()).pack(side=TOP, pady=10)
Button(main_frame, text='Delete users', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: Del_all_user()).pack(side=TOP, pady=10)
Button(main_frame, text='Power Off', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: window.quit()).pack(side=TOP, pady=10)
Button(main_frame, text='Window maximize', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: window.attributes('-fullscreen', True)).pack(side=TOP, pady=10)

footer(window, 'Contact us | Copyright arisgeor@ece.auth.gr')
Body_frame = Frame(window, bg=bgcolor)

User_frame = Frame(Body_frame, bg=bgcolor)
User_frame.pack(side=LEFT, padx=30)
Text_frame = Frame(Body_frame, bg=bgcolor)
Text_frame.pack(side=RIGHT, padx=100)
User_id_lb=Label(User_frame, text='UserId: User_1', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
      fg=text_color)
User_id_lb.pack(side=TOP, pady=10)
Button(User_frame, text='Home', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: back()).pack(side=TOP, pady=10)

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
Btserial_Scale=Scale.connect_scale()

def body_code():
    main_frame.pack_forget()
    import time
    Place_sensor_lb=Label(window, text='Place your finger on the sensor.....', bg=bgcolor, fg=text_color, font=(font_name,45))
    
    r=test_fing.VerifyUser()
    print(r)
    cur.execute('Select * from Users where user_id=?',(r,))
    res=cur.fetchall()
    if len(res)>0:
        Place_sensor_lb.pack_forget()
        Body_frame.pack(side=TOP, pady=30, fill='x')

        if True:
            tkMessageBox.showinfo('Info',"Place you finger on Heart Scanner.... /nand press ok...")
            HRM_data=HRM()
            Heart_rate.config(text='Heart-rate : '+str(HRM_data[0]))
            Sp02.config(text='Sp02 : '+str(HRM_data[1]))
            show_values_of_sensors()
    else:
	Place_sensor_lb.pack_forget()
	Body_frame.pack_forget()
	main_frame.pack(pady=30)

def show_values_of_sensors():

    ''' Display the current values of all the Sensors '''

    global after_v
    Temp_value=get_temp()
    Scale_value=Scale.get_scale(Btserial_Scale, 5.0)
    Temp.config(text='Temp : '+str(Temp_value) + ' C')
    Weight.config(text='Weight : '+str(Scale_value) + ' Kg')
    after_v=window.after(1000, show_values_of_sensors)
    print(after_v)

def add_users():
    '''
    new_window = Toplevel()
    new_window.title("New User")  # Title
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
    footer(new_window, 'Contact us | Copyright by your name or company name')
    '''

    response = tkMessageBox.askyesno("Confirmation", "Place the finger on the sensor and click on the yes button to continue")

    if response == 1:
        r = test_fing.AddUser()
        print('The id is =>  ', r[1])
        cur.execute('select * from users where user_id=?;',(r[1],))
        res=cur.fetchall()
        if len(res)>0:
            #messagebox.showwarning("Failed:", 'User Id already exists !')
            tkMessageBox.showwarning("Failed:", 'User Id already exists !')
        else:
            if r[1]>=0:
                #User_id.insert(0,r[1])
                from datetime import datetime
                today = datetime.now().strftime('%Y-%m-%d')
                cur.execute("insert into users (user_id, E_date) Values (?,?);", (r[1], today))
                tkMessageBox.showinfo("Success", "User Added Successfully user id = "+ str(r[1]))
                con.commit()
            elif r[1]==-1:
                tkMessageBox.showwarning("Failed:", "Time Out !")
            elif r[1]==-2:
                tkMessageBox.showerror("Error:", "Please try to place the center of the fingerprint flat to sensor, or this fingerprint already exists !")

def Del_all_user():

    ''' Delets all the Users from the Application's database, as well as the Fingerprint sensor's '''

    response = tkMessageBox.askyesno("Warning", "This will erase all the User id's do you want to continue...")
    if response==1:
        test_fing.ClearAllUser()
        cnt_user=test_fing.GetUserCount()
        cur.execute('Delete from users;')
        con.commit();
        tkMessageBox.showinfo('info','Successfully deleted remaining users = '+ str(cnt_user))

window.mainloop()
