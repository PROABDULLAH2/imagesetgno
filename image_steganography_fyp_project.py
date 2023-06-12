#Import libraries
from tkinter import * # The standard GUI library for Python
from PIL import ImageTk, Image # contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
import time
from tkinter import messagebox #used to display the message boxes in the python applications
from PIL import ImageTk # pip install pillow
from PIL import Image, ImageTk
from PIL import Image
from PIL import ImageTk,Image
from tkvideo import tkvideo
from tkinter.tix import * 
from time import sleep
from turtle import bgcolor
from PIL import Image
import io, os
from PIL import Image,ImageTk
import mysql.connector as mysql
import pymysql # pip install pymysql
import random 
from fileinput import close
from tkinter.tix import LabelEntry
from turtle import back, bgcolor
from PIL import ImageTk, Image 
from tkinter import font
import time
from logging import root
from msilib.schema import File
from multiprocessing import parent_process
from tkinter import messagebox
from PIL import ImageTk # pip install pillow
from cgitb import text #provides a special exception handler for Python scripts.
from email import message
from email.mime import image
from fileinput import filename
import secrets # provides functions for generating secure tokens. password resets, hard-to-guess 
from tkinter import filedialog
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from stegano import lsb
from datetime import date
import cv2 #  read video, VideoCapture(), CCTV, image read.
import numpy as np #Python library used for working with arrays, linear algebra, fourier transform, and matrices
from PIL import ImageTk,Image
from tkinter import messagebox
from argparse import FileType
from tkinter.filedialog import *
from tkinter import font as tkFont
from stegano import exifHeader as aaa
import os
from subprocess import Popen
from tkvideo import tkvideo
import random   
import string  
import secrets 
from tkinter.tix import *
from PIL import Image
import PIL.Image
from turtle import color
from cryptography.fernet import Fernet #provides symmetric encryption and authentication to data
import onetimepad # one time pad
from tkinter.filedialog import askopenfilename, asksaveasfilename
import base64 #base64 algorithm
import re
from tkinter import ttk
from tkinter import END
import datetime as dt
from time import strftime
from Crypto.Cipher import DES3 # DES Algorithm
from hashlib import md5
# ==================================================================================================================== #
# ============= Image Steganography Splash Screen, Size Setting, Tittle, logo, Label, Splash Screen timing =========== #
# ==================================================================================================================== #

# Splash window
splashWin=Tk()

# Define splash screen size
width_of_window = 427
height_of_window = 250
screen_width = splashWin.winfo_screenwidth()
screen_height = splashWin.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
splashWin.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

# For hiding titlebar
splashWin.overrideredirect(1) 
Frame(splashWin, width=427, height=250, bg='#272727').place(x=0,y=0)

# Decorate it
labelImgSteg=Label(splashWin, text='Image Steganography', fg='white', bg='#272727') 
labelImgSteg.configure(font=("Game Of Squids", 25, "bold"))  

#You need to install this font in your PC or try another one
labelImgSteg.place(x=35,y=90)

# Decorate it
labeLoading=Label(splashWin, text='Loading...', fg='white', bg='#272727')  
labeLoading.configure(font=("Calibri", 11))
labeLoading.place(x=10,y=215)

