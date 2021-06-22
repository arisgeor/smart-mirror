from Tkinter import *   # python2
import tkMessageBox     # python2
import sqlite3 as sql
import test_fing
import test_scale as Scale
from mlx90614.get_temp import get_temp
from max3010x.heart_main import heart_sensor as HRM
from datetime import datetime
con = sql.connect('finger_users.db')            # Creates Database 
cur = con.cursor()
cur.execute(
    "Create Table IF NOT EXISTS Users (User_id number primary key, E_Date Date);");

cur.execute(                                    # Creates Table
    "Create Table IF NOT EXISTS User_data (User_id number, E_Date Date, heart_rate number, sp02 number, temp number, weight number);");



def toggle_window(event):
    ''' Exit Fullscreen mode when you press the Esc key '''
    window.attributes("-fullscreen", False)
    window.geometry("1224x650+50+0")


bgcolor = 'Black'               # Background colors for the different frames used.
bg_color1 = 'Black'
text_color = 'white'            # text colors
font_name = 'Time New Roman'    # font name

window = Tk()                           # Window variable that holds the entire App.
window.title("Smart Mirror")            # Application Title appearint at the top of the window
window.attributes("-fullscreen", True)
window.config(background=bgcolor)       # Applying background color in window.
window.bind('<Escape>', toggle_window)  # Use the Escape Button to exit Fullscreen Mode through toggle_window().

home_page_title = "Smart-Mirror"
home_page_motto = "Biometric Measuring Device"
footer_text = "Contact me: arisgeor@ece.auth.gr"

global after_v, user_id, values
values=[]

def home():
    ''' 
    Function that returns the User to the Home (main) screen,
    and saves the recorded biomarkers in the Database.
    '''
    global after_v
    main_frame.pack(pady=30)                
    print(after_v)
    print('Cancel')
    Body_frame.pack_forget()                
    window.after_cancel(after_v)
    print(str(values[0]),'Date',str(values[1]),str(values[2]),str(values[-2]),str(values[-1]))
    cur_date=datetime.now().strftime('%y-%m-%d %H:%M:%S')
    cur.execute("insert into User_data (user_id,E_date,Heart_rate,sp02,temp,weight) values (?,?,?,?,?,?)",(values[0],cur_date,values[1],values[2], values[-2], values[-1]))
    con.commit()
    print('Data saved into DB Successfully...')

def Test_again(u_id):
    ''' 
    Function that executes after user clicks the "Test Again" Button.
    Lets the user repeat the measuremenent and reaquire his/her biomarkers, 
    without returning to the HOME tab.
    This function takes as an argument the user's ID, in order to repeat the measurement
    and save the Data under the same User. 
    '''
    global values
    tkMessageBox.showinfo('Info', "Place you finger on Heart Scanner.... \nand press ok...")
    values=[]
    HRM_data = HRM()
    Sp02_value=round(HRM_data[1],2)
    Heart_rate.config(text='Heart-rate : ' + str(HRM_data[0]))
    Sp02.config(text='Sp02 : ' + str(Sp02_value))
    values.append(u_id)
    values.append(HRM_data[0])
    values.append(Sp02_value)
    print(values)

def menu_bar(window_name):
    ''' Menu Bar of the Application (Top Left) Containing usufull options'''

    my_menu = Menu(window_name)
    window_name.config(menu=my_menu)
    window_menu = Menu(my_menu)
    my_menu.add_cascade(label="Window", menu=window_menu)
    window_menu.add_command(label="Maximize", command=lambda: window.attributes('-fullscreen', True))
    window_menu.add_separator()
    window_menu.add_command(label="Press Esc Key to Minimize",
                            command=lambda: tkMessageBox.showinfo('Info', "Press Esc Key to Minimize")) ###########
    window_menu.add_separator()
    window_menu.add_command(label="Back", command=lambda: home())
    window_menu.add_separator()
    window_menu.add_command(label="Exit", command=lambda: window.quit())


