from tkinter import*
from tkinter import messagebox

import os
import shutil
root=Tk()
root.geometry("500x500+100+100")
root.minsize(500,500)
root.maxsize(500,500)
root.title("File Organizer")


def organizer():
     path=filepath_en.get()
     if path!='':
          try:
               
               files=os.listdir(path)
               for file in files:
                   filename,extension=os.path.splitext(file)
                   extension=extension[1:]

                   if os.path.exists(path+'/'+extension):
                         shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
                         
                   else:
                         os.makedirs(path+'/'+extension)
                         shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
               messagebox.showinfo("Done", "seccessfuly organized")        
          except:
               messagebox.showwarning("Warning", "Enter vaild path")
               
     else:
          messagebox.showwarning("Warning", "Enter path!")
          
          
     
               


     

label_name=Label(root, text="Welcome in Files Organizer Software", bg="black" ,fg="white"
                 , font="arial 18 bold").pack(fill=X)


label_filepath=Label(root, text="Enter a folder path", font="arial 15 bold",).place(x=150,y=50)

filepath_en=Entry(root,font="arial 13",fg="red")
filepath_en.place(x=100,y=100,width=300,height=35)

button_convert=Button(root,text="Start", bd="8", fg="white", width=20, bg="blue",font="arial 13 bold",command=organizer).place(x=140,y=150)
#label_done=(root,text=vardone,fg="red", font="arial 15 bold").place(x=150,y=300)



label=Label(root,text="Developer: Kiran Ingale" ,font="arial 15 bold",bg="yellow", fg="black").place(x=0,y=470,width=500)
root.mainloop()
