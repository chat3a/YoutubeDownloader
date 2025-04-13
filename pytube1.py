from pytubefix import YouTube
from pytubefix.cli import on_progress
from tkinter import filedialog
import tkinter as tk


def choose_resolution():
    global res
    res = "0"
    cho = int(input("選擇影片畫質 (請輸入1,2,3,4) -> "))
    print("\n1| 360p\n2| 720p\n3| 1080p\n4| 最高畫質")
    if cho == 1:
        res = "360"
    if cho == 2:
        res = "720"
    if cho == 3:
        res = "1080"
    if cho == 4:
        res = "144"
    return res

def choose_audio_or_video():
    print("\n影片格式:\n1| MP4\n2| MP3")
    while True:
        cho1 = int(input("選擇影片格式 -> "))
        if cho1 == 1:
            print("選擇存放位置 -> ")
            save_path = filedialog.askdirectory(title = "選擇影片存放路徑")
            print("> "+ save_path)
            print("\n下載中...")
            yt.streams.get_highest_resolution().download(filename=f"{yt.title}.mp4", output_path = save_path)
            print("\n下載完成!")
            break
        elif cho1 == 2:
            print("選擇存放位置 -> ")
            save_path = filedialog.askdirectory(title = "選擇影片存放路徑")
            print("> "+ save_path)
            print("\n下載中...")
            yt.streams.get_audio_only().download(filename=f"{yt.title}.mp4", output_path = save_path)
            print("\n下載完成!")
            break
        else:
            print("\n! 請輸入有效的字串或數字")
        

root = tk.Tk()
root.title("YEEEE")
root.withdraw()

while True:
    url = str(input("輸入Youtube網址 -> "))
    if url.startswith("https://www.youtube.com/"):
        yt = YouTube(url, on_progress_callback = on_progress)
        choose_audio_or_video()
        break
    else:
        print("\n! 請輸入有效路徑")

