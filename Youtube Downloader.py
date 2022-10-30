from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import youtube_dl
import shutil

# This function will enable the user to select the path to where they want to save to downloaded file on their local machine.
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

# This function enables Python to convert a YouTube video into a MP4 file and download it onto your local machine.
def mp4():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)

def mp3():
    video_url = link_field.get()
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
YouTube_logo = PhotoImage(file='Logo.png')
#resize
YouTube_logo = YouTube_logo.subsample(2, 2)
canvas.create_image(250, 80, image=YouTube_logo)

#link field
link_field = Entry(screen, width=40, font=('Arial', 12) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 12))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 12))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
mp4_btn = Button(screen, text="Download File as mp4",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=mp4)
mp3_btn = Button(screen, text="Download File as mp3",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=mp3)
#add to canvas
canvas.create_window(250, 390, window=mp4_btn)
canvas.create_window(250, 440, window=mp3_btn)

screen.mainloop()