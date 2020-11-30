# importing module 
import youtube_dl 
import os
from tkinter import *
from time import *

os.system('clear')

ydl_opts = {} 
  
def dwl_vid(zxt): 
    '''Video downloader'''
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        ydl.download([zxt]) 
  

def when_download_clicked():
    '''Function to get the link inserted and call the downloader'''
    try:
        link_of_the_video = text.get() #input("Copy & paste the URL of the YouTube video you want to download:- ")
        zxt = link_of_the_video.strip() 
        label.configure(text="Downloading...")
        sleep(5)
        dwl_vid(zxt)
        label.configure(text="Done")
        text.delete(0, END)
        sleep(2)
        label.configure(text ="Please enter the link below")
    except youtube_dl.utils.DownloadError as dwlErr:
        label.configure(text="There is an error with the link.")
        sleep(2)
        text.delete(0, END)
        label.configure(text ="Please enter the link below")

window = Tk() #set the gui window

window.geometry("380x200") #set the window size

window.title("YouTube Downloader")

label = Label(window, text ='Please enter the link below', font=("Calibri", 20)) #creating a label
label.grid(column=0, row=0) #set the label to the window canvas

text = Entry(window, width=20) #set block to accept text
text.grid(column=0,row=1) #set the text block to the canvas

button = Button(window, text="Download", bg="black", fg="white", command=when_download_clicked) #creating a button
button.grid(column=0, row=2) #setting the button to the canvas

window.mainloop() #main loop to keep window open



