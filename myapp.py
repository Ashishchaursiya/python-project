#import required library
from tkinter import *
import pafy
import tkinter.messagebox as tmsg
import webbrowser
root=Tk()
#mouse event handling
def my_info1(event):
    b1.config(bg='red',fg='white')
def my_info2(event):
    b2.config(bg='red',fg='white')
def my_info3(event):
    b3.config(bg='red',fg='white')
def my_infos1(event):
    b1.config(bg='green', fg='white')
def my_infos2(event):
    b2.config(bg='green', fg='white')
def my_infos3(event):
    b3.config(bg='green', fg='white')
def info():
    webbrowser.open("https://chaurasiyaashish38.wixsite.com/mysite-1")
    tmsg.showinfo('Warning', 'Internet connection should be Enabled')
def info4(event):
    b4.config(bg='red')
def infos4(event):
    b4.config(bg='blue')
#fuction for video information
def description():
    link=E1.get()
    video = pafy.new(link)
    Label(fr1, text='Title:-' + video.title, bg='green',fg='white',font=" times 10 bold").pack()
    Label(fr1, text='view:-' + str(video.viewcount), bg='green',fg='white',font=" times 10 bold").pack()
    Label(fr1, text='Duration:-' + str(video.duration), bg='green',fg='white',font=" times 10 bold").pack()
    Label(fr1, text='Likes:-' + str(video.likes), bg='green',fg='white',font=" times 10 bold").pack()
    Label(fr1, text='Dislikes:-' + str(video.dislikes), bg='green',fg='white',font=" times 10 bold").pack()
    tmsg.showinfo('Check It,If not working','Path should be like this,Example:-C:/Users/VKC/Desktop')
#fuction for to download video
def dounload():
    import pafy
    url = E1.get()
    path=E2.get()
    video = pafy.new(url)
    best = video.getbest()
    best.download(path)
    tmsg.showinfo('info', 'video will be save in given location')
#fuction for to download audio
def audio():
    import pafy
    url = E1.get()
    path=E2.get()
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download(path)
    tmsg.showinfo('Warning', 'This file is webm file. so open  any browser press ctrl + o select this file to play ')
#main layout design code
root.geometry('500x500')
root.title('YouTube Duwnloder')
Label(root,text='WELCOME TO YOUTUBE DOWNLODER',bg='red',fg='white',font=" times 20 bold").pack(fill=X)
root.iconbitmap(r'as.ico')
root.config(bg='#1e3c72')
l=Label(root,text='App Devloped by Ashish Chaursiya',font='40',bg='blue',fg='white')
l.pack(side='bottom',fill=X)
fr=Frame(root,bg='#a3bded')
fr.pack(side='top',fill=Y,pady=100)
fr1=Frame(root,bg='#ffc3a0')
fr1.pack(side='right',fill=Y)
l1=Label(fr,text='Paste Youtube Url ',bg='#708090',fg='white',font=" times 15 bold")
l1.pack(side='top')
E1=Entry(fr,bg='#f5f7fa',fg='black',width='30',font=" times 9 bold")
E1.pack()
E2=Entry(fr,bg='#f5f7fa',width='40',fg='black',font=" times 10 bold")
Label(fr,text='Paste Your Path Where You want to Save',bg='#708090',fg='white',font=" times 15 bold").pack(pady=5)
E2.pack()
b1=Button(fr,text='Show Video Info',bg='green',fg='white',command=description,font=" times 15 bold")
b1.pack(pady=10)
b2=Button(fr,text='Download Video',bg='green',fg='white',font=" times 15 bold",command=dounload)
b2.pack(pady=10)
b3=Button(fr,text='Download Audio',bg='green',fg='white',font=" times 15 bold",command=audio)
b3.pack(pady=10)
#mouse event handling
b1.bind("<Enter>",my_info1)
b2.bind("<Enter>",my_info2)
b3.bind("<Enter>",my_info3)
b1.bind("<Leave>",my_infos1)
b2.bind("<Leave>",my_infos2)
b3.bind("<Leave>",my_infos3)
#background image
photo=PhotoImage(file="ass.png")
ph_label=Label(root,image=photo)
ph_label.pack()
b4=Button(fr,text='Contact me',bg='blue',fg='white',font=" times 15 bold",command=info)
b4.pack(side='right')
b4.bind("<Enter>",info4)
b4.bind("<Leave>",infos4)
root.mainloop()