def Header_part(window_name, Title, Motto):
    ''' 
    Function that sets the header part of the Application.
    Creates the logo and text frames and places the 3 labels
    containing the Title, Motto and Date of the App. 
    '''

    logo_frame = Frame(window_name, bg=bgcolor)     
    logo_frame.pack(side=TOP, fill='x')
    logo_text_frame = Frame(logo_frame, bg=bgcolor)
    logo_text_frame.pack(side=LEFT, padx=5)
    # Labels
    Label(logo_text_frame, text=Title, font=(font_name, 28, 'bold', 'italic'), bg=bgcolor,
          fg=text_color).pack(side=TOP, anchor=NW, pady=5)
    Label(logo_text_frame, text=Motto,
          font=(font_name, 16), bg=bgcolor, fg=text_color).pack(side=TOP, pady=2)
    today_date = datetime.now().strftime('%d-%m-%Y (%A)')
    logo_label = Label(logo_frame, text=today_date, bg=bgcolor, fg=text_color, font=(font_name, 28, 'bold', 'italic'))
    logo_label.pack(side=RIGHT, anchor=NE, padx=5)
    Canvas(window_name, height=2, bg='Red').pack(fill='x')

def footer(window_name, footer_text):
    ''' 
    Footer function of the Application. 
    Places the footer_text at the bottom of the screen.
    '''

    Label(window_name, text=footer_text, font=(font_name, 12), justify=LEFT, bg=bgcolor, fg=text_color).pack(
        side=BOTTOM, anchor=NE, padx=30)
    Canvas(window_name, height=2, bg='Blue').pack(side=BOTTOM, fill='x', pady=5)


# ************************************* #
# ************ Main Window ************ #
# ************************************* #

menu_bar(window)
Header_part(window, home_page_title, home_page_motto)
main_frame = Frame(window, bg=bgcolor)                  # Creates the "HOME" main_frame.
main_frame.pack(pady=30)                                # places it.

Button(main_frame, text='Login', font=(font_name, 12, 'bold'), width=15, bg='black', fg=text_color, bd=3,
       command=lambda: body_code()).pack(side=TOP, pady=10)
Button(main_frame, text='Add User', font=(font_name, 12, 'bold'), width=15, bg='black', fg=text_color, bd=3,
       command=lambda: add_users()).pack(side=TOP, pady=10)
Button(main_frame, text='Delete All Users', font=(font_name, 12, 'bold'), width=15, bg='black', fg=text_color, bd=3,
       command=lambda: Del_all_user()).pack(side=TOP, pady=10)
Button(main_frame, text='Power Off', font=(font_name, 12, 'bold'), width=15, bg='black', fg=text_color, bd=3,
       command=lambda: window.quit()).pack(side=TOP, pady=10)
Button(main_frame, text='Window maximize', font=(font_name, 12, 'bold'), width=15, bg='black', fg=text_color, bd=3,
       command=lambda: window.attributes('-fullscreen', True)).pack(side=TOP, pady=10)

footer(window, footer_text)

# After User logs in:
Body_frame = Frame(window, bg=bgcolor)      # Body_frame is created within window but not placed yet.
                                            # It will be placed when the user successfuly logs in.
User_frame = Frame(Body_frame, bg=bgcolor)  # User_frame is created within Body_frame.
User_frame.pack(side=LEFT, padx=30)

Text_frame = Frame(Body_frame, bg=bgcolor)  # and Text_frame is created within Body_Frame.
Text_frame.pack(side=RIGHT, padx=100)

# Inside User_frame:
User_id_lb = Label(User_frame, text='User Id: ????', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
                   fg=text_color)
User_id_lb.pack(side=TOP, pady=10)
Button(User_frame, text='Home', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: home()).pack(side=TOP, pady=10)
Button(User_frame, text='Test Again', font=(font_name, 12, 'bold'), width=15, bg='gray', fg=text_color, bd=3,
       command=lambda: Test_again(user_id)).pack(side=TOP, pady=10)

# Inside Text_frame:
Label(Text_frame, text='Current Biometrics:', font=(font_name, 20, 'bold', 'italic'), justify=LEFT, bg=bgcolor,
      fg=text_color).pack(side=TOP, pady=10)
