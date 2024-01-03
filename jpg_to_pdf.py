from tkinter import *
from tkinter import filedialog,simpledialog,messagebox
import tkinter
from PIL import Image,ImageTk
import img2pdf
import os 
import glob

root=Tk()
root.title("JPG TO PDF BY COMMUNITY PROGRAMMER")
root.geometry("390x550")



#CREATING CANVAS FOR BANNER
canvas=Canvas(root,width=386,height=100)
canvas.grid(row=0,column=0,columnspan=2)
#DISPLAYING IT ON BANNER
Banner=ImageTk.PhotoImage(Image.open("Path of the banner"))
canvas.create_image(0,0,image=Banner,anchor=NW )

#BROWSE BOX
box=Entry(root,width=45,font=("Arial bold",10))
box.grid(row=1,column=0,pady=8,ipady=7)

#DISPLAY WINDOW
scrollbar=Scrollbar(root)
scrollbar.grid(row=2,column=1,pady=5,sticky=NE+SE)
mylist = Listbox(root,width=60,height=20, yscrollcommand = scrollbar.set ,bg="white")
mylist.grid(row=2,column=0,columnspan=2,pady=5)
scrollbar.config( command = mylist.yview )

#FUNCTION FOR BROWSING FILE
def browse():
    global filename
    box.delete(0,END)
    mylist.delete(0,END)
    filename=filedialog.askdirectory()
    box.insert(END,str(filename))
    Img_list=glob.glob(str(filename) + "/*.jpg")
    Img_list.sort()
    for image in Img_list:
        a=""
        Img=image.replace(filename+f"/{a}" ,"")
        mylist.insert(END,Img)


#BROWSE BUTTON
browse=Button(root,text="Browse",font=("Arial bold",10),bg="Light blue",command=browse)
browse.grid(row=1,column=1,ipady=5)


#CLASS FOR CONVERTING
class Convert:
    def __init__(self,path,name):
        self.path=path
        self.name=name

    def process(self):
        Img_list=glob.glob(self.path + "/*.jpg")
        Img_list.sort()
        os.chdir(self.path)
        pdf=img2pdf.convert(Img_list)   
        file=open(self.path + f"//{self.name}.pdf","wb")
        file.write(pdf)
        file.close()

#CONVERTING FUNCTION
def converting():
    pdf_name=simpledialog.askstring("Name Of Pdf","Enter Name Of Pdf Without Extension",parent=root)
    converter=Convert(str(filename),pdf_name)
    converter.process()  
    messagebox.showinfo("Pdf Converted Successfully...","PDF Saved In Selected Image Folder")


#CONVERT BUTTON
button=Button(root,text="Convert To Pdf",font=("Arial bold",13),bg="Light blue",command=converting)
button.grid(row=3,column=0,columnspan=2,ipadx=115,ipady=7,pady=5)

root.mainloop()
