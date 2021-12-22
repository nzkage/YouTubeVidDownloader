from tkinter import PhotoImage, ttk
from tkinter.font import *

# Global, Final Vars
BKG_COLOR = "#23272a" 
FG_COLOR = "#ffffff"
HIGHLIGHT_COLOR = "#7289da"

# Text Styles
title_style = Font(family="Lucida Grande", size=40)
label_style = Font(family="Lucida Grande", size=22)
entry_style = Font(family="Lucida Grande", size=20)

# Images
browse_btn = PhotoImage(file="./assets/browse_btn.png")
add_btn = PhotoImage(file="./assets/add_btn.png")
delete_btn = PhotoImage(file="./assets/delete_btn.png")
clear_list_btn = PhotoImage(file="./assets/clear_list_btn.png")
download_btn = PhotoImage(file="./assets/download_btn.png")