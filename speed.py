from tkinter import *
from speedtest import Speedtest
from datetime import datetime
from PIL import Image

time = datetime.now()
col1 = '#ffffff' #white
col3 = '#78dedc'
col4 = '#33b6de' # blue
col5 = '#3ad638' #green

def update_text():
    speed_test = Speedtest()
    speed_test.get_servers()
    speed_test.get_best_server()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps" , fg = col5, font = ("Helvetica 18 ")) 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps",  fg = col4, font = ("Helvetica 18 ")) 
    time_label.config(text= "Test Time - " + str(time.strftime("%A  %d%B%Y  %I:%M %p ")) , font = ("Helvetica 15 bold")) 


root = Tk()
root.title("INTERNET SPEED TEST")

photo = PhotoImage(file = "1.png")
root.iconphoto( False, photo)

root.geometry('550x150')
root.configure(bg = 'black')
button = Button(root, text="Test Speed", width=30, command=update_text, bg =col3)
button.pack()
down_label = Label(root, text="",bg ='black')
down_label.pack()
up_label = Label(root, text="",bg ='black')
up_label.pack()
time_label = Label(root, text="",bg ='black', fg = 'white')
time_label.pack()

#app_name = Label(foot_frame, text= "LAST UPDATED {}".format(time.strftime("%A  %d%B%Y  %I:%M %p ")), width = 150, height  = 1, pady = 5,padx = 0, relief = "flat", anchor = CENTER, font = ("arial 10"), bg = col3, fg = col2)
#app_name.pack() 

root.mainloop()