# Making animation
image_a=ImageTk.PhotoImage(Image.open('images/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('images/c1.png'))

# Splash window time (3 loops)
for i in range(3): 
    l1=Label(splashWin, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    splashWin.update_idletasks()
    time.sleep(0.5)

    l1=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(splashWin, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    splashWin.update_idletasks()
    time.sleep(0.5)

    l1=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(splashWin, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    splashWin.update_idletasks()
    time.sleep(0.5)

    l1=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(splashWin, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(splashWin, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    splashWin.update_idletasks()
    time.sleep(0.5)

# =============================================================================== #
# ======================= Video Animation Window ================================ #
# =============================================================================== #

# Video animation function.
def videoAnimationFun():

    # Create Video animation window.
    videoAnimationWin = Tk()

    # Logo use.
    videoAniIcon = PhotoImage(file = 'icons/login3.png')
    
    # Setting icon of master window
    videoAnimationWin.iconphoto(False, videoAniIcon)
                
    # Title set window.
    videoAnimationWin.title('Video animation Window Image Steganography')
    
    # Define labei video animation.
    lblVideoAnimation = Label(videoAnimationWin)
    lblVideoAnimation.pack()
    # Define window size.
    videoAnimationWin.geometry("650x250")
    videoAnimationWin.attributes('-fullscreen', True)
    width1 = videoAnimationWin.winfo_screenwidth()
    height1 = videoAnimationWin.winfo_screenheight()

    # Play video animation. 
    player = tkvideo("videoAnimation/image steganography.mp4",
                                lblVideoAnimation,
                                loop=1,
                                size=(width1, height1 ))
    player.play()

    # Defibe main function of login window.
    def main():

        # Destroy video animation window.
        videoAnimationWin.destroy()

# =========================================================================== #          
# ===================== Encode And Decode Window ============================ # 
# =========================================================================== #
        
        def encodeDecodeWin(self):

            # Create encode and decode window. 
            self.selecEnDeWin = Tk()

            # Window size.
            self.selecEnDeWin.geometry("650x250")
            self.selecEnDeWin.attributes('-fullscreen', True)
            
            # Use tip tool ( Display message when hovering over something with mouse cursor ).
            tip= Balloon(self.selecEnDeWin)

            # Background Color.
            self.selecEnDeWin.configure(bg='black')

            # Add image Steganography icon (lock10.jfif) .
            bgImg = ImageTk.PhotoImage(file="images/lock10.jfif")

            # Show image Steganography icon using label.
            labelBgImg = Label( self.selecEnDeWin, image = bgImg, bd=0)
            labelBgImg.place(x = 1000, y = 310)

            # Creating a photoimage object to use image
            iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=self.selecEnDeWin)
            
            # Resizing image to fit on button
            resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

            # window minimize function.
            def minimizeWin(): 
                #make the window minimize 
                self.selecEnDeWin.state(newstate='iconic')

            minimizeBtn = Button(self.selecEnDeWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
            minimizeBtn.place(x=1400,y=50)
            tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

            # Creating a photoimage object to use image
            iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=self.selecEnDeWin)
            
            # Resizing image to fit on button
            resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

            # window RestoreDown function.
            def RestoreDown(): 
                #make the window Restore Down 
                messagebox.showerror("encode Window Status", "Window cann't resize", master=self.selecEnDeWin)
                
            # Button minimize
            minimizeBtn = Button(self.selecEnDeWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
            minimizeBtn.place(x=1355,y=54)
            tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')

# ============================================================================ #
# ============================ Encoding Window =============================== #
# ============================================================================ #
           
            # Encode button function.
            def encoding():

                # Create Encode Window
                encodWin = Tk()

                # Tip tool use for pop message 
                tip= Balloon(encodWin)

                # Window Size
                encodWin.geometry("650x250")
                encodWin.attributes('-fullscreen', True)

                # # Exit Button Function
                # def exit():
                #     if messagebox.askokcancel("Quit Program", "Do you want to quit?", master=encodWin):
                #         encodWin.destroy()
                #         self.selecEnDeWin.destroy()
                # encodWin.protocol("WM_DELETE_WINDOW", exit)

                # Background Color
                encodWin.configure(bg='black')

                # Add Lock Image Background 
                bgLockImg = PhotoImage(file='images/lock39.png', master=encodWin)
                # Add Lock Image Background 

                # Show image Steganography icon using label
                labelBgLockImg = Label( encodWin, image = bgLockImg, bd=0)
                labelBgLockImg.place(x=1030,y=460)

                # Creating a photoImage object to use image
                photoen1 = PhotoImage(file='icons/encode.png', master=encodWin)
                
                # Resizing image to fit on button
                photoimageencode1 = photoen1.subsample(2, 2)

                # Label For Tittle
                enLabel = Label(encodWin,text=" Enocode ", image = photoimageencode1, compound = LEFT, font=("time new roman",20,"bold"), fg="white", bg="black", highlightthickness=2)
                enLabel.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                enLabel.place(x=605,y=80)
                des = Label(encodWin,text=" This page hidde secrect information in image", font=("time new roman",10,"bold"), fg="white", bg="black", highlightthickness=2)
                des.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                des.place(x=540,y=125)
                # Label For Tittle
                # Creating a photoimage object to use image
                photoWriteMsg = PhotoImage(file = r"icons/writing.png", master=encodWin)
                
                # Resizing image to fit on button
                photoWrtMg = photoWriteMsg.subsample(18, 18)

                secMess = Label(encodWin,text=" Secret Message Write Here ", image = photoWrtMg, compound = LEFT, font=("time new roman",12,"bold"), fg="white", bg="black")
                secMess.place(x=630,y=210)
                
                # Creating a photoimage object to use image
                photoEncodImg = PhotoImage(file = r"icons/encodeimage.png", master=encodWin)
                
                # Resizing image to fit on button
                photoEnImg = photoEncodImg.subsample(4, 4)

                nameEnImg = Label(encodWin,text=" Name Of Enconde Image ", image = photoEnImg, compound = LEFT, font=("time new roman",12,"bold"), fg="white", bg="black")
                nameEnImg.place(x=990,y=220)
                
                # Creating a photoimage object to use image
                photoAutoKey = PhotoImage(file = r"icons/key.png", master=encodWin)
                
                # Resizing image to fit on button
                photoAukey = photoAutoKey.subsample(10, 10)
                
                autoKet = Label(encodWin,text=" Auto Key Genrate ", image = photoAukey, compound = LEFT, font=("time new roman",11,"bold"), fg="white", bg="black")
                autoKet.place(x=1000,y=270)
                
                # ========================================================#
                # ================= Encode Work ==========================#
                # ========================================================#
                # use exception.
                try:
                    #it convert data in binary formate
                    def data2binary(data):
                        if type(data) == str:
                            p = ''.join([format(ord(i), '08b')for i in data])
                        elif type(data) == bytes or type(data) == np.ndarray:
                            p = [format(i, '08b')for i in data]
                        return p
                    # ========================================================#
                    # ================= Encode Auto key genrate ==============#
                    # ========================================================#
                    # define the length of the string and genrate auto key
                    keyLength = 25
                    enKey = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(keyLength))  
                    
                    # Print the Secure string with the combonation of letters, digits and punctuation   
                    print("Secure random string is : "+ str(enKey)) 
                    with open('decodeImageKey.txt', 'w') as f:
                        f.write(enKey) 
                    lenghtKey = len(enKey)

                    # hide data in given img
                    def hidedata(img, data):

                        data += enKey  # --> secrete key
                        d_index = 0
                        b_data = data2binary(data)
                        len_data = len(b_data)

                        # iterate pixels from image and update pixel values
                        for value in img:
                            for pix in value:
                                r, g, b = data2binary(pix)
                                if d_index < len_data:
                                    pix[0] = int(r[:-1] + b_data[d_index])
                                    d_index += 1
                                if d_index < len_data:
                                    pix[1] = int(g[:-1] + b_data[d_index])
                                    d_index += 1
                                if d_index < len_data:
                                    pix[2] = int(b[:-1] + b_data[d_index])
                                    d_index += 1
                                if d_index >= len_data:
                                    break
                        return img

                # catch exception here.
                except Exception as e:
                    # Show message when catch exception.
                    messagebox.showerror('Encode window status', str(e), master=encodWin)

                # Declare gobal veriable for check select image or not.
                global ch
                ch = 0
                # ======================================================== #
                # ================= Diloge box window ==================== #
                # ======================================================== #
                # Openfile Function.
                def openfile():

                    # Create Global Veriables.
                    # img_name veriable for take path of image.
                    # imagee for read image/take image.
                    global img_name
                    global imagee
                    global ch
                    ch = ch+1
                    # Use Exception for catch exception.
                    try:
                        # Create Veriable And Code Of Select Image.
                        img_name=StringVar()
                        img_name=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*")), master=encodWin) 
                        imagee = ImageTk.PhotoImage(PIL.Image.open(img_name), master=encodWin)

                        # Label of image path
                        Labelpathimg = Label(encodWin,text=img_name, highlightthickness=2, bg="black", fg="white")
                        Labelpathimg.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        Labelpathimg.place(x=250, y=297, height=21, width=320)

                        # Label For image
                        Labelimg=Label(encodWin,image=imagee, highlightthickness=2)
                        Labelimg.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        Labelimg.place(x=250, y=355, height=270, width=200)

                        # Label path of select image
                        LabelPathEnImg=Label(encodWin,text="Path Of Seclect Encode Image",font=("time new roman", 10, "bold") ,bg="black", fg="white", highlightthickness=2)
                        LabelPathEnImg.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        LabelPathEnImg.place(x=250, y=265)

                        # Label image selected for encode
                        LabelSelectImg=Label(encodWin,text="Image Selected for Encode",font=("time new roman", 10, "bold") ,bg="black", fg="white", highlightthickness=2)
                        LabelSelectImg.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        LabelSelectImg.place(x=250, y=323)
                    # Catch exception and show message. 
                    except Exception as e:
                        messagebox.showerror('Image select status', 'Image not select.'+str(e), master=encodWin)
               
                # Go to back/previous window.
                def back():
                    encodWin.destroy()

                # Remove temparay text from secrect message field .
                def secMsg_text(e):
                    secMsg.delete('1.0', END)
                
                # Show temparay text in fields.
                def showTemTxt():
                    secMsg.delete('1.0', END)
                    enImgName.delete('1.0', END)
                    secMsg.insert(1.0, "Write secret message here .....")
                    enImgName.insert(1.0, "Enter encode image name")

                # ========================================================#
                # ================= Encode Function ======================#
                # ========================================================#
                # Function Ecode
                def encode():
                    
                    # Get values from secret message and encode image name fields. 
                    secMsgch = secMsg.get(1.0, "end-1c")
                    enImgNamech = enImgName.get(1.0, "end-1c")
                    enImgKeych = enImgKey.get(1.0, "end-1c")

                    # Declare global veriable and check condition.
                    # if ch veriable is equel to 0 then show message image not select
                    # otherwise image select.
                    # and check condition fields are requireds or not not
                    global ch
                    if(ch == 0):
                        messagebox.showerror("encode Window Status", "Not select Image Please select first image.", master=encodWin)
                        ch = 0
                    elif(secMsgch == "Write secret message here ....." and enImgNamech == "Enter encode image name"):
                        messagebox.showerror("encode Window Status", "All fields are required.", master=encodWin)
                    elif(secMsgch == "Write secret message here ....."):
                        messagebox.showerror("Encode Window Status", "Write secret message field are required.", master=encodWin)
                    elif(enImgNamech == "Enter encode image name"):
                        messagebox.showerror("encode Window Status", "Encode image name field are required.", master=encodWin)
                    elif(enImgKeych == "Enter Key For Encode Image"):
                        messagebox.showerror("encode Window Status", "Key For Encode Image field are required.", master=encodWin)
                    else:
                        
                        if(enImgKeych == "Encode_Key_For_Image"):
                            # Use Exceptipn for catch exception.
                            try:
                                # Create global veriables.
                                # data veriable for take secrect message.
                                # enc_img veriable for encode image.
                                global data
                                global enc_img
                                global f_obj
                                dataSec = secMsg.get("1.0", "end-1c")
                                enc_img = enImgName.get("1.0", "end-1c")
                                entrykey.delete(0,"end")
                                entrykey.insert(0, enKey)
                                # ========================================================#
                                # ================= Base64 and One time algorithm ========#
                                # ========================================================#
                                # Encrypt data through one time and base64 / encode function use for string convert into byte.
                                ds = dataSec.encode()
                                encoded_data = base64.b64encode(ds)
                                sms = encoded_data.decode()
                                encMessage = onetimepad.encrypt(sms, 'random')
                                data = str(encMessage)

                                with open('Encoded_Secret_Message.txt', 'w') as f:
                                    f.write(data)
                                 
                                # # Encrypt plain/secret message.
                                # encMessage = onetimepad.encrypt(dataSec, 'random')

                                # data = str(encMessage)

                                image = cv2.imread(img_name)
                                img = Image.open(img_name, 'r')
                                w, h = img.size
                                if len(data) == 0:
                                    raise ValueError("Empty data")
                                enc_data = hidedata(image, data)
                                cv2.imwrite(enc_img, enc_data)
                                img1 = Image.open(enc_img, 'r')
                                img1 = img1.resize((w, h),Image.ANTIALIAS)
                                # optimize with 65% quality
                                if w != h:
                                    img1.save(enc_img, optimize=True, quality=65)
                                else:
                                    img1.save(enc_img)
                                messagebox.showinfo("encode Window Status", "Successfully Encoded image and Secret Message.", master=encodWin)
                                # ========================================================#
                                # ================= Encrypt Message Window ===============#
                                # ========================================================#
                                # call function show temparay text in fields.
                                def SecretMsgEncrypt():
                                    # Create Window.
                                    encryptSecMsgWin = Tk()

                                    # Tittle window.
                                    encryptSecMsgWin.title("Encrypted secret message")

                                    # Setting icon of master window
                                    iconPath = PhotoImage(file = 'icons/pngegg.png', master=encryptSecMsgWin)
                                    
                                    # Setting icon of master window
                                    encryptSecMsgWin.iconphoto(False, iconPath)
                                    encryptSecMsgWin.geometry("430x530+500+100")
                                    encryptSecMsgWin['bg']='black'

                                    # adding frame
                                    frame = Frame(encryptSecMsgWin, highlightthickness=2)
                                    frame.config(highlightbackground = "#18aff0", highlightcolor= "#18aff0")
                                    frame.pack(pady=20)

                                    # adding scrollbars 
                                    ver_sb = Scrollbar(frame, orient=VERTICAL )
                                    ver_sb.pack(side=RIGHT, fill=BOTH)

                                    hor_sb = Scrollbar(frame, orient=HORIZONTAL)
                                    hor_sb.pack(side=BOTTOM, fill=BOTH)

                                    # adding writing space
                                    txtarea = Text(frame, width=40, height=20)
                                    txtarea.pack(side=LEFT)

                                    # binding scrollbar with text area
                                    txtarea.config(yscrollcommand=ver_sb.set)
                                    ver_sb.config(command=txtarea.yview)

                                    txtarea.config(xscrollcommand=hor_sb.set)
                                    hor_sb.config(command=txtarea.xview)

                                    # Creating a photoImage object to use image
                                    lblIcon = PhotoImage(file='icons/pngegg.png', master=encryptSecMsgWin)
                                                    
                                    # Resizing image to fit on button
                                    lblIconResize = lblIcon.subsample(20, 20)

                                    lbl = Label(encryptSecMsgWin, text="  Encrypted Secret Mesaage",font=(" time new roman", 14, "bold"), image = lblIconResize, compound = LEFT, bg="black", fg="white", highlightthickness=2)
                                    lbl.config(highlightbackground = "#18aff0", highlightcolor= "#18aff0")
                                    lbl.place(x=75, y=400)
                                    txtarea.insert(END, encMessage)

                                    encryptSecMsgWin.mainloop()

                                SecretMsgEncrypt()
                                showTemTxt()
                            # Catch exception here and show message.
                            except Exception as e:
                                messagebox.showerror('Image select status', str(e), master=encodWin)
                        else:
                            messagebox.showerror("encode Window Status", "Invalid Key For Encode Image.", master=encodWin)

                # Text box for write secret message
                secMsg = Text(encodWin, font = "Robote 13", bg="#B8BABC", fg="black", bd=0, highlightthickness=2)
                secMsg.insert(1.0, "Write secret message here .....")
                secMsg.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                secMsg.place(x=630, y=255,width=280,height=375)
                secMsg.bind("<FocusIn>",secMsg_text)
                tip.bind_widget(secMsg,balloonmsg='''Write Message Which Hide In Image .... ''')
                # ========================================================#
                # ================= Character counting  ==================#
                # ========================================================#
                # Character count ...
                l2=Label(encodWin,text=150,font=20)
                l2.place(x=630,y=635)
                def my_upd(value):
                    my_str=secMsg.get("1.0",'end-1c')
                    breaks=my_str.count('\n')
                    char_numbers=len(my_str)-breaks
                    l2.config(text=str(char_numbers))
                    prg1['value']=char_numbers # Update Progress bar value 
                    if(char_numbers < 151):
                        prg1.config(style='green.Horizontal.TProgressbar') 
                    else:
                        secMsg.delete('end-2c') # remove last char from Text widgets 
                        messagebox.showerror("Secret Messagge Info", "Only 150 character secret message allow", master=encodWin)

                        

                secMsg.bind('<KeyRelease>', my_upd)
                
                s = ttk.Style()
                s.theme_use('alt')
                s.configure("green.Horizontal.TProgressbar", background='green')
                prg1=ttk.Progressbar(encodWin,length=260,mode='determinate',maximum=151,value=0,
                style='green.Horizontal.TProgressbar')
                prg1.place(x=667,y=635)
                # ========================================================#
                # ================= Scroll bar and Field =================#
                # ========================================================#
                # Scrollbar of text box
                scrollbar = Scrollbar(encodWin, orient=VERTICAL, command=secMsg.yview)
                scrollbar.place(x=910, y=255, height=375)
                secMsg.config(yscrollcommand=scrollbar.set)
                  
                # Function of remove encode imgage name.
                def enImgName_text(e):
                    enImgName.delete('1.0', END)

                # Text box of write of encoding image name 
                enImgName = Text(encodWin, width=28, height=1.3, bg="#B8BABC", bd=0, highlightthickness=2)
                enImgName.insert(1.0, "Enter encode image name")
                enImgName.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                enImgName.place(x=1000,y=255)
                enImgName.bind("<FocusIn>",enImgName_text)
                tip.bind_widget(enImgName,balloonmsg='''Encoded Image Name Write''')

                # Entry box for genrate auto key
                entrykey = Entry(encodWin, font=("arial", 10, "bold"), bg="#B8BABC", fg="black", width=31,  highlightthickness=2)
                entrykey.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                entrykey.insert(0, " Auto Key Genrate. ")
                entrykey.place(x=1000,y=315)
                tip.bind_widget(entrykey,balloonmsg='''Auto Key Genrate''')
                
                # Creating a photoimage object to use image
                iconEnImgKey = PhotoImage(file = r"icons/key.png", master=encodWin)
                
                # Resizing icon,
                iconEnImgKeyResize = iconEnImgKey.subsample(15, 15)
                
                EnImgKey = Label(encodWin,text=" Key For Encode Image. ", image = iconEnImgKeyResize, compound = LEFT, font=("time new roman",11,"bold"), fg="white", bg="black")
                EnImgKey.place(x=1000,y=345)

                # Function of key for encode image.
                def enImgKey_text(e):
                    enImgKey.delete('1.0', END)

                # Text box of write of encode key.
                enImgKey = Text(encodWin, width=28, height=1.3, bg="#B8BABC", bd=0, highlightthickness=2)
                enImgKey.insert(1.0, "Enter Key For Encode Image")
                enImgKey.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                enImgKey.place(x=1000,y=380)
                enImgKey.bind("<FocusIn>",enImgKey_text)
                tip.bind_widget(enImgKey,balloonmsg='''Enter key for encode image.''')
                # ========================================================#
                # ================= Key select Button ====================#
                # ========================================================#
                # Button for select key (Encode key text file).
                def open_file():
                    try:
                        """Open a file for editing."""
                        filepath = askopenfilename(
                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], master=encodWin
                        )

                        with open(filepath, "r") as input_file:
                            text = input_file.read()
                            enImgKey.delete('1.0', END)
                            enImgKey.insert('1.0',text)
                    except Exception as e:
                        messagebox.showerror('Encode key process status', str(e), master=encodWin)
                
                 #Define functions change color of button
                def on_enter(e):
                    btn_open.config(background='#808080', foreground= "white")

                def on_leave(e):
                    btn_open.config(background= '#313030', foreground= 'white')

                btn_open = Button(encodWin, text="Key", command=open_file, bg="#232222", fg="white")
                btn_open.place(x=1245, y=380)

                #Bind the Enter 
                btn_open.bind('<Enter>', on_enter)
                btn_open.bind('<Leave>', on_leave)

                tip.bind_widget(btn_open,balloonmsg='''Button For Select key from folder''')


                # Creating a photoimage object to use image
                photoSelectBtn = PhotoImage(file = r"icons/open.png", master=encodWin)
                
                # Resizing image to fit on button
                photoSelBtn = photoSelectBtn.subsample(20, 20)

                #Define functions change color of button
                def on_enter(e):
                    selectImgBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    selectImgBtn.config(background= '#313030', foreground= 'white')

                # Select image button
                selectImgBtn = Button(encodWin, text="  Select file", image = photoSelBtn, compound = LEFT, bg="#232222",
                                    fg="white", font=("time new roman", 10, "bold"), width=140, command=openfile)
                selectImgBtn.place(x=250, y=220)

                #Bind the Enter 
                selectImgBtn.bind('<Enter>', on_enter)
                selectImgBtn.bind('<Leave>', on_leave)

                tip.bind_widget(selectImgBtn,balloonmsg='''Button For Select File/Image''')

                # # Creating a photoimage object to use image
                # photoExitBtn = PhotoImage(file = r"icons/exit.png", master=encodWin)
                
                # # Resizing image to fit on button
                # photoExBtn = photoExitBtn.subsample(6, 6)

                # #Define functions change color of button
                # def on_enter(e):
                #     ExBtn.config(background='#808080', foreground= "white")

                # def on_leave(e):
                #     ExBtn.config(background= '#313030', foreground= 'white')

                # # Exit Button
                # ExBtn = Button(encodWin, text="  Exit", image = photoExBtn, compound = LEFT, bg="#232222", 
                #     fg="white", font=("time new roman", 10, "bold"), width=120, command=exit)
                # ExBtn.place(x=1300, y=800)

                # #Bind the Enter 
                # ExBtn.bind('<Enter>', on_enter)
                # ExBtn.bind('<Leave>', on_leave)

                # tip.bind_widget(ExBtn,balloonmsg='''Button For Exit Page''')

                # Creating a photoimage object to use image
                photoBackBtn = PhotoImage(file = r"icons/back1.png", master=encodWin)
                
                # Resizing image to fit on button
                photoimageback = photoBackBtn.subsample(1, 1)

                #Define functions change color of button
                def on_enter(e):
                    baBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    baBtn.config(background= '#313030', foreground= 'white')

                # Back Button
                baBtn = Button(encodWin, text="  Back", image = photoimageback, compound = LEFT, bg="#232222", fg="white", font=("time new roman", 
                    10, "bold"), width=120, command=back)
                baBtn.place(x=1300, y=800)

                #Bind the Enter 
                baBtn.bind('<Enter>', on_enter)
                baBtn.bind('<Leave>', on_leave)

                tip.bind_widget(baBtn,balloonmsg='''Button For Previous Slide''')
                                        
                # Creating a photoimage object to use image
                photoEnBtn = PhotoImage(file = r"icons/lock.png", master=encodWin)
                
                # Resizing image to fit on button
                photoEncodeBtn = photoEnBtn.subsample(20, 20)

                #Define functions change color of button
                def on_enter(e):
                    enBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    enBtn.config(background= '#313030', foreground= 'white')

                enBtn = Button(encodWin, text="  Encode", image = photoEncodeBtn, compound = LEFT, bg="#232222", fg="white",
                    font=("time new roman", 10, "bold"), width=130, command=encode)
                enBtn.place(x=1050,y=420)

                #Bind the Enter 
                enBtn.bind('<Enter>', on_enter)
                enBtn.bind('<Leave>', on_leave)

                tip.bind_widget(enBtn,balloonmsg='''Button For Use Hide Information In Image''')
                encodWin.quit()

                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=encodWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    encodWin.state(newstate='iconic')
                    self.selecEnDeWin.state(newstate='iconic')

                minimizeBtn = Button(encodWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=encodWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=encodWin)
                    
                # Button minimize
                minimizeBtn = Button(encodWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')
                
                # Encode window main loop.                        
                encodWin.mainloop()

# ============================================================================ #
# ============================ Decoding Window =============================== #
# ============================================================================ #

            # Decode button function.
            def decoding():

                # Create Window
                decodWin = Tk()

                # tip tool use
                tip= Balloon(decodWin)

                # Window size
                decodWin.geometry("650x250")
                decodWin.attributes('-fullscreen', True)

                # # Exit button function
                # def exit():
                #     if messagebox.askokcancel("Quit Program", "Do you want to quit?", master= decodWin):
                #         decodWin.destroy()
                #         self.selecEnDeWin.destroy()
                # decodWin.protocol("WM_DELETE_WINDOW", exit)

                # Background Color
                decodWin.configure(bg='black')

                # Creating a photoimage object
                photodecodBtn = PhotoImage(file = r"icons/de2.png", master=decodWin)
                
                # Resizing image to fit on button
                photoDeBtn = photodecodBtn.subsample(10, 10)

                # Label decode and This page show secrect information in image
                deLabel = Label(decodWin,text="  Decode ", image = photoDeBtn, compound = LEFT, font=("time new roman",20,"bold"), fg="white", bg="black", highlightthickness=2)
                deLabel.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                deLabel.place(x=600,y=40)
                infoPage = Label(decodWin,text=" This page show secrect information in image",font=("time new roman",10,"bold"), fg="white", bg="black", highlightthickness=2)
                infoPage.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                infoPage.place(x=530,y=108)
                                                    
                # Decode Image  
                decodImg = ImageTk.PhotoImage(file="images/de5.png", master=decodWin)

                # Show image Steganography icon using label
                label1 = Label( decodWin, image = decodImg, bd=0)
                label1.place(x=820,y=380)
                # ========================================================#
                # ================= Decode Work ==========================#
                # ========================================================#
                # Use excaption for catch excaption.
                try:               
                    #it convert data in binary formate
                    def data2binary(data):
                        if type(data) == str:
                            p = ''.join([format(ord(i), '08b')for i in data])
                        elif type(data) == bytes or type(data) == np.ndarray:
                            p = [format(i, '08b')for i in data]
                        return p
                # Catch excaption here.        
                except Exception as e:
                    messagebox.showerror('Image select status', 'Invalid Image select '+str(e), master=decodWin)
                
                # Declare global veriable for check image select or not.
                global ch
                ch = 0
                # ========================================================#
                # ================= Image select =========================#
                # ========================================================#
                # Openfile button function
                def openfile():
                    
                    # Declare global veriable for check image select or not.
                    global ch
                    ch = ch+1

                    # Use excaption for catch excaption.
                    try:
                        # Create global veriables
                        global img_name
                        global open_img
                        
                        # Select file function
                        img_name=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*")), master=decodWin) 
                        open_img = ImageTk.PhotoImage(PIL.Image.open(img_name), master=decodWin)

                        # Create Label for img path
                        Labelpath=Label(decodWin,text=img_name, highlightthickness=2, bg="black", fg="white")
                        Labelpath.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        Labelpath.place(x=120, y=235, height=21, width=250)

                        # Create Label for open img
                        Labelimg=Label(decodWin,image=open_img, highlightthickness=2)
                        Labelimg.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        Labelimg.place(x=120, y=290, height=260, width=200)
                        
                        # Label for Path of image when select img
                        labelImgPath=Label(decodWin,text="Path of image",font=("time new roman", 10, "bold") ,bg="black", fg="white", highlightthickness=2)
                        labelImgPath.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        labelImgPath.place(x=120, y=205)

                        # Label for Image Selected for Encrypt when select img
                        labelImgSelect=Label(decodWin,text="Image Selected for Decrypt",font=("time new roman", 10, "bold") ,bg="black", fg="white", highlightthickness=2)
                        labelImgSelect.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                        labelImgSelect.place(x=120, y=260)
                    # Catch excaption here.
                    except Exception as e:
                        messagebox.showerror('Image select status', 'Image not select '+str(e), master=decodWin)
                        ch = 0
                
                # Decode key function.
                def decodkey_text(e):
                    decodkey.delete(0.1,"end")

                # Creating a photoimage object
                decodKeyIcon = PhotoImage(file = r"icons/key.png", master=decodWin)
                
                # Resizing image to fit on button
                decodKeIcon = decodKeyIcon.subsample(11, 11)

                # Label decode key
                textLabel = Label(decodWin,text="  Enter Key For Decode Image ", image = decodKeIcon, compound = LEFT, font=("time new roman",12,"bold"), fg="white", bg="black")
                textLabel.place(x=790,y=160)

                # Text field write key 
                decodkey = Text(decodWin, width=30, height=1.3, highlightthickness=2)
                decodkey.insert(0.1, "Enter key for Decode image")
                decodkey.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                decodkey.place(x=790,y=205)
                decodkey.bind("<FocusIn>", decodkey_text)
                # ========================================================#
                # ================= Select key button ====================#
                # ========================================================#
                 # Button for select key (Decode key text file).
                def open_file():
                    try:
                        """Open a file for editing."""
                        filepath = askopenfilename(
                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], master=decodWin
                        )

                        with open(filepath, "r") as input_file:
                            text = input_file.read()
                            decodkey.delete('1.0', END)
                            decodkey.insert('1.0',text)
                    except Exception as e:
                        messagebox.showerror('Encode key process status', str(e), master=decodWin)
                
                 #Define functions change color of button
                def on_enter(e):
                    btn_open1.config(background='#808080', foreground= "white")

                def on_leave(e):
                    btn_open1.config(background= '#313030', foreground= 'white')

                btn_open1 = Button(decodWin, text="Key", command=open_file, bg="#232222", fg="white")
                btn_open1.place(x=1050, y=205)

                #Bind the Enter 
                btn_open1.bind('<Enter>', on_enter)
                btn_open1.bind('<Leave>', on_leave)

                tip.bind_widget(btn_open1,balloonmsg='''Button For Select key from folder''')

                # Creating a photoimage object.
                IconSecMes = PhotoImage(file = r"icons/message.png", master=decodWin)
                    
                # Resizing image to fit on button.
                IconSecMesResize = IconSecMes.subsample(21, 21)

                # Label show secret message.
                msgShowtxtBoxLabel = Label(decodWin,text="  Secret Message  ", image = IconSecMesResize, compound = LEFT, font=("time new roman",12,"bold"), fg="white", bg="black")
                msgShowtxtBoxLabel.place(x=460,y=165)
                 
                # Back button function. 
                def back():
                    decodWin.destroy()
                # ========================================================#
                # ================= Decode Work ==========================#
                # ========================================================#
                # Use excaption catch excaption.
                try:

                    # decoding
                    def find_data(img):
                        bin_data = ""
                        for value in img:
                            for pix in value:
                                r, g, b = data2binary(pix)
                                bin_data += r[-1]
                                bin_data += g[-1]
                                bin_data += b[-1]

                        all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

                        readable_data = ""
                        for x in all_bytes:
                            readable_data += chr(int(x, 2))
                            if readable_data[-lenghtKey:] == deckey:
                                break
                        if readable_data[-lenghtKey:] == deckey:
                            return readable_data[:-lenghtKey]
                # Catch excaption here.
                except Exception as e:
                    messagebox.showerror('Image select status',str(e), master=decodWin)
                
                # Show temparay text in fields.
                def showTemTxt():
                    decodkey.delete('1.0', END)
                    decodkey.insert(1.0, "Enter decode image key")
                # ========================================================#
                # ================= Decode Function ======================#
                # ========================================================#
                def decode():

                    # Use exception for catch excaption.
                    try:
                        key1 = decodkey.get(1.0, "end-1c")
                        text_file = open("decodeImageKey.txt", "r")

                        key2 = text_file.read()
                        #close file
                        text_file.close()
                        
                    # Catch exception here.
                    except Exception as e:
                        messagebox.showerror('Error', str(e), master=decodWin)
                    
                    decodkeytext = decodkey.get(1.0, "end-1c")
                    if(decodkeytext == "Enter Decode key"):
                        messagebox.showerror("Decode Image Status", "Enter Decode key are field required.", master=decodWin)
                    elif(ch == 0):
                        messagebox.showerror("Decode Image Status", "Image not select please first select image.", master=decodWin)
                    # Check key for valid or invalid.
                    elif(key1 != key2 and decodkeytext != "Enter Decode key"):
                        messagebox.showerror('Decode Image Status', 'Invalid key for decode image please enter valid key', master=decodWin)
                    else:
                    
                        # Use excaption catch excaption.
                        try:
                            # Create global veriables
                            global deckey
                            global lenghtKey

                            # print("==================== "+str(key12))
                            deckey = decodkey.get("1.0", "end-1c")
                            lenghtKey = len(deckey)
                            # ========================================================#
                            # ==== image read , decrypt , base64, one time pad =======#
                            # ========================================================#
                            # Img read and call find_data
                            image = cv2.imread(img_name)
                            img=Image.open(img_name,'r')
                            msg = find_data(image)

                            # msgP = onetimepad.decrypt(msg, 'random')
                            msgP = onetimepad.decrypt(msg, 'random')
                            sms = msgP.encode()
                            decoded_data = base64.b64decode(sms)
                            smss = decoded_data.decode()
             
                            # Text box show secret message.
                            secMessLabel = Text(decodWin, font=('Calibri 15'), highlightthickness=2)
                            # Insert message in text box.
                            secMessLabel.insert(END, smss)
                            secMessLabel.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                            secMessLabel.place(x=450, y=200, height = 350, width = 280)

                            # Scrollbar of text box
                            scrollbar = Scrollbar(decodWin, orient=VERTICAL, command=secMessLabel.yview)
                            scrollbar.place(x=730, y=200, height=350)
                            secMessLabel.config(yscrollcommand=scrollbar.set)

                            # Message pop
                            messagebox.showinfo("Decode Image Status", "Successfully Image Decoded And Show Secret Message.", master=decodWin)
                            # SecretMsgEncrypt
                            showTemTxt()
                        # Catch excaption here.
                        except Exception as e:
                            messagebox.showerror('Image select status','Invalid select image '+str(e), master=decodWin)

                # Creating a photoimage object to use image
                photofil = PhotoImage(file = r"icons/open.png", master=decodWin)
                
                # Resizing image to fit on button
                photoimagefiles = photofil.subsample(20, 20)

                #Define functions
                def on_enter(e):
                    OpenfileBtn.config(background='#614648', foreground= "white")

                def on_leave(e):
                    OpenfileBtn.config(background= '#313030', foreground= 'white')

                # Select button 
                OpenfileBtn = Button(decodWin, text="   Select file", image = photoimagefiles, compound = LEFT, bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=140, command=openfile)
                OpenfileBtn.place(x=120, y=160)

                #Bind the Enter 
                OpenfileBtn.bind('<Enter>', on_enter)
                OpenfileBtn.bind('<Leave>', on_leave)

                tip.bind_widget(OpenfileBtn,balloonmsg='''Button For Select File From Image Location''')
                # ========================================================#
                # ================= Text file function ===================#
                # ========================================================#
                # Text File Decode function.
                def TextFile():

                    global data

                    try:
                        def openFile():
                            try:
                                global data
                                tf = filedialog.askopenfilename(
                                    initialdir="C:/Users/MainFrame/Desktop/", 
                                    title="Open Text file", 
                                    filetypes=(("Text Files", "*.txt"),), master=ws
                                    )

                                pathh.insert(END, tf)
                                tf = open(tf)  # or tf = open(tf, 'r')
                                data = tf.read()
                                txtarea.insert(END, data)
                                tf.close()
                            except Exception as e:
                                messagebox.showerror('Error', "Text file not", master=ws)
                        
                    
                        # ========================================================#
                        # ==== Text file decrypt one time pad, base64 ============#
                        # ========================================================#
                        def decodeTextFile():
                            global data
                            try:
                                msgP = onetimepad.decrypt(data, 'random')
                                 # Catch exception here.
                                sms = msgP.encode()
                                decoded_data = base64.b64decode(sms)
                                smss = decoded_data.decode()
                                txtarea.delete("1.0","end")
                                txtarea.insert(END, smss)
                                # Message pop
                                messagebox.showinfo("Decode Text File Status", "Successfully Text File Decode And Show Secret Message.", master=ws)
                            except Exception as e:
                                messagebox.showerror('Error', "Invalid Select Text File", master=ws)
                     # Catch exception here.
                    except Exception as e:
                        messagebox.showerror('Error', str(e), master=ws)
                    ws = Tk()  # ================= Text file window ==========#
                    ws.title("Decode Text File")
                    ws.geometry("500x550+500+180")
                    ws['bg']='#28a0c6'

                    txtarea = Text(ws, width=40, height=20)
                    txtarea.pack(pady=20)

                    pathh = Entry(ws)
                    pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

                    Button(
                        ws, 
                        text="Open File", 
                        command=openFile
                        ).pack(side=LEFT, expand=True, fill=X, padx=3)

                    Button(
                        ws, 
                        text="Decode Text File", 
                        command=decodeTextFile
                        ).pack(side=RIGHT, expand=True, fill=X, padx=5)

                    


                    ws.mainloop()

                # Creating a photoimage object to use text file.
                photoTextBtn = PhotoImage(file = r"icons/file.png", master=decodWin)
                
                # Resizing text to fit on button
                photoTextBtnResize = photoTextBtn.subsample(3, 3)

                #Define functions change color of button
                def on_enter(e):
                    textBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    textBtn.config(background= '#313030', foreground= 'white')

                textBtn = Button(decodWin, text=" Text File", image = photoTextBtnResize, compound = LEFT, bg="#232222", fg="white",
                    font=("time new roman", 10, "bold"), width=120, command=TextFile)
                textBtn.place(x=820,y=330)

                #Bind the Enter 
                textBtn.bind('<Enter>', on_enter)
                textBtn.bind('<Leave>', on_leave)

                tip.bind_widget(decodWin,balloonmsg='''Button For Decode Text File.''')
                # encodWin.quit()

                # # Creating a photoimage object to use image
                # photoe12 = PhotoImage(file = r"icons/exit.png", master=decodWin)
                
                # # Resizing image to fit on button
                # photoimageex1 = photoe12.subsample(6, 6)

                # #Define functions
                # def on_enter(e):
                #     ExBtn.config(background='#614648', foreground= "white")

                # def on_leave(e):
                #     ExBtn.config(background= '#313030', foreground= 'white')

                # # Exit Button
                # ExBtn = Button(decodWin, text="  Exit", image = photoimageex1, compound = LEFT, bg="#232222", fg="white",
                #             font=("time new roman", 10, "bold"), width=120, command=exit)
                # ExBtn.place(x=1300, y=800)

                # #Bind the Enter 
                # ExBtn.bind('<Enter>', on_enter)
                # ExBtn.bind('<Leave>', on_leave)

                # tip.bind_widget(ExBtn,balloonmsg='''Button For Exit Program''')

                # Creating a photoimage object to use image
                photoba1 = PhotoImage(file = r"icons/back1.png", master=decodWin)
                
                # Resizing image to fit on button
                photoimageback1 = photoba1.subsample(1, 1)

                #Define functions
                def on_enter(e):
                    backBtn.config(background='#614648', foreground= "white")

                def on_leave(e):
                    backBtn.config(background= '#313030', foreground= 'white')

                # Back button
                backBtn = Button(decodWin, text="  Back", image = photoimageback1, compound = LEFT, bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=120, command=back)
                backBtn.place(x=1300, y=800)

                #Bind the Enter 
                backBtn.bind('<Enter>', on_enter)
                backBtn.bind('<Leave>', on_leave)

                tip.bind_widget(backBtn,balloonmsg='''Button For Previous Page''')

                # Creating a photoimage object to use image
                photoen = PhotoImage(file = r"icons/unlock1.png", master=decodWin)
                
                # Resizing image to fit on button
                photoimageencode = photoen.subsample(25, 25)

                #Define functions
                def on_enter(e):
                    deBtn.config(background='#614648', foreground= "white")

                def on_leave(e):
                    deBtn.config(background= '#313030', foreground= 'white')

                # Decode Button
                deBtn = Button(decodWin, text="  Decode", image = photoimageencode, compound = LEFT, bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=120, 
                            height=27, bd=1, command=decode)
                deBtn.place(x=820,y=290)
                #Bind the Enter 
                deBtn.bind('<Enter>', on_enter)
                deBtn.bind('<Leave>', on_leave)

                tip.bind_widget(deBtn,balloonmsg='''Button For Decrypt/Show Message.''')

                                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=decodWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    decodWin.state(newstate='iconic')
                    self.selecEnDeWin.state(newstate='iconic')

                minimizeBtn = Button(decodWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=decodWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=decodWin)
                    
                # Button minimize
                minimizeBtn = Button(decodWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')
                 
                # Decode window main loop.
                decodWin.mainloop()
                
# =========================================================================== #
# ============================ Encrypt Window =============================== #
# =========================================================================== #
   
            def encrypt():

                EncryptWin = Tk()

                # Tittle
                EncryptWin.title("Encrypt Image ")

                # Define window size with geometry function
                EncryptWin.geometry("650x250")
                EncryptWin.attributes('-fullscreen', True)
                EncryptWin.configure(bg="black")

                # Icon of image steganography title
                photopicc = PhotoImage(file = r"icons/en2.png", master=EncryptWin)
                
                # Resizing image to fit on button
                photoimagepic = photopicc.subsample(15, 15)

                # Label Creat Account
                labelacc= Label(EncryptWin, text= " Encryption Image ", image = photoimagepic, compound = LEFT, 
                                font=('Times New Roman bold',25), bg="black", fg="white", highlightthickness=2)

                labelacc.config(highlightbackground = "gray", highlightcolor= "gray", width=330)
                labelacc.place(x = 600, y = 110)
                # ========================================================#
                # ================= DES Encryption algorithm =============#
                # ========================================================#
                def encryptionDES():
                    key=""
                    file_bytes=""
                    # Encode given key to 16 byte ascii key with md5 operation
                    key_hash = md5(key.encode('ascii')).digest()

                    # Adjust key parity of generated Hash Key for Final Triple DES Key
                    tdes_key = DES3.adjust_key_parity(key_hash)
                    
                    #  Cipher with integration of Triple DES key, MODE_EAX for Confidentiality & Authentication
                    #  and nonce for generating random / pseudo random number which is used for authentication protocol
                    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
                    new_file_bytes = cipher.encrypt(file_bytes)
                    
                # ========================================================#
                # ================= IMAGE STEGANOGRAPHY name =============#
                # ========================================================#
                # Image Steganography text amination
                canvas = Canvas(EncryptWin, background="gray")
                canvas.place(x=630, y=180, width=272, height=40)
                canvas_t = canvas.create_text(10, 10, text='', anchor=NW, font=('Times New Roman bold',15))
                our_text = "IMAGE STEGANOGRAPHY"
                delta = 300
                delay = 0
                for x in range(len(our_text)+1):
                    s = our_text[:x]
                    new_text = lambda s=s: canvas.itemconfigure(canvas_t, text=s)
                    canvas.after(delay, new_text)
                    delay += delta

                # # Exit Button Function
                # def exit():
                #     if messagebox.askokcancel("Program Quite Status", "Do You Want To Exit Program?", master=EncryptWin):
                #         EncryptWin.destroy()
                #         self.selecEnDeWin.destroy()

                # Back Button Function
                def back():
                    EncryptWin.destroy()
                # Declare global veriable for check image select or not.
                global ch
                ch=0
                # Select button image button function. 
                # ========================================================#
                # ================= select image  ========================#
                # ========================================================#
                def showimage():
                    # Declare global veriable for check image select or not.
                    global ch
                    ch = ch+1
                    # Use exception for catch exception.
                    try:
                        # Declare global veriable for access path of image.
                        global filename
                        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                            title="Select Image File",
                                                            filetypes=(("PNG file","*.png"),
                                                                            ("JPG file", "*.jpg"),
                                                                            ("All file","*.text")), master=EncryptWin)

                        img = PIL.Image.open(filename)
                        img = ImageTk.PhotoImage(img, master=EncryptWin)
                        lbl.configure(image=img,width=250,height=250)
                        lbl.image = img
                    # Catch exception here.
                    except Exception as e:
                        messagebox.showerror('Encrypt window status', 'Image not select '+str(e), master=EncryptWin)
                
                # Encrypt File Button Functiom
                def EncryptFile():
                    # Declare global veriable for check image select or not.
                    global ch
                    # Access value from entry file field .
                    imageName = entryFile.get()
                    # Check condition.
                    if(ch == 0):
                        messagebox.showerror('Encrypt window status', 'image not select first image select.', master=EncryptWin)
                    elif(imageName == "Enter Name Of Encrypt Image"):
                        messagebox.showerror('Encrypt window status', 'Enter Name Of Encrypt Image field are required.', master=EncryptWin)
                    else:
                        # Declare global veriable for access path of image.
                        try:
                            # ========================================================#
                            # ================= Encryption key genrate   =============#
                            # ========================================================#
                            # Access value from encrypt file name field.
                            key = Fernet.generate_key()
                            encryptedFileName = entryFile.get()
                            # Delete temparary text from field.
                            entrykey.delete(0,"end")
                            entrykey.insert(0, key)

                            # Encryption key
                            fernet = Fernet(key)

                            # How save key in system
                            # Write key
                            with open('Key_Of_Encrypt.key', 'wb') as filekey:
                                filekey.write(key)

                            # read key
                            with open('Key_Of_Encrypt.key', 'rb') as filekey:
                                key = filekey.read()

                            # read file
                            with open(filename, 'rb') as file:
                                original_file = file.read()

                            # Encrypted file
                            encrypted = fernet.encrypt(original_file )

                            with open(encryptedFileName , 'wb') as file:
                                file.write(encrypted)

                            messagebox.showinfo('Encrypt Image status', 'Successfully Image Encrypted And Create Key In System.', master=EncryptWin)
                        # Catch exception here.
                        except Exception as e:
                            messagebox.showerror('Encrypt Image status', str(e), master=EncryptWin)
                # Icon
                image_icon = PhotoImage(file="icons/enryp.png", master=EncryptWin)
                EncryptWin.iconphoto(False,image_icon)

                # image background encrypt
                bgEncrypt = ImageTk.PhotoImage(file="images/lock32.PNG", master=EncryptWin)
                bg_image = Label(EncryptWin,image=bgEncrypt, bd=0, width=300, height=300, background="black").place(x=150,y=260)

                # Image Frame
                f = Frame(EncryptWin, bd=3, bg="black", width=390, height=270, relief=GROOVE)
                f.place(x=570,y=260)

                # Show image in image frame 
                lbl = Label(f, bg="black")
                lbl.place(x=40, y=10)

                tip= Balloon(EncryptWin)
                # ========================================================#
                # ================= Entry field ==========================#
                # ========================================================#
                # Entry box for key
                entrykey = Entry(EncryptWin, font=("arial", 10, "bold"), bg="black", fg="white", highlightthickness=2)
                entrykey.config(highlightbackground = "gray", highlightcolor= "gray")
                entrykey.insert(0, " Auto Key Genrate. ")
                entrykey.place(x=570, y=580, width=390, height=28)

                # Pop Up Message Box
                tip.bind_widget(entrykey,balloonmsg='''Auto Key Genrate''')

                # Function delete entry box temparary text
                def remove_text(e):
                    entryFile.delete(0,"end")

                # Entry box for enter name of encrypt file
                entryFile = Entry(EncryptWin, font=("arial", 10, "bold"), bg="black", fg="white", highlightthickness=2)
                entryFile.config(highlightbackground = "gray", highlightcolor= "gray")
                entryFile.insert(0, "Enter Name Of Encrypt Image")
                entryFile.place(x=570, y=542, width=390, height=28)
                entryFile.bind("<FocusIn>", remove_text)

                # Pop Up Message Box
                tip.bind_widget(entryFile,balloonmsg='''Enter Name Of Encrypted File''')
                # ========================================================#
                # ================= Button      ==========================#
                # ========================================================#
                # Buttons select file and encrypt
                # Creating a photoimage object to use image
                selectFileBtn = PhotoImage(file = r"icons/open.png", master=EncryptWin)
                
                # Resizing image to fit on button
                selectBtn = selectFileBtn.subsample(18, 18)

                #Define functions change color of button
                def on_enter(e):
                    selBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    selBtn.config(background= '#313030', foreground= 'white')

                # Select File Button
                selBtn = Button(EncryptWin, text=" Select File", image = selectBtn, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=showimage)
                selBtn.place(x=630, y=630)

                #Bind the Enter 
                selBtn.bind('<Enter>', on_enter)
                selBtn.bind('<Leave>', on_leave)

                tip.bind_widget(selBtn,balloonmsg='''Button For Select File/Image From User Location''')

                # Creating a photoimage object to use image
                EncrptBtnIcon = PhotoImage(file = r"icons/padlock.png", master=EncryptWin)
                
                # Resizing image to fit on button
                EncrptBtn = EncrptBtnIcon.subsample(18, 18)

                #Define functions change color of button
                def on_enter(e):
                    enBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    enBtn.config(background= '#313030', foreground= 'white')

                # Encrypt Button
                enBtn = Button(EncryptWin, text=" Encrypt File", image = EncrptBtn, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=EncryptFile)
                enBtn.place(x=770, y=630)

                #Bind the Enter 
                enBtn.bind('<Enter>', on_enter)
                enBtn.bind('<Leave>', on_leave)

                tip.bind_widget(enBtn,balloonmsg='''Button For Encrypt Image''')

                # Creating a photoimage object to use image
                EncrptBackBtnIcon = PhotoImage(file = r"icons/back1.png", master=EncryptWin)
                
                # Resizing image to fit on button
                EncrptBackIcon = EncrptBackBtnIcon.subsample(1, 1)

                #Define functions change color of button
                def on_enter(e):
                    baBtn.config(background='#808080', foreground= "white")

                def on_leave(e):
                    baBtn.config(background= '#313030', foreground= 'white')

                # Back Button
                baBtn = Button(EncryptWin, text=" Back", image = EncrptBackIcon, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=back)
                baBtn.place(x=1300, y=800)


                #Bind the Enter 
                baBtn.bind('<Enter>', on_enter)
                baBtn.bind('<Leave>', on_leave)

                tip.bind_widget(baBtn,balloonmsg='''Button For Go Previous Page''')

                # # Creating a photoimage object to use image
                # EncrptExitBtnIcon = PhotoImage(file = r"icons/exit.png", master=EncryptWin)
                
                # # Resizing image to fit on button
                # EncrptIcon = EncrptExitBtnIcon.subsample(6, 6)

                # #Define functions change color of button
                # def on_enter(e):
                #     exBtn.config(background='#808080', foreground= "white")

                # def on_leave(e):
                #     exBtn.config(background= '#313030', foreground= 'white')

                # # Exit Button
                # exBtn = Button(EncryptWin, text=" Exit", image = EncrptIcon, compound = LEFT, bg="#232222", fg="white", 
                #         font=("time new roman", 10, "bold"), width=120, command=exit)
                # exBtn.place(x=1300, y=800)

                # #Bind the Enter 
                # exBtn.bind('<Enter>', on_enter)
                # exBtn.bind('<Leave>', on_leave)

                # tip.bind_widget(exBtn,balloonmsg='''Button For Exit Page''')

                EncryptWin.protocol("WM_DELETE_WINDOW", exit)

                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=EncryptWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    EncryptWin.state(newstate='iconic')
                    self.selecEnDeWin.state(newstate='iconic')

                minimizeBtn = Button(EncryptWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=EncryptWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=EncryptWin)
                    
                # Button minimize
                minimizeBtn = Button(EncryptWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')

                # Encrypt window main loop.
                EncryptWin.mainloop()

# =========================================================================== #
# ============================ Decrypt Window =============================== #
# =========================================================================== #
   
            # Decrypt Window function.
            def decrypt():
                DecryptWin = Tk()

                # Tip Tool use for show pop Message
                tip= Balloon(DecryptWin)

                # Tittle
                DecryptWin.title("Encrypt Image ")

                # Define window size with geometry function
                DecryptWin.geometry("650x250")
                DecryptWin.attributes('-fullscreen', True)
                DecryptWin.configure(bg="black")

                # Icon of image steganography title
                photopicc = PhotoImage(file = r"icons/de1.png", master=DecryptWin)
                
                # Resizing image to fit on button
                photoimagepic = photopicc.subsample(16, 16)

                # Label Creat Account
                labelacc= Label(DecryptWin, text= " Decryption Image ", image = photoimagepic, compound = LEFT, 
                                font=('Times New Roman bold',25), bg="black", fg="white")
                labelacc.place(x = 560, y = 110) 
                # ========================================================#
                # ================= Decrypt DES  =========================#
                # ========================================================#
                def decryptDES():
                    key=""
                    file_bytes=""
                    # Encode given key to 16 byte ascii key with md5 operation
                    key_hash = md5(key.encode('ascii')).digest()

                    # Adjust key parity of generated Hash Key for Final Triple DES Key
                    tdes_key = DES3.adjust_key_parity(key_hash)
                    
                    #  Cipher with integration of Triple DES key, MODE_EAX for Confidentiality & Authentication
                    #  and nonce for generating random / pseudo random number which is used for authentication protocol
                    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

                    # Perform Decryption operation
                    new_file_bytes = cipher.decrypt(file_bytes)
                # ========================================================#
                # ================= IMAGE STEGANOGRAPHY Name =============#
                # ========================================================#
                # Image Steganography text amination
                canvas = Canvas(DecryptWin, background="blue")
                canvas.place(x=630, y=180, width=272, height=40)
                canvas_t = canvas.create_text(10, 10, text='', anchor=NW, font=('Times New Roman bold',15))
                our_text = "IMAGE STEGANOGRAPHY"
                delta = 300
                delay = 0
                for x in range(len(our_text)+1):
                    s = our_text[:x]
                    new_text = lambda s=s: canvas.itemconfigure(canvas_t, text=s)
                    canvas.after(delay, new_text)
                    delay += delta

                # # Exit Button Function
                # def exit():
                #     if messagebox.askokcancel("Program Quite Status", "Do You Want To Exit Program?", master=DecryptWin):
                #         DecryptWin.destroy()
                #         self.selecEnDeWin.destroy()

                # Back Button Function
                def back():
                    DecryptWin.destroy()

                # Show data in entry field.
                def showEntry():
                    entryPathDecImg.delete(0,"end")
                    decrypFile.delete(0,"end")
                    decryptkey.delete(0,"end")
                    entryPathDecImg.insert(0, " Path Of Decrypted Image")
                    decrypFile.insert(0, " Enter Name Of Decrypt Image")
                    decryptkey.insert(0, " Enter Key For Decrypt Image")
                # global verioable for check image select or not.   
                global ch
                ch=0
                # ========================================================#
                # ================= select image =============#
                # ========================================================#
                # Function 
                def showimage():
                    
                    # global verioable for check image select or not.
                    global ch
                    ch=ch+1

                    # Use exception for catch exception. 
                    try:
                        global filename
                        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                            title="Select Image File",
                                                            filetypes=(("PNG file","*.png"),
                                                                            ("JPG file", "*.jpg"),
                                                                            ("All file","*.text")), master=DecryptWin)

                        entryPathDecImg.delete(0,"end")
                        entryPathDecImg.insert(0, filename)
                    # Catch exception here. 
                    except Exception as e:
                        messagebox.showerror("Decrypt Window Status", 'image not select '+str(e), master=DecryptWin)

                # Function Show encrypt image
                def showImageEncrypt():
                    # Use exception for catch exception.
                    try:
                        # Accress value from decrypt field.
                        decryptImgName = decrypFile.get()
                        # Label for encrypted image.
                        lblImgEn = Label(DecryptWin, text="Decrypt image "+str("[ ")+str(decryptImgName)+str(" ]"), font=("arial", 10, "bold"), bg="black", fg="white")
                        lblImgEn.place(x=570,y=250 )

                        # Accress value from decrypt field.
                        decryptFileName = decrypFile.get()
                        # Image Frame
                        f = Frame(DecryptWin, bd=3, bg="black", width=390, height=270, relief=GROOVE)
                        f.place(x=570,y=275)

                        # Show image in image frame 
                        lbl = Label(f, bg="black")
                        lbl.place(x=40, y=10)

                        img = PIL.Image.open(decryptFileName)
                        img = ImageTk.PhotoImage(img, master=DecryptWin)
                        lbl.configure(image=img,width=250,height=250)
                        lbl.image = img
                    # Catch exception.
                    except Exception as e:
                        messagebox.showerror("Decrypt Window Status", str(e))
                        

                # Encrypt File Button Functiom
                def DecryptFile():
                   
                    try:
                        key1 = decryptkey.get()
                        text_file = open("Key_Of_Encrypt.key", "r")
                        #read whole file to a string
                        key2 = text_file.read()
                        #close file
                        text_file.close()
                    except Exception as e:
                        messagebox.showerror('Error', str(e), master=DecryptWin)

                    # Access values from field. 
                    decryptFileName = decrypFile.get()
                    decryptKeyFile = decryptkey.get()
                    # Declare veriable to check condition image select or not
                    global ch
                    # Check conditions.
                    
                    if(decrypFile.get()==" Enter Name Of Decrypt Image" and decryptkey.get()==" Enter Key For Decrypt Image"):
                        messagebox.showerror('Error', 'All fields are required', master=DecryptWin)
                    elif(decrypFile.get()==" Enter Name Of Decrypt Image"):
                        messagebox.showerror('Error', 'Enter Name Of Decrypt Image field are required', master=DecryptWin)
                    elif(decryptkey.get()==" Enter Key For Decrypt Image"):
                        messagebox.showerror('Error', 'Enter Key For Decrypt Image field are required', master=DecryptWin)    
                    if(ch == 0):
                        messagebox.showerror('Error', 'Image not select first image select', master=DecryptWin)
                    elif(key1 != key2):
                        messagebox.showerror('Error', 'Invalid key please enter valid key', master=DecryptWin)
                    else:
                        # Use exception for catch exception.
                        try:
                            # Decryption key
                            fernet = Fernet(decryptKeyFile)
                            with open(filename, 'rb') as file:
                                encrypted_file = file.read()

                            # Decrypted file
                            decrypted = fernet.decrypt(encrypted_file)    

                            with open(decryptFileName, 'wb') as file:
                                file.write(decrypted)
                            # call functions.
                            showImageEncrypt()
                            showEntry()
                            messagebox.showinfo('Encrypt Image status', 'Successfully Image Decrypted', master=DecryptWin)
                        # Catch exception here.
                        except Exception as e:
                            # Declare veriable to check to condition image valid or invalid.
                            ch=0
                            # exception convert into string.
                            s = "Error {0}".format(str(e)) # string
                            utf8str = s.encode("utf-8")
                            le = len(utf8str)
                            # Check conditions.
                            if(le == 6):
                                messagebox.showerror("Decrypt Window Status", "Select invalid image please select valid image", master=DecryptWin)
                                ch = ch+1
                            if(ch == 0):
                                messagebox.showerror("Decrypt Window Status", str(e), master=DecryptWin)
                
                # Icon
                image_icon = PhotoImage(file="icons/enryp.png", master=DecryptWin)
                DecryptWin.iconphoto(False,image_icon)

                # image background decoding
                bgdecod = ImageTk.PhotoImage(file="images/de5.PNG", master=DecryptWin)
                bg_imagedecod = Label(DecryptWin,image=bgdecod, bd=0, width=300, height=300, background="black").place(x=1000,y=265)

                # Function Decrypt entry box temparary text
                def remove_textd_Decrypt(e):
                    decrypFile.delete(0,"end")

                # Function delete entry box temparary text
                def remove_text_Key(e):
                    decryptkey.delete(0,"end")

                # Creating a photoimage object to use image
                iconImagePath = PhotoImage(file = r"icons/pathway.png", master=DecryptWin)
                
                # Resizing image to fit on button
                resizeIconImagePath = iconImagePath.subsample(20, 20)

                # Label image path.
                lblPathImg = Label(DecryptWin, text="  Path Of Decrypted Image",image = resizeIconImagePath, compound = LEFT, font=("arial", 10, "bold"), bg="black", fg="white")
                lblPathImg.place(x=100, y=260)

                # Entry box for key
                entryPathDecImg = Entry(DecryptWin, font=("arial", 10, "bold"), bg="black", fg="white")
                entryPathDecImg.insert(0, " Path Of Decrypted Image")
                entryPathDecImg.place(x=100, y=300, width=390, height=28)

                # Creating a photoimage object to use image
                iconImageName = PhotoImage(file = r"icons/image.png", master=DecryptWin)
                
                # Resizing image to fit on button
                resizeIconImageName = iconImageName.subsample(4, 4)

                # Label name encrypt image.
                lblNameImg = Label(DecryptWin, text="  Enter Name Of Encrypt Image",image = resizeIconImageName, compound = LEFT, font=("arial", 10, "bold"), bg="black", fg="white")
                lblNameImg.place(x=100, y=340)

                # Entry box for enter name of decrypt file
                decrypFile = Entry(DecryptWin, font=("arial", 10, "bold"), bg="black", fg="white")
                decrypFile.insert(0, " Enter Name Of Decrypt Image")
                decrypFile.place(x=100, y=375, width=390, height=28)
                decrypFile.bind("<FocusIn>", remove_textd_Decrypt)
                tip.bind_widget(decrypFile,balloonmsg='''Enter Name Of Encrypt File''')

                # Creating a photoimage object to use image
                iconEnKey = PhotoImage(file = r"icons/key.png", master=DecryptWin)
                
                # Resizing image to fit on button
                resizeIconEnKey = iconEnKey.subsample(15, 15)

                # Label name encrypt image.
                lblNameImg = Label(DecryptWin, text="  Enter Key For Decrypt Image",image = resizeIconEnKey, compound = LEFT, font=("arial", 10, "bold"), bg="black", fg="white")
                lblNameImg.place(x=100, y=410)

                # Entry box for enter Key of Decrypt file
                decryptkey = Entry(DecryptWin, font=("arial", 10, "bold"), bg="black", fg="white")
                decryptkey.insert(0, " Enter Key For Decrypt Image")
                decryptkey.place(x=100, y=448, width=390, height=28)
                decryptkey.bind("<FocusIn>", remove_text_Key)
                tip.bind_widget(decryptkey,balloonmsg='''Enter Key For Decrypt Image''')

                   # Button for select key (Decode key text file).
                def open_file():
                    try:
                        """Open a file for editing."""
                        filepath = askopenfilename(
                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], master=DecryptWin
                        )

                        with open(filepath, "r") as input_file:
                            text = input_file.read()
                            decryptkey.delete(0, END)
                            decryptkey.insert(0,text)
                    except Exception as e:
                        messagebox.showerror('Encode key process status', str(e), master=DecryptWin)
                
                 #Define functions change color of button
                def on_enter(e):
                    btn_open2.config(background='#808080', foreground= "white")

                def on_leave(e):
                    btn_open2.config(background= '#313030', foreground= 'white')

                btn_open2 = Button(DecryptWin, text="Key", command=open_file, bg="#232222", fg="white")
                btn_open2.place(x=500, y=448)

                #Bind the Enter 
                btn_open2.bind('<Enter>', on_enter)
                btn_open2.bind('<Leave>', on_leave)

                tip.bind_widget(btn_open2,balloonmsg='''Button For Select key from folder''')

                # Buttons select file and encrypt
                # Creating a photoimage object to use image
                selectFileBtn = PhotoImage(file = r"icons/open.png", master=DecryptWin)
                
                # Resizing image to fit on button
                selectBtn = selectFileBtn.subsample(18, 18)

                # change color of button function
                def on_enter(e):
                    selBtn.config(background='#00008B', foreground= "white")

                def on_leave(e):
                    selBtn.config(background= '#313030', foreground= 'white')

                # Exit Select File
                selBtn = Button(DecryptWin, text=" Select File", image = selectBtn, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=showimage)
                selBtn.place(x=140, y=520)

                #Bind the Enter 
                selBtn.bind('<Enter>', on_enter)
                selBtn.bind('<Leave>', on_leave)

                tip.bind_widget(selBtn,balloonmsg='''Button For Select File/Image From User Location''')

                # Creating a photoimage object to use image
                decrptBtnIcon = PhotoImage(file = r"icons/unlocked1.png", master=DecryptWin)
                
                # Resizing image to fit on button
                decrptBtn = decrptBtnIcon.subsample(18, 18)

                #Define functions change color of button
                def on_enter(e):
                    deBtn.config(background='#00008B', foreground= "white")

                def on_leave(e):
                    deBtn.config(background= '#313030', foreground= 'white')

                # Exit Button
                deBtn = Button(DecryptWin, text=" Decrypt File", image = decrptBtn, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=DecryptFile)
                deBtn.place(x=280, y=520)

                #Bind the Enter 
                deBtn.bind('<Enter>', on_enter)
                deBtn.bind('<Leave>', on_leave)

                tip.bind_widget(deBtn,balloonmsg='''Button For Decrypted File/Image''')

                # Creating a photoimage object to use image
                EncrptBackBtnIcon = PhotoImage(file = r"icons/back1.png", master=DecryptWin)
                
                # Resizing image to fit on button
                EncrptBackIcon = EncrptBackBtnIcon.subsample(1, 1)

                #Define functions change color of button
                def on_enter(e):
                    baBtn.config(background='#00008B', foreground= "white")

                def on_leave(e):
                    baBtn.config(background= '#313030', foreground= 'white')

                # Back Button
                baBtn = Button(DecryptWin, text=" Back", image = EncrptBackIcon, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=back)
                baBtn.place(x=1300, y=800)

                #Bind the Enter 
                baBtn.bind('<Enter>', on_enter)
                baBtn.bind('<Leave>', on_leave)

                tip.bind_widget(baBtn,balloonmsg='''Button For Go Previous Page''')

                # # Creating a photoimage object to use image
                # EncrptExitBtnIcon = PhotoImage(file = r"icons/exit.png", master=DecryptWin)
                
                # # Resizing image to fit on button
                # EncrptIcon = EncrptExitBtnIcon.subsample(6, 6)

                # #Define functions change color of button
                # def on_enter(e):
                #     exBtn.config(background='#00008B', foreground= "white")

                # def on_leave(e):
                #     exBtn.config(background= '#313030', foreground= 'white')

                # # Exit Button
                # exBtn = Button(DecryptWin, text=" Exit", image = EncrptIcon, compound = LEFT, bg="#232222", fg="white", 
                #         font=("time new roman", 10, "bold"), width=120, command=exit)
                # exBtn.place(x=1300, y=800)


                # #Bind the Enter 
                # exBtn.bind('<Enter>', on_enter)
                # exBtn.bind('<Leave>', on_leave)

                # tip.bind_widget(exBtn,balloonmsg='''Button For Exit Page''')

                DecryptWin.protocol("WM_DELETE_WINDOW", exit)

                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=DecryptWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    DecryptWin.state(newstate='iconic')
                    self.selecEnDeWin.state(newstate='iconic')

                minimizeBtn = Button(DecryptWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=DecryptWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=DecryptWin)
                    
                # Button minimize
                minimizeBtn = Button(DecryptWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')

                # Decrypt Window main loop.
                DecryptWin.mainloop()


# ================================================================================= #
# ============================ About Project Window =============================== #
# ================================================================================= #

            # About project button function
            def aboutProject():
                
                # Create about project window
                aboutProjectWin = Tk()

                # Window size.
                aboutProjectWin.geometry("650x250")
                aboutProjectWin.attributes('-fullscreen', True)

                # Background Color.
                aboutProjectWin.configure(bg='black')

                # Label for show project name.
                labelproj=Label(aboutProjectWin,text='ABOUT PROJECT ' ,fg='grey',bg="black", width=15, height=1, highlightthickness=2)
                font=('Calibri (Body)',24,'bold')

                # highlightbackground and highlightcolor for the border color
                labelproj.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                labelproj.config(font=font)
                labelproj.place(x=550,y=70)

                # Label for show project method.
                labelprojName=Label(aboutProjectWin,text='NAME: Image Steganography' ,fg='grey',bg="black", width=25, height=1, highlightthickness=2)
                font=('Calibri (Body)',24,'bold')

                # highlightbackground and highlightcolor for the border color
                labelprojName.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                labelprojName.config(font=font)
                labelprojName.place(x=447,y=123)

                # Label for show project method.
                labelprojMethod=Label(aboutProjectWin,text='PROJECT METHOD: Least Significant Bit (LSB)' ,fg='grey',bg="black", width=40, height=1, highlightthickness=2)
                font=('Calibri (Body)',24,'bold')

                # highlightbackground and highlightcolor for the border color
                labelprojMethod.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                labelprojMethod.config(font=font)
                labelprojMethod.place(x=310,y=177)

                # Label for show project info.
                labelprojInfo=Label(aboutProjectWin,text='Project information' ,fg='grey',bg="black", width=15, height=1, highlightthickness=2)
                
                # highlightbackground and highlightcolor for the border color
                labelprojInfo.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                font=('Calibri (Body)',10,'bold')
                labelprojInfo.config(font=font)
                labelprojInfo.place(x=420,y=540)

                # Label for show project diagram.
                labelprojDiagram=Label(aboutProjectWin,text='Project diagram proccess' ,fg='grey',bg="black", width=20, height=1, highlightthickness=2)
                
                # highlightbackground and highlightcolor for the border color
                labelprojDiagram.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                font=('Calibri (Body)',10,'bold')
                labelprojDiagram.config(font=font)
                labelprojDiagram.place(x=850,y=540)

                # Image Steganography text amination
                canvas1 = Canvas(aboutProjectWin, background="#1475f5")
                canvas1.place(x=300, y=590, width=660, height=150)
                canvas_t1 = canvas1.create_text(10, 10, text='', anchor=NW, font=('Times New Roman bold',12))
                our_text1 = '''
                Algorithm Of Program ....
                Step_1: Encode Function || Select (Image + Secrect) Convert Binery|| Extrect RGB
                values use (LSB add Message + Key) and resize image (Convert original image).
                Step_2: Encrypt Function || Select Encoded image + Key Convert Encrypt image.
                Step_3: Decrypt Function || Select Encrypted + Key Convert into Encode Image.
                Step_4: Decode Function || Select Decrypted Image + Key Then Show Message.'''
                delta1 = 300
                delay1 = 0
                for x in range(len(our_text1)+1):
                    s = our_text1[:x]
                    new_text1 = lambda s=s: canvas1.itemconfigure(canvas_t1, text=s)
                    canvas1.after(delay1, new_text1)
                    delay1 += delta1

                # # Exit button function.
                # def exit():
                #     if messagebox.askokcancel("Quit Program", "Do you want to quit?", master =aboutProjectWin):
                #         aboutProjectWin.destroy()
                #         self.selecEnDeWin.destroy()
                
                # aboutProjectWin.protocol("WM_DELETE_WINDOW", exit)

                # text write code
                font=('Calibri (Body)',15,'bold')
                aboutProjText = Text(aboutProjectWin, font = font, bg="black", fg="grey", bd=0, highlightthickness=2)
                aboutProjText.insert(END, '''Steganography is the process of hiding one file inside another such that others can neither identify the meaning of the embedded object nor even recognize its existence. The main objective of Steganography is mainly concerned with the protection of contents of the hidden information. Images are ideal for information hiding because of the large amount of redundant space is created in the storing of images. Since this can be done in several ways, image steganography is studied and one of these methods has been used to demonstrate it here i.e. The LSB technique in which the least significant bit of every byte is altered to form the bitstring representing the embedded file. Altering the LSB will only cause minor changes in color, and thus is usually not noticeable to the human eye. While this technique works well for 24-bit color image files, steganography has not been as successful when using an 8-bit color image file, due to limitations in color variations and the use of a color-map During its implementation, after the process of compression, a text message is hidden in the final, compressed image. This hidden information can be retrieved only through proper decoding technique.''')

                # highlightbackground and highlightcolor for the border color
                aboutProjText.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                aboutProjText.place(x=300, y=250,width=400,height=275)

                scrollbar = Scrollbar(aboutProjectWin, orient=VERTICAL, command=aboutProjText.yview,  highlightthickness=2)
                scrollbar.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                scrollbar.place(x=700, y=250, height=275)
                aboutProjText.config(yscrollcommand=scrollbar.set)

                # imageAbproj = Image.open("images/aboutProject.png", master=aboutProjectWin)

                # Creating a photoimage object to use image
                imageAbproj = PhotoImage(file = r"images/aboutProject.png", master=aboutProjectWin)

                # Resizing image to fit on button
                resize_imageAbproj = imageAbproj.subsample(2, 2)

                # Show image Steganography icon using label.
                abProjImglbl = Label( aboutProjectWin, image = resize_imageAbproj, bd=0, bg="black", highlightthickness=2)

                # highlightbackground and highlightcolor for the border color
                abProjImglbl.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                abProjImglbl.place(x = 750, y = 250)

                # Back button function.
                def back():
                    aboutProjectWin.destroy()

                # Creating a photoimage object to use image
                abProjBackBtnIcon = PhotoImage(file = r"icons/back1.png", master=aboutProjectWin)
                
                # Resizing image to fit on button
                abProjBackIcon = abProjBackBtnIcon.subsample(1, 1)

                #Define functions change color of button
                def on_enter(e):
                    baBtn.config(background='#00008B', foreground= "white")

                def on_leave(e):
                    baBtn.config(background= '#313030', foreground= 'white')

                # Back Button
                baBtn = Button(aboutProjectWin, text=" Back", image = abProjBackIcon, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=back)
                baBtn.place(x=1300, y=800)

                #Bind the Enter 
                baBtn.bind('<Enter>', on_enter)
                baBtn.bind('<Leave>', on_leave)

                tip.bind_widget(baBtn,balloonmsg='''Button For Go Previous Page''')

                # # Creating a photoimage object to use image
                # iconExitBtn = PhotoImage(file = r"icons/exit.png", master=aboutProjectWin)

                # # Resizing image to fit on button
                # iconExitBtnResize = iconExitBtn.subsample(6, 6)

                # #Define functions
                # def on_enter(e):
                #     exitBtnAbPro.config(background='#0a21f2', foreground= "white")

                # def on_leave(e):
                #     exitBtnAbPro.config(background= '#313030', foreground= 'white')
                
                # # Exit button 
                # exitBtnAbPro = Button(aboutProjectWin, text="  Exit ", image = iconExitBtnResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=100 , command=exit)
                # exitBtnAbPro.place(x=1300, y=800)
                
                # #Bind function
                # exitBtnAbPro.bind('<Enter>', on_enter)
                # exitBtnAbPro.bind('<Leave>', on_leave)

                # # bind function for show message.
                # tip.bind_widget(exitBtnAbPro,balloonmsg='''Exit program.''')

                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=aboutProjectWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    aboutProjectWin.state(newstate='iconic')
                    self.selecEnDeWin.state(newstate='iconic')

                minimizeBtn = Button(aboutProjectWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=aboutProjectWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showinfo("encode Window Status", "Window cann't resize", master=aboutProjectWin)
                    
                # Button minimize
                minimizeBtn = Button(aboutProjectWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')   

                # About project window main loop.           
                aboutProjectWin.mainloop()

#==========================================================================#
#======================= Encode and Decode window code ====================#
#==========================================================================#

            # #Exit button function.
            # def exit():
            #     if messagebox.askokcancel("Quit Program", "Do you want to quit?"):
            #         self.selecEnDeWin.destroy()

            # Creating a photoimage object to use icon (binary2.png)
            iconImgSteg = PhotoImage(file = r"icons/pngegg.png")

            # Resizing image to fit on button
            iconImgStegResize = iconImgSteg.subsample(10, 10)
            
            # Create label
            Label(self.selecEnDeWin,image = iconImgStegResize, bg="black").place(x=680,y=100)

            # Image Steganography text amination
            canvas = Canvas(self.selecEnDeWin, background="#1475f5")
            canvas.place(x=585, y=190, width=272, height=40)
            canvas_t = canvas.create_text(10, 10, text='', anchor=NW, font=('Times New Roman bold',15))
            our_text = "IMAGE STEGANOGRAPHY"
            delta = 300
            delay = 0
            for x in range(len(our_text)+1):
                s = our_text[:x]
                new_text = lambda s=s: canvas.itemconfigure(canvas_t, text=s)
                canvas.after(delay, new_text)
                delay += delta
                
            labelProcess = Label(self.selecEnDeWin, text="Processes Of Program.", font=('Times New Roman bold',13), bg="black", fg="white")
            labelProcess.place(x=190, y=280)
            # Image Steganography text amination
            canvas1 = Canvas(self.selecEnDeWin, background="#1475f5")
            canvas1.place(x=190, y=310, width=272, height=170)
            canvas_t1 = canvas1.create_text(10, 10, text='', anchor=NW, font=('Times New Roman bold',12))
            our_text1 = '''
            Processes Of Program ....
            Step_1: Encode Image.
            Step_2: Encrypt Image.
            Step_3: Decrypt Image.
            Step_4: Decode Image.
            Step_5: Show Message.'''
            delta1 = 300
            delay1 = 0
            for x in range(len(our_text1)+1):
                s = our_text1[:x]
                new_text1 = lambda s=s: canvas1.itemconfigure(canvas_t1, text=s)
                canvas1.after(delay1, new_text1)
                delay1 += delta1
            #===============================================#
            # =========== frame and button code ============#
            #===============================================#
            # Define frame (Select encode or decode ectt window).
            self.frameSelEnDe = Frame(self.selecEnDeWin, bg="#313030", bd=0, highlightthickness=2)
            self.frameSelEnDe.config(highlightbackground = "#1475f5", highlightcolor= "#1475f5")
            self.frameSelEnDe.place(x=570, y=250, width=300, height=300)

            # Creating a photoimage object to use image
            IconBtnEn = PhotoImage(file = r"icons/lock.png", master=self.selecEnDeWin)

            # Resizing image to fit on button
            IconBtnEnResize = IconBtnEn.subsample(25, 25)
            
            #Define functions
            def on_enter(e):
                enBtn.config(background='#0a21f2', foreground= "white")

            def on_leave(e):
                enBtn.config(background= '#313030', foreground= 'white')

            enBtn = Button(self.frameSelEnDe, text="  Encode ", image = IconBtnEnResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 15, "bold"),width=160, command=encoding)
            enBtn.place(x=65, y=35)
            
            #Bind function
            enBtn.bind('<Enter>', on_enter)
            enBtn.bind('<Leave>', on_leave)

            # bind function for show message.
            tip.bind_widget(enBtn,balloonmsg='''Encode button for hide information in  image.''')
             
            # Creating a photoimage object to use image
            IconBtnDe = PhotoImage(file = r"icons/unlock1.png", master=self.selecEnDeWin)

            # Resizing image to fit on button
            IconBtnDeResize = IconBtnDe.subsample(25, 25)
 

            #Define functions
            def on_enter(e):
                deBtn.config(background='#0a21f2', foreground= "white")

            def on_leave(e):
                deBtn.config(background= '#313030', foreground= 'white')

            deBtn = Button(self.frameSelEnDe, text="  Decode ",image = IconBtnDeResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 15, "bold"), width=160, command=decoding)
            deBtn.place(x=65, y=85)

            #Bind function
            deBtn.bind('<Enter>', on_enter)
            deBtn.bind('<Leave>', on_leave)

            # bind function for show message.
            tip.bind_widget(deBtn,balloonmsg='''Decode button for show information fron hide information image.''')
     
            # Creating a photoimage object to use image
            IconBtnEncrypt = PhotoImage(file = r"icons/lock1.png", master=self.selecEnDeWin)

            # Resizing image to fit on button
            IconBtnEncryptResize = IconBtnEncrypt.subsample(25, 25)
 

            #Define functions
            def on_enter(e):
                encrBtn.config(background='#0a21f2', foreground= "white")

            def on_leave(e):
                encrBtn.config(background= '#313030', foreground= 'white')

            encrBtn = Button(self.frameSelEnDe, text="  Encrypt ",image = IconBtnEncryptResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 15, "bold"), width=160, command=encrypt)
            encrBtn.place(x=65, y=135)

            #Bind function
            encrBtn.bind('<Enter>', on_enter)
            encrBtn.bind('<Leave>', on_leave)

            # bind function for show message.
            tip.bind_widget(encrBtn,balloonmsg='''Encrypt button for encrypt image.''')

            # Creating a photoimage object to use image
            IconBtnDecrypt = PhotoImage(file = r"icons/unlock2.png", master=self.selecEnDeWin)

            # Resizing image to fit on button
            IconBtnDecryptResize = IconBtnDecrypt.subsample(25, 25)
 

            #Define functions
            def on_enter(e):
                decrBtn.config(background='#0a21f2', foreground= "white")

            def on_leave(e):
                decrBtn.config(background= '#313030', foreground= 'white')

            decrBtn = Button(self.frameSelEnDe, text="  Decrypt ",image = IconBtnDecryptResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 15, "bold"), width=160, command=decrypt)
            decrBtn.place(x=65, y=185)

            #Bind function
            decrBtn.bind('<Enter>', on_enter)
            decrBtn.bind('<Leave>', on_leave)

            # bind function for show message.
            tip.bind_widget(decrBtn,balloonmsg='''Decrypt button for decrypt image.''')
     

            # Creating a photoimage object to use image
            iconProjBtn = PhotoImage(file = r"icons/project.png", master=self.selecEnDeWin)

            # Resizing image to fit on button
            iconProjBtnResize = iconProjBtn.subsample(21, 21)   

            #Define functions
            def on_enter(e):
                aboutProjBtn.config(background='#0a21f2', foreground= "white")

            def on_leave(e):
                aboutProjBtn.config(background= '#313030', foreground= 'white')

            aboutProjBtn = Button(self.frameSelEnDe, text="  About Project ",image = iconProjBtnResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 13, "bold"), width=160, command=aboutProject)
            aboutProjBtn.place(x=65, y=235)

            #Bind function
            aboutProjBtn.bind('<Enter>', on_enter)
            aboutProjBtn.bind('<Leave>', on_leave)

            # bind function for show message.
            tip.bind_widget(aboutProjBtn,balloonmsg='''Show information about project.''')

            # # Creating a photoimage object to use image
            # iconExitBtn = PhotoImage(file = r"icons/exit.png")

            # # Resizing image to fit on button
            # iconExitBtnResize = iconExitBtn.subsample(6, 6)

            # #Define functions
            # def on_enter(e):
            #     exitBtn.config(background='#0a21f2', foreground= "white")

            # def on_leave(e):
            #     exitBtn.config(background= '#313030', foreground= 'white')

            # exitBtn = Button(self.selecEnDeWin, text="  Exit ", image = iconExitBtnResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=100 , command=exit)
            # exitBtn.place(x=1300, y=800)
            # #Bind function
            # exitBtn.bind('<Enter>', on_enter)
            # exitBtn.bind('<Leave>', on_leave)

            # # bind function for show message.
            # tip.bind_widget(exitBtn,balloonmsg='''Exit program.''')
            # self.selecEnDeWin.protocol("WM_DELETE_WINDOW", exit)
            #===============================================#
            # ======= Logout and store time and date DB ====#
            #===============================================#
            def logout():
                if messagebox.askokcancel("Logout status", "Do you want to logout ?"):
                
                    # self.selecEnDeWin.quit(self)
                    # mainlogout(self)
                    # loginWin = Toplevel()
                    self.selecEnDeWin.destroy()
                    # log()
                    global name
                    username=name
                    print("Name Loggggg "+str(name))

                    datetime1=dt.datetime.now()
                    # Format the date
                    format_date=f"{datetime1:%a, %b %d %Y}"
                    date = str(format_date)

                    time_string = strftime('%H:%M:%S %p')
                    time = str(time_string)
                    # datetime = str(datetime1)

                    con = pymysql.connect(host="localhost", user="root", password="", database="imgstegregistrationaccount")
                    cur = con.cursor()
                    
                    cur.execute("insert into userlogoutrecord values('"+ username +"', '"+ date +"', '"+ time +"')")
                    cur.execute("commit") 
                    con.close()
                    loginWin = Tk()
                    # Create object Login class.
                    obj = Login(loginWin) 
                    # self.selecEnDeWin.after(4400,mainprogram)

            # Creating a photoimage object to use image
            iconLogOutBtn = PhotoImage(file = r"icons/logout2.png")

            # Resizing image to fit on button
            iconLogOutResize = iconLogOutBtn.subsample(5, 5)

            #Define functions
            def on_enter(e):
                logOutBtn.config(background='#0a21f2', foreground= "white")

            def on_leave(e):
                logOutBtn.config(background= '#313030', foreground= 'white')

            logOutBtn = Button(self.selecEnDeWin, text="  Logout ", image = iconLogOutResize, compound = LEFT , bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=100 , command=logout)
            logOutBtn.place(x=1300, y=800)
            
            #Bind function
            logOutBtn.bind('<Enter>', on_enter)
            logOutBtn.bind('<Leave>', on_leave)
            
            # Encode and Decde window main loop.
            self.selecEnDeWin.mainloop()

# ======================================================================================= #
# ========================= Welcome Splash Window ======================================= #
# ======================================================================================= #

        def welSplashWin():
         
            # Welcome window.
            class loadingSplash:
                def __init__(self) -> None:
                    # setting splash window.
                    # self.splashWin = Toplevel(loginWin)
                    self.splashWin = Tk()
                    self.splashWin.config(bg="black")
                    self.splashWin.title("Welcome Image Steganography")
                    self.splashWin.attributes("-fullscreen", True)

                    # Open image (wel4.png).
                    self.image = Image.open("images/wel4.png")

                    # Resize the image using resize() method.
                    self.resize_image = self.image.resize((550, 550))

                    self.userImg = ImageTk.PhotoImage(self.resize_image)

                    # Show image Steganography icon using label.
                    labelUserImg = Label( self.splashWin, image = self.userImg, bd=0, bg="black" )
                    labelUserImg.place(x = 468, y = 70)

                    # Label for show user name.
                    labelUserName=Label(self.splashWin,text='WELCOME '+str(userName).upper(),fg='grey',bg="black", width=50, height=3, highlightthickness=2)
                    font=('Calibri (Body)',24,'bold')

                    # highlightbackground and highlightcolor for the border color
                    labelUserName.config(highlightbackground = "#6cc1e3", highlightcolor= "#6cc1e3")
                    labelUserName.config(font=font)
                    labelUserName.place(x=250,y=350)

                    # Loading text.
                    Label(self.splashWin, text="Lo", font="Bahnschrift 15", bg="black", fg="#1fc6f3").place(x=525, y=620)

                    # Loading text.
                    Label(self.splashWin, text="ad", font="Bahnschrift 15", bg="black", fg="#f31f1f").place(x=548, y=620)

                    # Loading text.
                    Label(self.splashWin, text="in", font="Bahnschrift 15", bg="black", fg="#0860f0").place(x=570, y=620)

                    # Loading text.
                    Label(self.splashWin, text="g", font="Bahnschrift 15", bg="black", fg="#f008eb").place(x=588, y=620)

                    # Loading text.
                    Label(self.splashWin, text="..", font="Bahnschrift 15", bg="black", fg="#f0c708").place(x=602, y=620)

                    # Loading text.
                    Label(self.splashWin, text="..", font="Bahnschrift 15", bg="black", fg="#1cf008").place(x=613, y=620)

                    # Loading Blocks yellow.
                    for i in range(16):
                        Label(self.splashWin, bg="yellow", width=2, height=1).place(x=(i+24)*22, y=650)

                    # dpdate window see amination.
                    self.splashWin.update()
                    self.play_animation()

                    # Window in loop.
                    self.splashWin.mainloop()

                # Loader animation.
                def play_animation(self):
                    for i in range(1):
                        for j in range(16):

                            # Make blocks #6cc1e3.
                            Label(self.splashWin, bg="#6cc1e3", width=2, height=1).place(x=(j+24)*22, y=650)
                            sleep(0.06)
                            self.splashWin.update_idletasks()

                            # Make blocks #0a1bfc.
                            Label(self.splashWin, bg="#0a1bfc", width=2, height=1).place(x=(j+24)*22, y=650)
                            sleep(0.06)
                            self.splashWin.update_idletasks()

                            # Make blocks #fc0a0a.
                            Label(self.splashWin, bg="#fc0a0a", width=2, height=1).place(x=(j+24)*22, y=650)
                            sleep(0.06)
                            self.splashWin.update_idletasks()

                            # Make blocks #8d00f3.
                            Label(self.splashWin, bg="#8d00f3", width=2, height=1).place(x=(j+24)*22, y=650)
                            sleep(0.06)
                            self.splashWin.update_idletasks()

                            # Make blocks #1fc6f3.
                            Label(self.splashWin, bg="#1fc6f3", width=2, height=1).place(x=(j+24)*22, y=650)


                    else:
                        self.splashWin.destroy()
                        encodeDecodeWin(self)

                
            # loadingSplashClass call.
            if __name__ == "__main__":
                loadingSplash() 
            splashWin.mainloop()

# ======================================================================== #
# ======================= Login Class And Clock ========================== #
# ======================================================================== #

        # Define login class.
        class Login:

            # Define login class constructor and parameter.
            def __init__(self, loginWin):
                self.loginWin = loginWin

                # Use tip tool ( Display message when hovering over something with mouse cursor ).
                tip= Balloon(self.loginWin)

                # Window size.
                self.loginWin.geometry("650x250")
                loginWin.attributes('-fullscreen', True)

                # Creating a photoimage object to use image
                self.iconMinizeBtn = PhotoImage(file = r"icons/min.png", master=self.loginWin)
                
                # Resizing image to fit on button
                self.resizeIconMinizeBtn = self.iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    self.loginWin.state(newstate='iconic')

                minimizeBtn = Button(self.loginWin, image = self.resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')


                # Creating a photoimage object to use image
                self.iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=self.loginWin)
                
                # Resizing image to fit on button
                self.resizeIconRestoreDownBtn = self.iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown1(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=self.loginWin)
                    
                # Button minimize
                minimizeBtn1 = Button(self.loginWin, image = self.resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown1)
                minimizeBtn1.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn1,balloonmsg='''Restore down Window''')

                # Time code.

                from time import strftime

                # Function time.
                def time():

                    time_string = strftime('%H:%M:%S %p \n %A \n %x')
                    clockLbl.config(text=time_string)
    
                    # 1000 mean 1 second change.
                    clockLbl.after(1000, time)

                font = ('time', 13, 'bold')
                clockLbl = Label(self.loginWin, font=font, bg="black", fg="#357EC7", highlightthickness=2)
                clockLbl.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                clockLbl.grid(row=1, column=1, padx=100, pady=750)

                # call time function.
                time()

                # Background Color.
                self.loginWin.configure(bg='black')

                # Logo use.
                self.loginIcon = PhotoImage(file = 'icons/name13.png')

                # Setting icon of master window
                self.loginWin.iconphoto(False, self.loginIcon)
                
                # Title set window.
                loginWin.title('Login Window Image Steganography')

                # Creating a photoimage object to use icon.
                self.nameIcon = PhotoImage(file = r"icons/name13.png")
  
                # Resizing icon.
                self.nameIconResize = self.nameIcon.subsample(2, 2)

                # Label Image Sterganography.
                labelImgStg = Label(self.loginWin, text= "  Image Steganography Login Form", image = self.nameIconResize, compound = LEFT, font=('Times New Roman bold',15), bg="black", fg="#357EC7", highlightthickness=2)
                labelImgStg.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                labelImgStg.place(x = 805, y = 530)

                # Creating a photoimage object to use icon
                self.iconImgStgno = PhotoImage(file = r"icons/binary2.png")
  
                # Resizing icon.
                self.iconImgStgResize = self.iconImgStgno.subsample(13, 13)

                # Label Image Sterganography.
                labellmgStag = Label(self.loginWin, text= " Image Steganography ", image = self.iconImgStgResize, compound = LEFT, font=('Times New Roman bold',15), bg="black", fg="#357EC7", highlightthickness=2)
                labellmgStag.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                labellmgStag.place(x = 230, y = 110)
                
                # Background Color.
                self.loginWin.configure(bg='black')

                # Open image (login10.png).
                self.image = Image.open("images/login10.png")
 
                # Resize the image using resize() method.
                self.resize_image = self.image.resize((330, 330))
 
                self.userImg = ImageTk.PhotoImage(self.resize_image)

                # Show image Steganography icon using label.
                labelUserImg = Label( self.loginWin, image = self.userImg, bd=0, bg="black" )
                labelUserImg.place(x = 800, y = 190)

                # Define Frame
                Frame_Login = Frame(self.loginWin, bg="#313030", highlightthickness=2)
                Frame_Login.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                Frame_Login.place(x=100,y=170, width=500, height=430)

                # Label for tittle.
                title = Label(Frame_Login,text="Login Here",font=("Impact",35,"bold"), fg="#B4B0B0", bg="#313030")
                title.place(x=90,y=30)
                descrip = Label(Frame_Login,text="Image Steganography Login Form",font=("Goudy old style",15,"bold"), fg="#B4B0B0", bg="#313030")
                descrip.place(x=90,y=100)
                # Creating a photoimage object to use icon.
                self.iconUserName = PhotoImage(file = r"icons/name13.png")
  
                # Resizing icon.
                self.iconUserNameResize = self.iconUserName.subsample(2, 2)

                # Entry field(user name).
                lbl_user = Label(Frame_Login,text="  User email", image = self.iconUserNameResize, compound = LEFT, font=("Goudy old style",13,"bold"), fg="#B4B0B0", bg="#313030").place(x=90,y=140)
                self.u_email = Entry(Frame_Login, font=("time new roman", 13), bg="lightgray", highlightthickness=2)
                self.u_email.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                self.u_email.place(x=90, y=170, width=350, height=30)

                # bind function for show message.
                tip.bind_widget(self.u_email,balloonmsg=''' Enter user name.''')

                # Creating a photoimage object to use icon.
                self.iconPass = PhotoImage(file = r"icons/key21.png")
  
                # Resizing icon.
                self.iconPassResize = self.iconPass.subsample(2, 2)

                # Define string veriable.
                self.e1_str=StringVar() 
                
                # Define label and entry field (user password).
                lbl_pass = Label(Frame_Login,text="  User password", image = self.iconPassResize, compound = LEFT, font=("Goudy old style",13,"bold"), fg="#B4B0B0", bg="#313030").place(x=90,y=210)
                self.u_pass = Entry(Frame_Login, font=("time new roman", 13), bg="lightgray",show='*', textvariable=self.e1_str, highlightthickness=2)
                self.u_pass.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                self.u_pass.place(x=90, y=241, width=350, height=30)

                # bind function for show message.
                tip.bind_widget(self.u_pass,balloonmsg=''' Enter user password.''')

                # Define check button function.
                self.c_v1=IntVar(value=0)
                def my_show():
                    if(self.c_v1.get()==1):
                        self.u_pass.config(show='')
                    else:
                        self.u_pass.config(show='*')
                # Check button.
                self.checkBtn = Checkbutton(Frame_Login ,variable=self.c_v1, bg="#313030",
	                onvalue=1,offvalue=0,command=my_show)

                self.checkBtn.place(x=450 ,y=245)

                # bind function for show message.
                tip.bind_widget(self.checkBtn,balloonmsg='''Show password.''')

                # Creating a photoimage object to use icon
                self.iconPassword = PhotoImage(file = r"icons/password2.png")
  
                # Resizing image to fit on button
                self.iconPasswordResize = self.iconPassword.subsample(4, 4)

                # Creating a photoimage object to use icon.
                self.iconUserId = PhotoImage(file = r"icons/id5.png")
  
                # Resizing icon.
                self.iconUserIdResize = self.iconUserId.subsample(20, 20)

                # Entry field(user name).
                lbl_userId = Label(Frame_Login,text="  User ID", image = self.iconUserIdResize, compound = LEFT, font=("Goudy old style",13,"bold"), fg="#B4B0B0", bg="#313030").place(x=90,y=280)
                self.u_id = Entry(Frame_Login, font=("time new roman", 13), bg="lightgray",show='*', highlightthickness=2)
                self.u_id.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                self.u_id.place(x=90, y=313, width=108, height=30)

                # bind function for show message.
                tip.bind_widget(self.u_id,balloonmsg=''' Show user id which genrate auto.''')

                # Define check button function.
                self.c_v11=IntVar(value=0)
                def my_show1():
                    if(self.c_v11.get()==1):
                        self.u_id.config(show='')
                    else:
                        self.u_id.config(show='*')
                # Check button.
                self.checkBtn1 = Checkbutton(Frame_Login ,variable=self.c_v11, bg="#313030",
	                onvalue=1,offvalue=0,command=my_show1)

                self.checkBtn1.place(x=203 ,y=316)

                # bind function for show message.
                tip.bind_widget(self.checkBtn1,balloonmsg='''Show password.''')
                
                #Define functions
                def on_enter(e):
                    Forget_btn.config(background='#357EC7', foreground= "white")

                def on_leave(e):
                    Forget_btn.config(background= '#313030', foreground= 'white')

                # Forget Button
                Forget_btn = Button(Frame_Login, text="  Forget password ?", image = self.iconPasswordResize, compound = LEFT, cursor="hand2", bg="#313030", fg="#B4B0B0", bd=0, font=("time new roman", 10, "bold"), command=self.forGetPass, highlightthickness=2)
                Forget_btn.config(highlightbackground = "#357EC7", highlightcolor= "#357EC7")
                Forget_btn.place(x=90, y=365)

                #Bind function
                Forget_btn.bind('<Enter>', on_enter)
                Forget_btn.bind('<Leave>', on_leave)

                # bind function for show message.
                tip.bind_widget(Forget_btn,balloonmsg='''Button For Forget password.''')

                # Creating a photoimage object to use icon.
                self.iconAccount = PhotoImage(file = r"icons/accoun1.png")
  
                # Resizing icon.
                self.iconAccountResize = self.iconAccount.subsample(20, 20)

                #Define functions
                def on_enter(e):
                    account_btn.config(background='#357EC7', foreground= "white")

                def on_leave(e):
                    account_btn.config(background= '#313030', foreground= 'white')

                # Account Button
                account_btn = Button(Frame_Login, text="  For Account Create", image = self.iconAccountResize, compound = LEFT, cursor="hand2", bg="#313030", fg="#B4B0B0", bd=0, font=("time new roman", 10, "bold"), command=self.createAccount)
                account_btn.place(x=300, y=365)
 
                #Bind function
                account_btn.bind('<Enter>', on_enter)
                account_btn.bind('<Leave>', on_leave)

                # bind function for show message.
                tip.bind_widget(account_btn,balloonmsg='''Button For Account Create.''')

                # Creating a photoimage object to use icon.
                self.iconLogin = PhotoImage(file = r"icons/login5.png")
  
                # Resizing image to fit on button
                self.iconLoginResize = self.iconLogin.subsample(2, 2)

                #Define functions
                def on_enter(e):
                    Login_btn.config(background='#357EC7', foreground= "white")

                def on_leave(e):
                    Login_btn.config(background= '#313030', foreground= 'white')

                # Login Button
                Login_btn = Button(self.loginWin, text="   Login ", cursor="hand2", image = self.iconLoginResize, compound = LEFT, bg="#313030", fg="white", font=("time new roman", 13, "bold"), width=120, command=self.login_fun)
                Login_btn.place(x=287, y=583)

                #Bind function
                Login_btn.bind('<Enter>', on_enter)
                Login_btn.bind('<Leave>', on_leave)

                # bind function for show message.
                tip.bind_widget(Login_btn,balloonmsg='''Login Button For Login.''')

                def close1():
                    if messagebox.askokcancel("Login quit status", "Do you want to quit ?"):
                        loginWin.destroy()

                # Creating a photoimage object to use icon.
                self.iconExit = PhotoImage(file = r"icons/exit.png")
  
                # Resizing icon.
                self.iconExitResize = self.iconExit.subsample(6, 6)

                #Define functions
                def on_enter(e):
                    exitBtn.config(background='#357EC7', foreground= "white")

                def on_leave(e):
                    exitBtn.config(background= '#313030', foreground= 'white')

                # Exit Button
                exitBtn = Button(loginWin, text="   Exit ", image = self.iconExitResize, compound = LEFT, bg="#232222", fg="white", font=("time new roman", 10, "bold"), width=100, command=close1)
                exitBtn.place(x=1300, y=800)

                #Bind function
                exitBtn.bind('<Enter>', on_enter)
                exitBtn.bind('<Leave>', on_leave)

                # bind function for show message.
                tip.bind_widget(exitBtn,balloonmsg='''Exit program.''')

# =================================================================================== #
# =========================== Create Account Window ================================= #
# =================================================================================== #
            def createAccount(self):

                self.accWin = Tk()

                # Define window size (window size full screen).
                self.accWin.geometry("650x250")
                self.accWin.attributes('-fullscreen', True)
               
                # Background Color
                self.accWin.configure(bg='black')

                # Tittle set (tittle image steganography).
                self.accWin.title("Image Steganography")

                # Background imge (Image name acc.png which use account screen).
                self.bgAccount = ImageTk.PhotoImage(file="icons/acc.png",master=self.accWin)

                # Define label for show image (acc.png).
                labelBackGroundImg = Label( self.accWin, image = self.bgAccount, bd=0, bg="black")
                labelBackGroundImg.place(x=0,y=315)

                # Image steganography icon (icon binary2.png which use account window).
                self.imgSteganoIcon = PhotoImage(file = 'icons/binary2.png',master=self.accWin)
  
                # Setting icon (account window).
                self.accWin.iconphoto(False, self.imgSteganoIcon)

                # Creating a photoimage object to use icon (binary2.png account window).
                self.imgSteganoIcon = PhotoImage(file = r"icons/binary2.png",master=self.accWin)

                # Resizing icon size (binary2.png).
                self.imgStegIconResizing = self.imgSteganoIcon.subsample(18, 18)

                # Label (Image Sterganography).
                labelmgSteg = Label(self.accWin, text= " Image Steganography ", image = self.imgStegIconResizing, compound = LEFT, font=('Times New Roman bold',12), bg="black", fg="white")
                labelmgSteg.place(x = 615, y = 70) 

                # Creating a photoimage object to use icon (accoun1.png which use account window).
                self.accountIcon = PhotoImage(file = r"icons/accoun1.png",master=self.accWin)
                
                # Resizing icon size (accoun1.png).
                self.accIconResizing = self.accountIcon.subsample(10, 10)

                # Label Creat Account.
                labelAccount = Label(self.accWin, text= " Creat Account ", image = self.accIconResizing, compound = LEFT, font=('Times New Roman bold',25), bg="black", fg="white")
                labelAccount.place(x = 550, y = 20) 


                # Define frame (account window).
                self.frameAccount = Frame(self.accWin, bg="#313030", bd=0, highlightthickness=2)
                self.frameAccount.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                self.frameAccount.place(x=450, y=110, width=500, height=650)

                # Function use for remove temparary text in user name field (when click in user name field).
                def userName(e):
                    u_name.delete(0,"end")

                # Function use for remove temparary text in user password field (when click in user password field).
                def userPass(e):
                    u_pass.delete(0,"end")

                # Function use for remove temparary text in user age field (when click in user age field).
                def userAge(e):
                    u_age.delete(0, "end")

                # Function use for remove temparary text in user gender field (when click in user gender field).
                def userGender(e):
                    u_gender.delete(0, "end")

                # Function use for remove temparary text in user email field (when click in user email field).
                def userEmail(e):
                    u_email.delete(0, "end")

                # Function use for remove temparary text in user phone number field (when click in user phone number field).
                def userPhone(e):
                    u_phone.delete(0, "end")

                # Function use for remove temparary text in user address field (when click in user addresss field).
                def userAddress(e):
                    u_address.delete(0, "end")

                # Function use for remove temparary text in user street no field (when click in user street no field).
                def userStreetNo(e):
                    u_addressStreet.delete(0, "end")

                # Function use for remove temparary text in user city field (when click in user city field).
                def userCity(e):
                    u_city.delete(0, "end")

                # Function use for remove temparary text in region field (when click in region field).
                def userRegion(e):
                    u_region.delete(0, "end")

                # Function use for remove temparary text in user zip code field (when click in user zip code field).
                def userZipCode(e):
                    u_zipcode.delete(0, "end")

                # Function use for remove temparary text in user country field (when click in user country field).
                def userCountry(e):
                    u_country.delete(0, "end")
                
                # Function use for remove temparary text in user Id field (when click in user Id field).
                def userId(e):
                    u_id.delete(0, "end")

                # Clear data From field.
                def clearFieldData():
                    u_name.delete(0, END)
                    u_pass.delete(0, END)
                    u_age.delete(0, END)
                    u_gender.delete(0, END)
                    u_email.delete(0, END)
                    u_phone.delete(0, END)
                    u_address.delete(0, END)
                    u_addressStreet.delete(0, END)
                    u_city.delete(0, END)
                    u_region.delete(0, END)
                    u_zipcode.delete(0, END)
                    u_country.delete(0, END)
                    u_id.delete(0, END)
                    u_name.insert(0, " Enter your name")
                    u_pass.insert(0, " Enter password")
                    u_age.insert(0, " Enter your age")
                    u_gender.insert(0, " Enter your gender")
                    u_email.insert(0, " Enter your email (xyz@gmail.com)")
                    u_phone.insert(0, " Enter your phone number")
                    u_address.insert(0, " Enter your address")
                    u_addressStreet.insert(0, " Enter your street no")
                    u_city.insert(0, " Enter your city name??")
                    u_region.insert(0, " Your region ??")
                    u_zipcode.insert(0, " Your postal code ??")
                    u_country.insert(0, " Your country ??")
                    u_id.insert(0, " Auto user ID ")

                # Function create account button.
                def createAccBtn():
                
                    # Global veriable and genrate random user id, get values fron entry field.
                    user_name = u_name.get()
                    user_password = u_pass.get()
                    user_age = u_age.get()
                    user_gender = u_gender.get()
                    user_email = u_email.get()
                    user_phone = u_phone.get()
                    user_address = u_address.get()
                    user_streetno = u_addressStreet.get()
                    user_city = u_city.get()
                    user_region = u_region.get()
                    user_zipcode = u_zipcode.get()
                    user_country = u_country.get()
                    user_id = u_id.get()

                    # Check condition all entry field.
                    if user_name == " Enter your name" and user_password == " Enter password" and user_age == " Enter your age" and user_gender == " Enter your gender" and user_email == " Enter your email (xyz@gmail.com)" and user_phone == " Enter your phone number" and user_address == " Enter your address" and user_streetno == " Enter your street no" and user_city == " Enter your city name??" and user_region == " Your region ??" and user_zipcode == " Your postal code ??" and user_country == " Your country ??" and user_id == " Auto user ID ":
                        messagebox.showerror("Entry Field Status", "All field are required", parent= self.accWin)

                    elif(user_name == " Enter your name"):
                        messagebox.showerror("Name Field Status", "Name field are required", parent= self.accWin)
                    
                    elif(user_password == " Enter password"):
                        messagebox.showerror("Password Field Status", "Password field are required", parent= self.accWin)
                    
                    elif(user_email == " Enter your email (xyz@gmail.com)"):
                        messagebox.showerror("Email Field Status", "Email field are required", parent= self.accWin)
                    
                    elif(user_phone == " Enter your phone number"):
                        messagebox.showerror("Phone Number Field Status", "Phone Number field are required", parent= self.accWin)
                    
                    elif(user_gender == " Enter your gender"):
                        messagebox.showerror("Gender Field Status", "Gender field are required", parent= self.accWin)
                    
                    elif(user_age == " Enter your age"):
                        messagebox.showerror("Age Field Status", "Age field are required", parent= self.accWin)

                    elif(user_address == " Enter your address"):
                        messagebox.showerror("Address Field Status", "Address field are required", parent= self.accWin)

                    elif(user_streetno == " Enter your street no"):
                        messagebox.showerror("Street No Field Status", "Street No field are required", parent= self.accWin)

                    elif(user_city == " Enter your city name??"):
                        messagebox.showerror("City Field Status", "City field are required", parent= self.accWin)

                    elif(user_region == " Your region ??"):
                        messagebox.showerror("Region Field Status", "Region field are required", parent= self.accWin)

                    elif(user_zipcode == " Your postal code ??"):
                        messagebox.showerror("Zip code Field Status", "Zip code field are required", parent= self.accWin)

                    elif(user_country == " Your country ??"):
                        messagebox.showerror("Country Field Status", "Country field are required", parent= self.accWin)

                    else:

                        # Apply Exception for throw error.
                        try:

                            con = pymysql.connect(host="localhost", user="root", password="", database="imgstegregistrationaccount")
                            cur = con.cursor()
                            cur.execute("select * from imgestegregistrationusersrecords where user_email=%s", user_email)
                            row = cur.fetchone()
                            print("roe "+str(row))
                            if row != None: 
                                messagebox.showinfo("Data Base Status", "This record already exist please try again.", parent= self.accWin)
                            else:

                                global userId
                                randomUserId = random.randint(0,10000)
                                userId = str(randomUserId)
                                u_id.delete(0,"end")
                                u_id.insert(0, userId)
                                cur.execute("insert into imgestegregistrationusersrecords values('"+ user_name +"', '"+ user_password +"', '"+ userId+ "', '"+ user_age +"', '"+  user_gender +"', '"+ user_email +"', '"+ user_phone +"', '"+ user_address +"', '"+ user_streetno +"', '"+ user_city +"', '"+ user_region +"', '"+ user_zipcode +"', '"+ user_country +"')")
                                cur.execute("commit") 
                                messagebox.showinfo("insert data status", "Your record Successfully inserted", parent= self.accWin)
                                clearFieldData()
                                con.close()

                        except Exception as e:
                            messagebox.showerror("Data Base Status", str(e)+ str(" [ Data not inserted check error and please try again."), parent= self.accWin)
                            print(e)

                # Use tip tool ( Display message when hovering over something with mouse cursor ).
                tip= Balloon(self.accWin)
                
                # Label create account here and image steganography account form
                Label(self.frameAccount,text="Create Account Here",font=("Impact",20,"bold"), fg="white", bg="#313030").place(x=120,y=15)
                Label(self.frameAccount,text="Image Steganography Account Form",font=("Goudy old style",13,"bold"), fg="white", bg="#313030").place(x=125,y=51)
                # User name icon.
                self.userNameIcon = PhotoImage(file='icons/name13.png', master=self.accWin)
                self.labelUserNameIcon = Label(self.frameAccount , image = self.userNameIcon, bd=0, bg="#313030")
                self.labelUserNameIcon.place(x = 60, y = 92)

                # User name entry field (for input user name)
                u_name = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_name.insert(0, " Enter your name")

                # highlightbackground and highlightcolor for the border color (Entry field).
                u_name.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_name.place(x=115, y=101, width=300, height=28)
                u_name.bind("<FocusIn>", userName)

                # Bind the tooltip with user name entry field.
                tip.bind_widget(u_name,balloonmsg='''Enter user name for save record''')

                # User password icon.
                self.userPasswordIcon = PhotoImage(file='icons/key21.png', master=self.accWin)
                self.labelUserPasswordIcon = Label(self.frameAccount , image = self.userPasswordIcon, bd=0, bg="#313030")
                self.labelUserPasswordIcon.place(x = 65, y = 150)

                # User password entry field (input user password (frame)).
                u_pass = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", show='*', highlightthickness=2)
                u_pass.insert(0, " Enter password")

                # highlightbackground and highlightcolor for the border color
                u_pass.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_pass.place(x=115, y=155, width=300, height=28)
                u_pass.bind("<FocusIn>", userPass)
                # checkBox button.
                tip.bind_widget(self.u_pass,balloonmsg='''Enter password 
                Click check box button for show information''')

                check=IntVar(self.accWin)
                def showPassCreAcc():
                    if(check.get()==1):
                        u_pass.config(show='')
                    else:
                        u_pass.config(show='*')

                checkBoxBtn = Checkbutton(self.frameAccount,variable=check,onvalue=1,offvalue=0,command=showPassCreAcc, bg="#313030", cursor="hand2")
                checkBoxBtn.place(x=420, y=157)

                #Bind the tooltip.
                tip.bind_widget(checkBoxBtn,balloonmsg='''Show user password and information about user password field ''') 

                # User email icon.
                self.userEmailIcon = PhotoImage(file='icons/email.png', master=self.accWin)
                self.labelUserEmailIcon = Label(self.frameAccount , image = self.userEmailIcon, bd=0, bg="#313030")
                self.labelUserEmailIcon.place(x = 65, y = 200)

                # Email entry field (for input user email).
                u_email = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_email.insert(0, " Enter your email (xyz@gmail.com)")

                # highlightbackground and highlightcolor for the border color.
                u_email.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_email.place(x=115, y=200, width=300, height=28)
                u_email.bind("<FocusIn>", userEmail)

                # Bind the tooltip.
                tip.bind_widget(u_email,balloonmsg='''Enter your email for your record and inform.''')

                # User phone icon.
                self.userPhoneIcon = PhotoImage(file='icons/phone.png', master=self.accWin)
                self.labelUserPhoneIcon = Label(self.frameAccount , image = self.userPhoneIcon, bd=0, bg="#313030")
                self.labelUserPhoneIcon.place(x = 65, y = 250)

                # Phone entry field (for user input phone number)
                u_phone = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_phone.insert(0, " Enter your phone number")

                # highlightbackground and highlightcolor for the border color
                u_phone.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_phone.place(x=115, y=250, width=300, height=28)
                u_phone.bind("<FocusIn>", userPhone)

                #Bind the tooltip with button
                tip.bind_widget(u_phone,balloonmsg='''Enter user phone number for record.''')

                # User gender icon.
                self.userGenderIcon = PhotoImage(file='icons/gender.png', master=self.accWin)
                self.labelUserGenderIcon = Label(self.frameAccount , image = self.userGenderIcon, bd=0, bg="#313030")
                self.labelUserGenderIcon.place(x = 65, y = 300)

                # Gender entry field (For input user gender).
                u_gender = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_gender.insert(0, " Enter your gender")

                # highlightbackground and highlightcolor for the border color.
                u_gender.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_gender.place(x=115, y=300, width=130, height=28)
                u_gender.bind("<FocusIn>", userGender)

                #Bind the tooltip.
                tip.bind_widget(u_gender,balloonmsg='''Enter your gender which gender (Male/Female)''')

                # User age icon.
                self.userAgeIcon = PhotoImage(file='icons/age.png', master=self.accWin)
                self.labelUserAgeIcon = Label(self.frameAccount , image = self.userAgeIcon, bd=0, bg="#313030")
                self.labelUserAgeIcon.place(x = 255, y = 295)
             
                # User age field (input user age).
                u_age = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_age.insert(0, " Enter your age")

                # highlightbackground and highlightcolor for the border color.
                u_age.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_age.place(x=295, y=300, width=122, height=28)
                u_age.bind("<FocusIn>", userAge)

                #Bind the tooltip.
                tip.bind_widget(u_age,balloonmsg='''How much you old ??. ''')

                # User Address icon.
                self.userAddressIcon = PhotoImage(file='icons/address.png', master=self.accWin)
                # Resizing image to fit on button
                self.Resize_userAddressIcon = self.userAddressIcon.subsample(2, 2)
                self.labelUserAddressIcon = Label(self.frameAccount , image = self.Resize_userAddressIcon, bd=0, bg="#313030")
                self.labelUserAddressIcon.place(x = 65, y = 350)
             
                # Address entry field (for user input).
                u_address = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_address.insert(0, " Enter your address")

                # highlightbackground and highlightcolor for the border color
                u_address.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_address.place(x=115, y=350, width=300, height=28)
                u_address.bind("<FocusIn>", userAddress)

                #Bind the tooltip.
                tip.bind_widget(u_address,balloonmsg='''Enter your address for record.''')

                # User streetno icon.
                self.userStreetNoIcon = PhotoImage(file='icons/addressStreet.png', master=self.accWin)
                # Resizing image to fit on button
                self.Resize_userStreetNoIcon = self.userStreetNoIcon.subsample(2, 2)
                self.labelUserStreetNoIcon = Label(self.frameAccount , image = self.Resize_userStreetNoIcon, bd=0, bg="#313030")
                self.labelUserStreetNoIcon.place(x = 65, y = 400)

                # Street no entry field (for user input street no.).
                u_addressStreet = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_addressStreet.insert(0, " Enter your street no")

                # highlightbackground and highlightcolor for the border color
                u_addressStreet.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_addressStreet.place(x=115, y=400, width=300, height=28)
                u_addressStreet.bind("<FocusIn>", userStreetNo)

                #Bind the tooltip.
                tip.bind_widget(u_addressStreet,balloonmsg='''Enter your street nunber for record.''')
                # User city icon.
                self.userCityIcon = PhotoImage(file='icons/city.png', master=self.accWin)
                # Resizing image to fit on button
                self.Resize_userCityIcon = self.userCityIcon.subsample(25, 25)
                self.labelUserCityIcon = Label(self.frameAccount , image = self.Resize_userCityIcon, bd=0, bg="#313030")
                self.labelUserCityIcon.place(x = 65, y = 445)

                # City enty field (for input user city name).
                u_city = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_city.insert(0, " Enter your city name??")

                # highlightbackground and highlightcolor for the border color
                u_city.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_city.place(x=115, y=450, width=150, height=28)
                u_city.bind("<FocusIn>", userCity)

                #Bind the tooltip.
                tip.bind_widget(u_city,balloonmsg='''Enter your city name (which county ??).''')

                # User region icon.
                self.userRegionIcon = PhotoImage(file='icons/region.png', master=self.accWin)
                self.labelUserRegionIcon = Label(self.frameAccount , image = self.userRegionIcon, bd=0, bg="#313030")
                self.labelUserRegionIcon.place(x = 275, y = 450)
    
                # rgion entry field (for user input region).
                u_region = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_region.insert(0, " Your region ?")

                # highlightbackground and highlightcolor for the border color.
                u_region.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_region.place(x=315, y=450, width=100, height=28)
                u_region.bind("<FocusIn>", userRegion)

                #Bind the tooltip.
                tip.bind_widget(u_region,balloonmsg='''Enter your region Which region for record.''')

                # User region icon.
                self.userZipCodeIcon = PhotoImage(file='icons/zipcode.png', master=self.accWin)
                # Resizing image to fit on button
                self.Resize_userZipCodeIcon = self.userZipCodeIcon.subsample(2, 2)
                self.labelUserZipCodeIcon = Label(self.frameAccount , image = self.Resize_userZipCodeIcon, bd=0, bg="#313030")
                self.labelUserZipCodeIcon.place(x = 65, y = 498)

                # Zip code entry field (for input user zoi code).
                u_zipcode = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_zipcode.insert(0, " Your postal code ??")

                # highlightbackground and highlightcolor for the border color.
                u_zipcode.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_zipcode.place(x=115, y=500, width=150, height=28)
                u_zipcode.bind("<FocusIn>", userZipCode)

                #Bind the tooltip.
                tip.bind_widget(u_zipcode,balloonmsg='''Enter your postal code (your city zip code).''')

                # User country icon.
                self.userCountryIcon = PhotoImage(file='icons/country.png', master=self.accWin)
                # Resizing image to fit on button
                self.Resize_userCountryIcon = self.userCountryIcon.subsample(2, 2)
                self.labelUserCountryIcon = Label(self.frameAccount , image = self.Resize_userCountryIcon, bd=0, bg="#313030")
                self.labelUserCountryIcon.place(x = 268, y = 500)

                # Country entry field (for input user country name). 
                u_country = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", highlightthickness=2)
                u_country.insert(0, " Your country ??")

                # highlightbackground and highlightcolor for the border color
                u_country.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_country.place(x=312, y=500, width=103, height=28)
                u_country.bind("<FocusIn>", userCountry)

                #Bind the tooltip.
                tip.bind_widget(u_country,balloonmsg='''Enter your country name.''')

                # User id icon.
                self.userIdcon = PhotoImage(file='icons/id5.png', master=self.accWin)
                # Resizing image to fit on button
                self.Resize_userIdcon = self.userIdcon.subsample(15, 15)
                self.labelUserIdcon = Label(self.frameAccount , image = self.Resize_userIdcon, bd=0, bg="#313030")
                self.labelUserIdcon.place(x = 65, y = 545)

                # User id entry field (auto genrate user registration user id).
                u_id = Entry(self.frameAccount, font=("arial", 10, "bold"), bg="lightgray", fg="black", highlightthickness=2)
                u_id.insert(0, " Auto user ID ")

                # highlightbackground and highlightcolor for the border color.
                u_id.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                u_id.place(x=115, y=545, width=90, height=28)
                u_id.bind("<FocusIn>", userId)

                #Bind the tooltip.
                tip.bind_widget(u_id,balloonmsg='''Show user ID which important for login wihtout registration id not login''')

                

                # Creating a photoimage object to use image.
                self.iconRegBtn = PhotoImage(file = r"icons/accoun2.png", master=self.accWin)
                
                # Resizing image to fit on button
                self.Resize_regisbtnicon = self.iconRegBtn.subsample(20, 20)

                #Define functions.
                def on_enter(e):
                    regsBtn.config(background='#87CEFA', foreground= "white")

                def on_leave(e):
                    regsBtn.config(background= '#313030', foreground= 'white')

                regsBtn = Button(self.frameAccount, text=" Create Account ", cursor="hand2", image = self.Resize_regisbtnicon, compound = LEFT, font=("arial", 13, "bold"),width=160, bg="#313030", fg="white", command=createAccBtn)
                regsBtn.place(x=180,y=600)

                #Bind function
                regsBtn.bind('<Enter>', on_enter)
                regsBtn.bind('<Leave>', on_leave)

                #Bind the tooltip with button.
                tip.bind_widget(regsBtn,balloonmsg='''Button for create account''')

                # Back button function.
                def back():
                    self.accWin.destroy()
                    
                # Creating a photoimage object to use image
                EncrptBackBtnIcon = PhotoImage(file = r"icons/back1.png", master=self.accWin)
                
                # Resizing image to fit on button
                EncrptBackIcon = EncrptBackBtnIcon.subsample(1, 1)

                #Define functions change color of button
                def on_enter(e):
                    baBtn.config(background='#87CEFA', foreground= "white")

                def on_leave(e):
                    baBtn.config(background= '#313030', foreground= 'white')

                # Back Button
                baBtn = Button(self.accWin, text=" Back", image = EncrptBackIcon, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=back)
                baBtn.place(x=1300,y=800)

                #Bind the Enter 
                baBtn.bind('<Enter>', on_enter)
                baBtn.bind('<Leave>', on_leave)

                tip.bind_widget(baBtn,balloonmsg='''Button For Go Previous Page''')

                # # Close button function (Close account window).
                # def on_close():
                #     if messagebox.askokcancel("Quit Window", "Do you want to quit?", parent= self.accWin):
                #         self.accWin.destroy()
                #         self.loginWin.destroy()

                # Exit button icon (exit.png).
                # self.iconExitBtn = PhotoImage(file = r"icons/exit.png", master=self.accWin)
                
                # # Resizing image to fit on button.
                # self.resize_iconExBtn = self.iconExitBtn.subsample(6, 6)

                # #Define functions show color when cursor on button.
                # def on_enter(e):
                #     ExitBtn.config(background='#87CEFA', foreground= "white")

                # def on_leave(e):
                #     ExitBtn.config(background= '#313030', foreground= 'white')
                
                # # Button Exit.
                # ExitBtn = Button(self.accWin, text="   Exit", font=("arial", 13, "bold"), image = self.resize_iconExBtn, compound = LEFT, command=on_close, bg="#313030", width=120, fg="white")
                # ExitBtn.place(x=1300,y=800)

                # #Bind function.
                # ExitBtn.bind('<Enter>', on_enter)
                # ExitBtn.bind('<Leave>', on_leave)

                # #Bind the tooltip.
                # tip.bind_widget(ExitBtn,balloonmsg='''Button For Exit Window ''')
                # self.accWin.protocol("WM_DELETE_WINDOW", on_close)

                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master = self.accWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    self.accWin.state(newstate='iconic')
                    self.loginWin.state(newstate='iconic')

                minimizeBtn = Button(self.accWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=self.accWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=self.accWin)
                    
                # Button minimize
                minimizeBtn = Button(self.accWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')
                
                # Create account window main loop.
                self.accWin.mainloop()

# =================================================================================== #
# ========================= Forget Password Window ================================== #
# =================================================================================== #

            def forGetPass(self):
# ====  Creat window ,size, tittle, window logo, background color ================== 
                userForgetPassWin = Tk()
                userForgetPassWin.geometry("650x250")
                userForgetPassWin.attributes('-fullscreen', True)
                userForgetPassWin.title('Forgot Password')
                userForgetPassWin.iconbitmap('icons\\aa.ico')
                userForgetPassWin.configure(background='black')
                userForgetPassWin.resizable(0, 0)

                # Use tip tool ( Display message when hovering over something with mouse cursor ).
                tip= Balloon(userForgetPassWin)

                # Creating a photoimage object to use image
                iconMinizeBtn = PhotoImage(file = r"icons/min.png", master = userForgetPassWin)
                
                # Resizing image to fit on button
                resizeIconMinizeBtn = iconMinizeBtn.subsample(1, 1)

                # window minimize function.
                def minimizeWin(): 
                    #make the window minimize 
                    userForgetPassWin.state(newstate='iconic')
                    self.loginWin.state(newstate='iconic')

                minimizeBtn = Button(userForgetPassWin, image = resizeIconMinizeBtn, compound = LEFT, bg="black", bd=0, command=minimizeWin)
                minimizeBtn.place(x=1400,y=50)
                tip.bind_widget(minimizeBtn,balloonmsg='''Minimize Window''')

                # Creating a photoimage object to use image
                iconRestoreDownBtn = PhotoImage(file = r"icons/restoredown.png", master=userForgetPassWin)
                
                # Resizing image to fit on button
                resizeIconRestoreDownBtn = iconRestoreDownBtn.subsample(20, 20)

                # window RestoreDown function.
                def RestoreDown(): 
                    #make the window Restore Down.
                    messagebox.showerror("encode Window Status", "Window cann't resize", master=userForgetPassWin)
                    
                # Button minimize
                minimizeBtn = Button(userForgetPassWin, image = resizeIconRestoreDownBtn, compound = LEFT, bg="black", bd=0, command=RestoreDown)
                minimizeBtn.place(x=1355,y=54)
                tip.bind_widget(minimizeBtn,balloonmsg='''Restore down Window''')

                # ======= Forget Password icon and label ============

                # Creating a photoimage object to use icon (resetpass.png which use account window).
                forgetPassIcon = PhotoImage(file = r"icons/resetpass.png", master=userForgetPassWin)
                
                # Resizing icon size (accoun1.png).
                forgetPassIconResizing = forgetPassIcon.subsample(10, 10)

                # Label Creat Account.
                labelAccount = Label(userForgetPassWin, text= " Forget Password ", image = forgetPassIconResizing, compound = LEFT, font=('Times New Roman bold',25), bg="black", fg="white")
                labelAccount.place(x = 550, y = 80) 

                # ======= Back ground image label  ============

                # Background imge (Image name acc.png which use account screen).
                bgForgetPass = ImageTk.PhotoImage(file="images/password.png", master=userForgetPassWin)

                # Define label for show image (acc.png).
                labelBackGroundImg = Label( userForgetPassWin, image = bgForgetPass, bd=0, bg="black")
                labelBackGroundImg.place(x=0,y=315)

                # ======= Forget Password Button ans Exit Button Funtion  ============

                # Forget Password button function.
                def forgetPass():

                    # Create variables to access entry veriables.
                    userEmail = user_email_field.get()
                    userNewPassword = new_password_user.get()
                    confirmUserPassord = confirm_password_user.get()
                    userIdEntryField = user_id_Entry.get()
                    newpasslen = int(len(userNewPassword))
                    conpasslen = int((confirmUserPassord))
                    print(userNewPassword.isspace())

                    # ======= Entry Fields Check  ============

                    # Apply restriction onditions to check entry field.
                    if userEmail == "" and userNewPassword == "" and confirmUserPassord == "":
                        messagebox.showerror("Forget Password Status", "All fields are required.", master=userForgetPassWin)

                    elif userEmail =="" and userNewPassword == "":
                        messagebox.showerror("Forget Password Status", "User email and user new password fields are required.", master=userForgetPassWin)

                    elif userEmail =="" and confirmUserPassord == "":
                        messagebox.showerror("Forget Password Status", "User email and user confirm password fields are required.", master=userForgetPassWin)

                    elif confirmUserPassord =="" and userNewPassword == "":
                        messagebox.showerror("Forget Password Status", "User confirm password and user new password fields are required.", master=userForgetPassWin)     
                    
                    elif userNewPassword =="" and confirmUserPassord == "":
                        messagebox.showerror("Forget Password Status", "User new password and user confirm password fields are required.", master=userForgetPassWin)

                    elif userEmail =="":
                        messagebox.showerror("Forget Password Status", "User email fields are required.", master=userForgetPassWin)

                    elif userNewPassword =="":
                        messagebox.showerror("Forget Password Status", "New password fields are required.", master=userForgetPassWin)

                    elif confirmUserPassord =="":
                        messagebox.showerror("Forget Password Status", "User confirm Password fields are required.", master=userForgetPassWin)
                                  
                    elif userNewPassword =="":
                        messagebox.showerror("Forget Password Status", "user id field are required.", master=userForgetPassWin)

                    elif userNewPassword != confirmUserPassord:
                        messagebox.showerror("Forget Password Status", "New password and Confirm password not match.", master=userForgetPassWin)
                    
                    elif newpasslen < 6:
                        messagebox.showerror("Forget Password Status", "Password should be between 6 to 20 ", master=userForgetPassWin)
                    
                    else:

                        # ======= Exception and Database and Querys  ============

                        # Apply Exception for throw error.
                        try:
                            con = pymysql.connect(host="localhost", user="root", password="", database="imgstegregistrationaccount")                       
                        except Exception as e:
                            messagebox.showerror("Data Base Status", f"{str(e)}", master=userForgetPassWin)
                        cur = con.cursor()

                        cur.execute("select * from imgestegregistrationusersrecords where user_email=%s or userId=%s", (userEmail,userIdEntryField))
                        rows = cur.fetchone()
                    
                        if rows == None:
                            messagebox.showerror("Forget password status", "Invalid user email and confirm password please enter valid user email and confirm password.", master=userForgetPassWin)
                        elif rows[5] != userEmail:
                            messagebox.showerror("Forget password status", "Invalid user email please enter valid user email.", master=userForgetPassWin)
                        elif rows[2] != userIdEntryField:
                            messagebox.showerror("Forget password status", "Invalid user user id please enter valid user confirm password.", master=userForgetPassWin)
                      
                        if userEmail == rows[5] and userIdEntryField == rows[2]:
                            # access email and confirm password fron data base.
                            cur.execute("update imgestegregistrationusersrecords set user_password=%s where user_email=%s and userId=%s", (userNewPassword,userEmail,userIdEntryField))
                            cur.execute("commit") 
                            con.close()
                            messagebox.showinfo("Forget password status", "Successfully reset your login password, login with new password.  ", master=userForgetPassWin)

                # ======= Forget Password Frame  ============

                # Define forget password frame.
                forgetPassFrame = Frame(userForgetPassWin, highlightthickness=2, bg="#89898b")
                forgetPassFrame.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                forgetPassFrame.config(bg="black")
                forgetPassFrame.place(x=450, y=150, height=510, width=500)

                # ======= Forget Password Here Icon and Label  ============

                # Creating a photoimage object to use icon (resetpass1.png which use account window).
                forPassIcon = PhotoImage(file = r"icons/resetpass1.png", master=userForgetPassWin)
                
                # Resizing icon size (resetpass1.png).
                forPassIconResizing = forPassIcon.subsample(15, 15)

                # Label Creat Account.
                labelForgetPassword = Label(forgetPassFrame, text= "  Forget Password Here", image = forPassIconResizing, compound = LEFT, font=("Impact",20,"bold"), bg="black", fg="white")
                labelForgetPassword.place(x =100, y = 20)
                Label(forgetPassFrame,text="Image Steganography Forget Password Form",font=("Goudy old style",15,"bold"), fg="white", bg="black").place(x=40,y=70)

                # ====== Email Entry Field and Label ====================
                email_label = Label(forgetPassFrame, text='• Email account', fg="white", bg='black',font=("yu gothic ui", 11, 'bold'))
                email_label.place(x=100, y=130)
                user_email_field = Entry(forgetPassFrame, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
                user_email_field.config(highlightbackground = "#87CEEB", highlightcolor= "#87CEEB")
                user_email_field.place(x=100, y=160, width=300, height=34)

                # bind function for show message.
                tip.bind_widget(user_email_field,balloonmsg='''User enter register email. ''')

                # ====  New Password Entry Field and Label ==================
                new_password_label = Label(forgetPassFrame, text='• New Password', fg="white", bg='black', font=("yu gothic ui", 11, 'bold'))
                new_password_label.place(x=100, y=210)
                new_password_user = Entry(forgetPassFrame, fg="black", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                new_password_user.config(highlightbackground="#87CEEB", highlightcolor="#87CEEB")
                new_password_user.place(x=100, y=240, width=300, height=34)

                # bind function for show message.
                tip.bind_widget(new_password_user,balloonmsg='''user enter new password which user want''')

                # checkBox button.
                checkNewPAss=IntVar(userForgetPassWin)
                def showNewPass():
                    if(checkNewPAss.get()==1):
                        new_password_user.config(show='')
                    else:
                        new_password_user.config(show='*')

                checkBoxBtnNew = Checkbutton(forgetPassFrame,variable=checkNewPAss, onvalue=1,offvalue=0,command=showNewPass, bg="black", cursor="hand2")
                checkBoxBtnNew.place(x=410, y=245)

                #Bind the tooltip.
                tip.bind_widget(checkBoxBtnNew,balloonmsg='''Show user new password.''')  

                # ====  Confirm Password Entry Field and Label ================== #
                confirm_password_label = Label(forgetPassFrame, text='• Confirm Password', fg="white", bg='black',font=("yu gothic ui", 11, 'bold'))
                confirm_password_label.place(x=100, y=290)
                confirm_password_user = Entry(forgetPassFrame, fg="black", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                confirm_password_user.config(highlightbackground="#87CEEB", highlightcolor="#87CEEB")
                confirm_password_user.place(x=100, y=320, width=300, height=34)

                # bind function for show message.
                tip.bind_widget(confirm_password_user,balloonmsg='''user enter confirm password. Register password''')

                # checkBox button.
                checkConfirmPass=IntVar(userForgetPassWin)
                def showConfirmPass():
                    if(checkConfirmPass.get()==1):
                        confirm_password_user.config(show='')
                    else:
                        confirm_password_user.config(show='*')

                checkBoxBtnConfirm = Checkbutton(forgetPassFrame,variable=checkConfirmPass, onvalue=1,offvalue=0,command=showConfirmPass, bg="black", cursor="hand2")
                checkBoxBtnConfirm.place(x=410, y=325)

                #Bind the tooltip.
                tip.bind_widget(checkBoxBtnConfirm,balloonmsg='''Show user confirm password.''') 

                # ====  User id Entry Field and Label ================== #
                user_id_label = Label(forgetPassFrame, text='• User Id', fg="white", bg='black',font=("yu gothic ui", 11, 'bold'))
                user_id_label.place(x=100, y=365)
                user_id_Entry = Entry(forgetPassFrame, fg="black", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                user_id_Entry.config(highlightbackground="#87CEEB", highlightcolor="#87CEEB")
                user_id_Entry.place(x=100, y=400, width=120, height=34)

                # bind function for show message.
                tip.bind_widget(user_id_Entry,balloonmsg='''user enter confirm password. Register password''')

                # checkBox button.
                checkConfirmPass1=IntVar(userForgetPassWin)
                def showConfirmPass1():
                    if(checkConfirmPass1.get()==1):
                        user_id_Entry.config(show='')
                    else:
                        user_id_Entry.config(show='*')

                checkBoxBtnConfirm1 = Checkbutton(forgetPassFrame,variable=checkConfirmPass1, onvalue=1,offvalue=0,command=showConfirmPass1, bg="black", cursor="hand2")
                checkBoxBtnConfirm1.place(x=230, y=405)

                #Bind the tooltip.
                tip.bind_widget(checkBoxBtnConfirm1,balloonmsg='''Show user confirm password.''')


                # ======= Update Password Button, Icon Button and Change Color Function ============ #

                # Exit button icon (exit.png).
                iconForgetPass = PhotoImage(file = r"icons/respass.png", master=userForgetPassWin)
                
                # Resizing image to fit on button.
                iconForgetPassResize = iconForgetPass.subsample(20, 20)

                #Define functions
                def on_enter(e):
                    updatePassBtn.config(background='#87CEFA', foreground= "white")

                def on_leave(e):
                    updatePassBtn.config(background= '#1b87d2', foreground= 'white')

                updatePassBtn = Button(userForgetPassWin, fg='black', text=' Update Password', image = iconForgetPassResize, compound = LEFT, bg='#1b87d2', font=("yu gothic ui bold", 14),cursor='hand2', command=forgetPass)
                updatePassBtn.place(x=582, y=635, width=256, height=50)

                #Bind function
                updatePassBtn.bind('<Enter>', on_enter)
                updatePassBtn.bind('<Leave>', on_leave)

                # bind function for show message.
                tip.bind_widget(updatePassBtn,balloonmsg='''Forget password button for reset password.''')


                # Back button function.
                def back():
                    userForgetPassWin.destroy()


                # Creating a photoimage object to use image
                EncrptBackBtnIcon = PhotoImage(file = r"icons/back1.png", master=userForgetPassWin)
                
                # Resizing image to fit on button
                EncrptBackIcon = EncrptBackBtnIcon.subsample(1, 1)

                #Define functions change color of button
                def on_enter(e):
                    baBtn.config(background='#87CEFA', foreground= "white")

                def on_leave(e):
                    baBtn.config(background= '#313030', foreground= 'white')

                # Back Button
                baBtn = Button(userForgetPassWin, text=" Back", image = EncrptBackIcon, compound = LEFT, bg="#232222", fg="white", 
                        font=("time new roman", 10, "bold"), width=120, command=back)
                baBtn.place(x=1300,y=800)

                #Bind the Enter 
                baBtn.bind('<Enter>', on_enter)
                baBtn.bind('<Leave>', on_leave)

                tip.bind_widget(baBtn,balloonmsg='''Button For Go Previous Page''')

                # # Close button function (Close account window).
                # def on_close():
                #     if messagebox.askokcancel("Quit Window", "Do you want to quit?", parent= userForgetPassWin):
                #         userForgetPassWin.destroy()
                #         self.loginWin.destroy()

                # # Exit button icon (exit.png).
                # self.iconExitBtn = PhotoImage(file = r"icons/exit.png", master=userForgetPassWin)
                
                # # Resizing image to fit on button.
                # self.resize_iconExBtn = self.iconExitBtn.subsample(6, 6)

                # #Define functions show color when cursor on button.
                # def on_enter(e):
                #     ExitBtn.config(background='#87CEFA', foreground= "white")

                # def on_leave(e):
                #     ExitBtn.config(background= '#313030', foreground= 'white')
                
                # # Button Exit.
                # ExitBtn = Button(userForgetPassWin, text="   Exit", font=("arial", 13, "bold"), image = self.resize_iconExBtn, compound = LEFT, command=on_close, bg="#313030", width=120, fg="white")
                # ExitBtn.place(x=1300,y=800)

                # #Bind function.
                # ExitBtn.bind('<Enter>', on_enter)
                # ExitBtn.bind('<Leave>', on_leave)

                # #Bind the tooltip.
                # tip.bind_widget(ExitBtn,balloonmsg='''Button For Exit Window ''')
                # userForgetPassWin.protocol("WM_DELETE_WINDOW", on_close)
                
                # Forget Password window main loop.
                userForgetPassWin.mainloop()

# ================================================================ #
# ========================== Login window code =================== #
# ================================================================ #

            # Class object (Self) access out of class all variables
            def login_fun(self):

                # Apply Exception for throw error.
                try:
                    # Declare veriables.
                    global userName
                    global userEmail
                    global userPass
                    global userId
                    # Get values from entry box.
                    self.user_email = self.u_email.get()
                    userEmail = self.user_email
                    self.user_password = self.u_pass.get()
                    userPass = self.user_password
                    self.userId = self.u_id.get()
                    userId =  self.userId
                    # Declare veriables.
                    check = IntVar()
                    check = 0
                    # Check conditions
                    if self.user_email=="" and self.user_password=="" and self.userId=="":
                        messagebox.showerror("All field status", "All fields are required.")
                        check = check+1

                    elif self.user_email=="" and self.user_password=="":
                        messagebox.showerror("Login status", "User email and password field required.")
                        check = check+1

                    elif self.user_email=="" and self.userId=="":
                        messagebox.showerror("Login status", "User email and user id field required.")
                        check = check+1
                    
                    elif self.user_password=="" and self.userId=="":
                        messagebox.showerror("Login status", "User password and user id field required.")
                        check = check+1

                    elif self.user_email=="":
                        messagebox.showerror("User name field status", "User email field required.")
                        check = check+1

                    elif self.user_password=="":
                        messagebox.showerror("User password field status", "User password required.")
                        check = check+1

                    elif self.userId=="":
                        messagebox.showerror("User id field status", "User id field required.")
                        check = check+1
                    # Database conncetor.
                    self.con = pymysql.connect(host="localhost", user="root", password="", database="imgstegregistrationaccount")
                    self.mycursor = self.con.cursor()
                    self.sql = "select * from imgestegregistrationusersrecords where user_email = %s and user_password = %s and userId = %s"
                    self.mycursor.execute(self.sql, [(self.user_email), (self.user_password), (self.userId)])
                    self.results = self.mycursor.fetchone()
                    rows = self.results
                    if(rows != None):
                        global name
                        userName = rows[0]
                        username = userName
                        name = username
                        # ///////////////////////////////////// 
                        # Apply Exception for throw error.
                        try:
                            # Create an instance of datetime module
                            # Create an instance of datetime module

                            # Create an instance of datetime module
                            # date=dt.datetime.now()
                            datetime1=dt.datetime.now()
                            # Format the date
                            format_date=f"{datetime1:%a, %b %d %Y}"
                            date = str(format_date)

                            time_string = strftime('%H:%M:%S %p')
                            time = str(time_string)
                            # datetime = str(datetime1)

                            con = pymysql.connect(host="localhost", user="root", password="", database="imgstegregistrationaccount")
                            cur = con.cursor()
                            
                            cur.execute("insert into userloginrecord values('"+ username +"', '"+ date +"', '"+ time +"')")
                            cur.execute("commit") 
                            con.close()

                        except Exception as e:
                            messagebox.showerror("Data Base Status", str(e)+ str(" [ Data not inserted check error and please try again."), parent= self.loginWin)
                            print(e)
                    if self.results:
                        self.loginWin.destroy()
                        welSplashWin()
                        
                    else:
                        # Database conncetor.
                        self.con = pymysql.connect(host="localhost", user="root", password="", database="imgstegregistrationaccount")
                        self.mycursor = self.con.cursor()
                        self.sql = "select * from imgestegregistrationusersrecords where user_email = %s or user_password = %s or userId = %s"
                        self.mycursor.execute(self.sql, [(self.user_email), (self.user_password), (self.userId)])
                        self.results = self.mycursor.fetchone()
                        rowsInvalid = self.results
                        if(check == 0):
                            # Check conditions.
                            if(rowsInvalid == None):
                                messagebox.showerror("Login Status", "Invalid user email, passwors and id please enter valid information")
                            elif(rowsInvalid[5] != self.u_email.get() and rowsInvalid[1] != self.u_pass.get()):
                                messagebox.showerror("Login Status", "Invalid user email and password please enter valid user email and password")
                            elif(rowsInvalid[5] != self.u_email.get() and rowsInvalid[2] != self.u_id.get()):
                                messagebox.showerror("Login Status", "Invalid user email and Id please enter valid user email and id")
                            elif(rowsInvalid[1] != self.u_pass.get() and rowsInvalid[2] != self.u_id.get()):
                                messagebox.showerror("Login Status", "Invalid user password and Id please enter valid user password and id")
                            elif(rowsInvalid[1] != self.u_pass.get()):
                                messagebox.showerror("Login Password Status", "Invalid user password please enter valid password")
                            elif(rowsInvalid[2] != self.u_id.get()):
                                messagebox.showerror("Login User Id Status", "Invalid user id please enter valid user id")
                            elif(rowsInvalid[5] != self.u_email.get()):
                                messagebox.showerror("Login User Email Status", "Invalid user email please enter valid user email")

                except Exception as e:
                    messagebox.showerror("Error Login Status", str(e))
        
        # Creae login window. 
        loginWin = Tk()

        # Create object Login class. 
        obj = Login(loginWin)
        loginWin.protocol("WM_DELETE_WINDOW", exit)
        loginWin.mainloop()

    # Set the Interval video animation window
    videoAnimationWin.after(14000,main)
    videoAnimationWin.mainloop()

# Splash window destory and open new window.
splashWin.destroy()
# =======================================#
#===== Call video animation function. ===#
#========================================#
# Call video animation function.
videoAnimationFun()
splashWin.mainloop()
