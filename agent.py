import platform
import getpass
import socket
from tkinter import *
from tkinter import messagebox
import requests
import json
import time

# Post URL
endpoint = "https://requestbin.fullcontact.com/1f4p8zy1"

# Pull info into variables
os = platform.system()
username = getpass.getuser()
local_ip = socket.gethostbyname(socket.getfqdn())
external_ip = requests.get('https://api.ipify.org').text


# Button Click
def click():

    # Build JSON Object
    data = dict()
    data['os'] = os
    data['username'] = username
    data['local_ip'] = local_ip
    data['external_ip'] = external_ip
    data['symptoms'] = symptoms.get('1.0', 'end-1c')
    data['timestamp'] = time.time()

    r = requests.post(endpoint, data=json.dumps(data))

    if r.status_code == 200:
        # Send message, clear text box, close window.
        messagebox.showinfo("Agent", "A technician has been notified and will be in contact.")
        symptoms.delete('1.0', END)
        root.destroy()
    else:
        # POST failed
        messagebox.showinfo("Agent", "Error: %s. Please try again.")


# Build & configure UI elements
root = Tk()
root.title("Agent")
root.geometry('480x360')
root.configure(background='grey')

container = Frame(root)
container.grid()
container.configure(background='grey')

os_label = Label(container, text=("Operating System: %s" % os))
os_label.grid(row=0, column=0, pady=(25, 0), padx=(50, 0))

username_label = Label(container, text=("User Name: %s" % username))
username_label.grid(padx=(50, 0))

local_ip_label = Label(container, text=("Local IP: %s" % local_ip))
local_ip_label.grid(padx=(50, 0))

external_ip_label = Label(container, text=("External IP: %s" % external_ip))
external_ip_label.grid(padx=(50, 0))

symptoms = Text(container, height=10, width=50)
symptoms.grid(padx=(50, 0), pady=(25, 0))

button = Button(container, text="Submit", command=click)
button.grid(padx=(50, 0), pady=(25, 0))

# Main window loop
root.mainloop()


