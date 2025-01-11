from tkinter import *
from tkinter import ttk
from time import strftime #For displaying real Time and Date
from PIL  import ImageTk,Image #For adding background image
import webbrowser
import subprocess
import os

# Create the main window
root = Tk()
root.title("Home")
root.iconbitmap('home.ico')
root.geometry("626x470")
root.resizable(FALSE,FALSE)

#Background Image
path=Image.open('back.jpg')
back=ImageTk.PhotoImage(path)
lbl=Label(root,image=back,height=470,width=626)
lbl.place(relheight=1,relwidth=1)


# Function to update the time
def time_update():
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%A, %d %B')
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    time_label.after(1000, time_update)

#Function to open Google.com website
def open_clock():
    subprocess.Popen("start ms-clock:",shell=True)

def open_camera():
    subprocess.Popen("start microsoft.windows.camera:",shell=True)

def open_calendar():
    subprocess.Popen("start outlookcal:",shell=True)

def open_calculator():
    subprocess.Popen("calc.exe")

def open_google():
    webbrowser.open('https://www.google.com')

# Time Label
time_label = Label(root, font=('Script MT Bold', 40),fg='#095b61',highlightthickness=0,bg='#000206')
time_label.pack(pady=(30, 10))

# Date Label
date_label = Label(root, font=('Script MT Bold', 20),bg='#000206',fg='#095b61')
date_label.pack(pady=(0, 30))

# Frame to hold the app buttons
button_frame = Frame(root,bg='#061b20',height=10,width=32)
button_frame.pack()

# Load icons for buttons
clock_icon=PhotoImage(file='clock.png')
camera_icon=PhotoImage(file='camera.png')
cal_icon=PhotoImage(file='calculator.png')
calender_icon=PhotoImage(file='calendar2.png')
google_icon=PhotoImage(file='chrome.png')

# Create the buttons with icons
icons=[
    (clock_icon),
    (camera_icon),
    (cal_icon),
    (calender_icon),
    (google_icon)
]

for i, icon in enumerate(icons):
    if icon:  # Only create button if the icon was successfully loaded
        if i==0:
            button = Button(button_frame, image=icon, compound='top',
                            font=('Arial', 12), relief='flat', height=32, width=32,
                            bg='#004b49',bd=5,activebackground="#004b49",cursor="hand2",command=open_clock)
            button.pack(side=LEFT, padx=10, pady=10)

        elif i==1:
            button = Button(button_frame, image=icon, compound='top',
                            font=('Arial', 12), relief='flat', height=32 ,cursor="hand2",activebackground="#004b49", width=32,bg='#004b49',command=open_camera)
            button.pack(side=LEFT, padx=10, pady=10)
        elif i==2:
            button = Button(button_frame, image=icon, compound='top',
                            font=('Arial', 12), relief='flat' ,cursor="hand2",activebackground="#004b49", height=32, width=32,bg='#004b49',command=open_calculator)
            button.pack(side=LEFT, padx=10, pady=10)  
    
        elif i==3:  # If it's the Google icon
            button = Button(button_frame, image=icon, compound='top',bg='#004b49',
                            font=('Arial', 12), relief='flat', height=32 ,cursor="hand2",activebackground="#004b49", width=32,command=open_calendar)  # Assign the command
            button.pack(side=LEFT, padx=10, pady=10)

        else:
            button = Button(button_frame, image=icon, compound='top',bg='#004b49',
                            font=('Arial', 12), relief='flat' ,cursor="hand2",activebackground="#004b49", height=32, width=32,command=open_google)  # Assign the command
            button.pack(side=LEFT, padx=10, pady=10)
            
# Function call to update time
time_update()

# Start the Tkinter event loop
root.mainloop()
