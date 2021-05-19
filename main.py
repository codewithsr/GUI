#tk -> widget toolkit
#tkinter -> python interface for tk
#first we make instance for tk class. root is instance of tk class. root has all the basic widgets needed

#Note: kisi bhi code k baad "exit()" likhne se uske baad vala code kaam nhi karta

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
#Note: root=Tk() and root.mainloop() ke hi beech me sara code likha jata h gui ka

#For title
root.title("My gui with Harry")


#Frames technical term h bakse(boxes) ke liye. 
f1 = Frame(root, bg="green", borderwidth=20, relief=SUNKEN)         #ye jo hum Frame ke baad bracket m likhte h na jaise maine is code me "root" likha hua h, iska matlab hota h ki frame kaha jaega
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
f2.pack(side=BOTTOM, fill="x")


l1 = Label(f1, text="Project Tkinter - PyCharm", fg="blue")
l1.pack(pady=12)

l2 = Label(f2, text="Project Tkinter - Code", fg="blue")
l2.pack(pady=12 )





#Important Label Options
#text = adds the text
#bg = background
#fg = foreground
#font = sets the font. font can be done in two ways i.e, by touple method and by string method
# 1) touple method -> font=("verdana", 9, "bold")
# 2) string method -> font="verdana 9 bold"
#padx = x padding
#pady = y padding
#relief = border_styling = SUNKEN, RAISED, GROOVE, RIDGE


rathi_label = Label(text='''WhatsApp Messenger, or simply WhatsApp, is an American freeware,\n cross-platform messaging 
and Voice over IP (VoIP) service owned by Facebook,\n Inc.[46] It allows users to send text messages and voice messages,
[47] make voice and video calls,\n and share images, documents, user locations, and other media.\n WhatsApp's client 
application runs on mobile devices but is also accessible from desktop computers,\n as long as the user's mobile device
 remains connected to the Internet while they use the desktop app.\n The service requires users to provide a standard 
 cellular mobile number for registering with the service.\n In January 2018, WhatsApp released a standalone business app 
 targeted at small business owners,\n called WhatsApp Business, to allow companies to communicate with customers who use 
 the standard WhatsApp client.''', bg="blue", fg="white", padx="22", pady="95", font="verdana 9 bold", borderwidth=13, relief=RIDGE)

#Important Pack options
#anchor=nw(for northwest), se(southeast), north, etc
#side= TOP, BOTTOM, LEFT, RIGHT
#fill=X or Y . fill text ko stretch karta h jaise jaise hum box ko stretch ya bada ya chota karte h
#padx
#pady
rathi_label.pack(side=BOTTOM, anchor="sw", fill=Y, )





#width x height
root.geometry("1055x566")

#width, height
root.minsize(200,100)
#root.maxsize(350,300)



#If your photo is in png format
#photo = PhotoImage(file="1.png")                #Photo show karne k lie label use karna padta h
#shubham_label = Label(image=photo)
#shubham_label.pack()



#if not install pillow library. In command prompt write "pip install pillow"
#For Jpg images
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)
shubham_label = Label(image=photo)
shubham_label.pack()







rathi = Label(text="Shubham is a good boy")                 #label is something user don't interact with
rathi.pack()                                        #bina pack() k text show nhi hoga. Ye rule h tkinter ka



#gui logic here
root.mainloop()                  #mainloop does nothing but put you in the gui and remembers whatever logic you put 