Heart_rate = Label(Text_frame, text='Heart-rate : 000', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Heart_rate.pack(side=TOP, pady=10)
Sp02 = Label(Text_frame, text='Sp02 : 0000', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Sp02.pack(side=TOP, pady=10)
Temp = Label(Text_frame, text='Temp : 00 C', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Temp.pack(side=TOP, pady=10)
Weight = Label(Text_frame, text='Weight : 00 Kg', font=(font_name, 20), justify=LEFT, bg=bgcolor, fg=text_color)
Weight.pack(side=TOP, pady=10)
try:
    Btserial_Scale = Scale.connect_scale()  # Connect the scale.
except ValueError as e:
    tkMessageBox.showerror('Error:', e)


def body_code():
    ''' 
    App Screen After User Clicks the "Log In" Button 
    Contains all possible scenarios of Verification 
    and pops up the approporiate message
    '''

    global user_id
    main_frame.pack_forget()                                # Hides the "Home Screen" and pops up the message below.
    Place_sensor_lb = Label(window, text='Place your finger on the sensor.....', bg=bgcolor, fg=text_color,
                            font=(font_name, 45))
    r = test_fing.VerifyUser()
    print(r)
    user_id=r[1]
    if r[1] >= 0:                                           # User is successfully verified.
        Place_sensor_lb.pack_forget()
        User_id_lb.config(text='User Id = ' + str(r[1]))    # Hides the pop up notification.
        Body_frame.pack(side=TOP, pady=30, fill='x')        # Places the Body_frame containing the measurements.

        if True:
            Test_again(user_id)
            show_values_of_sensors()
    else:                                                   # Verification failed.
        Place_sensor_lb.pack_forget()                       # Hides the pop up notification.
        Body_frame.pack_forget()                            # Hides the Body_frame.
        main_frame.pack(pady=30)                            # Puts the main_frame back in place.
        if r[1] == -1:
            tkMessageBox.showwarning('Failed', "Time Out... !")
        elif r[1] == -3:
            tkMessageBox.showwarning('Failed', "No User Found... !")
        elif r[1] == -2:
            tkMessageBox.showerror("Failed:", "Please try to place the center of the fingerprint flat to sensor !")

def show_values_of_sensors():
    ''' Display the current values of all the Sensors '''

    global after_v, user_id, values
    try:
	Btserial_Scale = Scale.connect_scale()  # Connect the scale
        Temp_value = get_temp()
        Scale_value = Scale.get_scale(Btserial_Scale, 5.0)  # Get scale Value and set weigth Threshhold.
        Temp_value=round(Temp_value,2)
        Scale_value= round(float(Scale_value),2)
        Temp.config(text='Temp : ' + str(Temp_value) + ' C')  # Update Temperature value.
        Weight.config(text='Weight : ' + str(Scale_value) + ' Kg')  # Update Weight value.
        #cur.execute("update users set temp=?, weight=? where user_id=?",(Temp_value, Scale_value, user_id))
        #con.commit()
        print("data saved.................")
        after_v = window.after(1000, show_values_of_sensors)  # Each second call "show_values_of_sensors" again.
        values.append(Temp_value)
        values.append(Scale_value)
    except ValueError as err:
        tkMessagebox.showerror('Error', err)


def add_users():
    '''
    Function that initiates the procedure of adding a 
    new user to the Smart Mirror.
    '''

    response = tkMessageBox.askyesno("Confirmation",
                                     "Place the finger on the sensor and click on the yes button to continue")

    if response == 1:
        r = test_fing.AddUser()
        print('The id is =>  ', r[1])
        cur.execute('select * from users where user_id=?;', (r[1],))
        res = cur.fetchall()
        if len(res) > 0:                            # User already exists.
            tkMessageBox.showwarning("Failed:", 'User Id already exists !')
        else:
            if r[1] >= 0:
                from datetime import datetime
                today = datetime.now().strftime('%Y-%m-%d')
                cur.execute("insert into users (user_id, E_date) Values (?,?);", (r[1], today))
                tkMessageBox.showinfo("Success", "User %d Added Successfully!" % (r[1]))
                con.commit()
            elif r[1] == -1:
                tkMessageBox.showwarning("Failed:", "Time Out !")
            elif r[1] == -2:
                tkMessageBox.showerror("Error:",
                                       "Please try to place the center of the fingerprint flat to sensor, or this fingerprint already exists !")


def Del_all_user():
    ''' Delets all the Users from the Application's as well as the Fingerprint sensor's Databases'''

    response = tkMessageBox.askyesno("Warning", "This will erase all the User id's do you wish to continue?")
    if response == 1:
        test_fing.ClearAllUser()
        cnt_user = test_fing.GetUserCount()
        cur.execute('Delete from users;')
        con.commit();
        tkMessageBox.showinfo('info', 'Successfully deleted remaining users = ' + str(cnt_user))


window.mainloop()  # execute App.
