from tkinter import *

# Create a window 
window = Tk()

# Styles
from styles import *

# Set window UI
window.title("YouTube Video Downloader")    # Set Window Name
window.geometry("1000x450")                 # Set Window Size
window.resizable(False, False)              # Stop Resizing 
window.configure(bg=BKG_COLOR)              # Set bkg color

# Forms
from forms import *

# Set up the forms that were imported
SaveLocationForm(window)                                
YouTubeVideoForm(window)
DownloadForm(window)

if __name__ == "__main__":
    window.mainloop()
