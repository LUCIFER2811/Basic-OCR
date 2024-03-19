import cv2
import numpy as np
import pytesseract
from pytesseract import Output
from tkinter import *
from PIL import Image, ImageTk
def first():
    def close():
        q.destroy()
        second()
    q=Tk()
    q.state('zoomed')
    q.title("WELCOME TO OCR....")
    im=Image.open(r"C:\Users\sarth\Documents\scan-character-recognition-ocr.png")
    photo1=ImageTk.PhotoImage(im, master=q)
    photo11=Label(q, image=photo1)
    label =Label(q, text = 'A basic OCR designed to recognize character and information from images.\n Build in Python using Machine Learning', font=('arial',30, 'bold'))
    label.pack(pady=10)
    photo11.pack(pady=150)
    btn=Button(q,text="Continue",font=("arial",20),command=close)
    btn.pack()
    q.mainloop()

def pred():
    t=acce()
    cv2.imshow("Preview", t)
    cv2.waitKey(0)
        
def second():
    qp=Tk()
    qp.state("zoomed")
    qp.title("OCR - Optical Character Recognizer ......")
    lab=Label(qp,text="Enter picture address:", font=("arial",20))
    lab.pack(pady=25)
    fram=Frame(qp)
    sc=Scrollbar(fram)
    sc.pack(side=RIGHT,fill=Y)
    messag=Text(fram,width=80,height=20,wrap=CHAR)
    messag.tag_configure("tag_name",justify='center')
    messag.pack(side=LEFT,fill=BOTH,pady=18)
    inp=StringVar()
    global acce
    def acce():
        inpu=inp.get()
        inp.set("")
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        cnf="--psm 11"
        image=cv2.imread(f"{inpu}")
        res=cv2.resize(image,(900,600))
        irt=pytesseract.image_to_string(res)
        messag.insert(END,str(irt),"tag_name")
        height,width,_=res.shape

        d=pytesseract.image_to_data(res,config=cnf,output_type=Output.DICT)

        detectbox=len(d['text'])
        for i in range(detectbox):
            if float(d['conf'][i]) > 20:
                (x,y,width,height)=(d['left'][i],d['top'][i],d['width'][i],d['height'][i])
                res=cv2.rectangle(res,(x,y),(x+width , y+height),(0,255,0),2)
                res=cv2.putText(res,d["text"][i],(x,y+height+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
        
        return res
    def close1():
        qp.destroy()
        third()
    def clos():
        messag.delete("1.0","end")
    btn1=Button(qp,text="Upload",font=("arial",20),command=acce)
    name_entry = Entry(qp,textvariable =inp, font=('calibre',20,'normal'))
    name_entry.pack(side=TOP,pady=5)
    btn1.pack()
    fram.pack(pady=15)
    btn=Button(qp,text="Preview",font=("arial",20),command=pred)
    btn.pack()
    bt=Button(qp,text="Clear",font=("arial",20),command=clos)
    bt.pack()
    
    btn2=Button(qp,text="Close❌",font=("arial",20),command=close1)
    btn2.pack()

def third():
    mm=Tk()
    mm.title("Bye.......")
    mm.geometry("750x100")
    label =Label(mm, text = 'Thank you for Using the Software ... Hope to see u soon', font=('calibre',20, 'bold'))
    label.pack()
    mm.mainloop()



first()
# cv2.imshow("i",conv)
    