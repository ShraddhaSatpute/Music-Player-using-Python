import tkinter as tk
import fnmatch
import os
from pygame import mixer

# Initialize the main window
canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("1440x880")
canvas.config(bg='black')

# Set the background image path
background_image_path = r"C:\Users\shrad\Desktop\Music Player\Background.png"
background_image = tk.PhotoImage(file=background_image_path)
background_label = tk.Label(canvas, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the music files directory path
rootpath = r"C:\Users\shrad\Desktop\Music Player\Music Player Songs"
pattern = "*.mp3"

# Initialize the Pygame mixer
mixer.init()

def select():
    selected_song = listBox.get("anchor")
    if not selected_song:  # If nothing is selected
        return
    full_path = os.path.join(rootpath, selected_song)
    print(f"Loading song: {full_path}")  # Debugging line to check the path
    try:
        mixer.music.load(full_path)
        mixer.music.play()
        label.config(text=selected_song)
    except pygame.error as e:
        print(f"Error loading song: {e}")


def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    if not next_song:  # If no song is selected
        return
    next_song = next_song[0] + 1
    if next_song >= listBox.size():  # Check if it's the last song
        return
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(os.path.join(rootpath, next_song_name))
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    if not next_song:  # If no song is selected
        return
    next_song = next_song[0] - 1
    if next_song < 0:  # Check if it's the first song
        return
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(os.path.join(rootpath, next_song_name))
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

def set_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

# Create the Listbox to display songs
listBox = tk.Listbox(canvas, fg="black", bg="violet", width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('ds-digital', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

# Create buttons
prevButton = tk.Button(canvas, text="Prev", command=play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

# Create volume scale
volumeScale = tk.Scale(canvas, from_=0, to=100, orient='horizontal', command=set_volume, bg='black', fg='white', label='Volume')
volumeScale.pack(padx=15, pady=15)

# Load music files into the Listbox
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

# Start the main loop
canvas.mainloop()
