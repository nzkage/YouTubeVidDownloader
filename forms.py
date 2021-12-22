from tkinter import *
from tkinter import filedialog

from styles import *
from downloader import Downloader


class Singleton(type):
    """
    Acts as a metaclass to allow other classes to become Singleton classes
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SaveLocationForm(metaclass=Singleton):
    def __init__(self, window) -> None:
        self.file_entry_label = Label(
            window,
            text="Download Location",
            bg=BKG_COLOR,
            fg=FG_COLOR,
            font=label_style
        )

        self.file_entry = Entry(
            window,
            bg=BKG_COLOR,
            fg=FG_COLOR,
            font=entry_style,
            width=30
        )

        self.browse_btn = Button(
            window,
            image=browse_btn,
            command=self.browse_func,
            width=47,
            height=47,
            borderwidth=0,
            relief='flat',
            highlightthickness=0, 
            bd=0,
        )

        self.position()

    def position(self):
        self.file_entry_label.grid(row = 1, columnspan = 2, padx=(25, 0), pady=(30,10), sticky="W")
        self.file_entry.grid(row = 2, column = 0, padx=(25, 0), pady=0, sticky="W")
        self.browse_btn.grid(row = 2, column = 1, padx=(10, 0), pady=0, sticky="W")

    def browse_func(self):
        """
        Called on button press
        Popup to allow users to find a directory on their system 
        """
        self.file_entry.delete(0, END)
        filename = filedialog.askdirectory()
        self.file_entry.insert(END, filename) 

    def get_path(self):
        """
        Called in the DownloadForm
        Gets the path the user wants to save the videos in
        """
        return self.file_entry.get()


class YouTubeVideoForm(metaclass=Singleton):
    
    def __init__(self, window) -> None:
        self.video_link_label = Label(
            window,
            text="YouTube Video Link",
            bg=BKG_COLOR,
            fg=FG_COLOR,
            font=label_style
        )

        self.link_entry = Entry(
            window,
            bg=BKG_COLOR,
            fg=FG_COLOR,
            font= entry_style,
            width= 30
        )

        self.link_entry_btn = Button(
            window,
            image=add_btn,
            command=self.add_link,
            width=47,
            height=47,
            borderwidth=0,
            relief='flat',
            highlightthickness=0, 
            bd=0,
        )

        # Column 2
        self.video_list_label = Label(
            window,
            text="Selected Videos",
            bg=BKG_COLOR,
            fg=FG_COLOR,
            font=label_style
        )

        self.links_entry_delete_btn = Button(
            window,
            image=delete_btn,
            command=self.delete_link,
            width=47,
            height=47,
            borderwidth=0,
            relief='flat',
            highlightthickness=0, 
            bd=0,
        )

        self.links_list_clear_btn = Button(
            window,
            image=clear_list_btn,
            command=self.clear_list,
            width=47,
            height=47,
            borderwidth=0,
            relief='flat',
            highlightthickness=0, 
            bd=0,
        )

        self.links_list = Listbox(
            window,
            width=47,
            height=20,
            fg=BKG_COLOR,
            bg=FG_COLOR,
        )

        self.position()

    def position(self):
        self.video_link_label.grid(row=3, columnspan=2, padx=(25, 0), pady=(25,10), sticky="W")
        self.link_entry.grid(row=4, column=0, padx=(25,0), pady=0, sticky="W")
        self.link_entry_btn.grid(row=4, column=1, padx=(10,0), pady=0, sticky="W")

        # Column 2
        self.video_list_label.grid(row=1, column=3, padx=(60,0), pady=(25,10), sticky="W")
        self.links_entry_delete_btn.grid(row=1, column=4, pady=(25,10), sticky="E") 
        self.links_list_clear_btn.grid(row=1, column=5, pady=(25,10), sticky="E")
        self.links_list.grid(row=2, rowspan=10, column=3, columnspan=3, padx=(60,0), pady=(0,10), sticky="W")

    def add_link(self):
        """
        Called on button press
        Checks if Youtube Link and adds them to the ListBox
        """
        if "https://www.youtube.com/watch?v=" in self.link_entry.get():
            self.links_list.insert("end", self.link_entry.get())
            self.link_entry.delete(0, "end")
        else:
            # TODO - Add error popup to remind user to upload YOUTUBE LINKS
            pass

    def delete_link(self):
        """
        Called on button press
        Deletes the link the User has selected
        """
        self.links_list.delete(self.links_list.curselection()[0])

    def clear_list(self):
        """
        Called on button press
        Deletes the entire ListBox of YT Video Links 
        """
        self.links_list.delete(0, END)

    def get_list(self):
        """
        Called in DownloadForm
        Gets the entire ListBox of links (works bcs of Singleton)
        """
        return list(self.links_list.get(first=0, last=END))

    def remove_from_list(self, vid):
        """
        Called in DownloadForm
        Finds the first occurence of a link and removes it from the ListBox
        """
        idx = self.links_list.get(0, END).index(vid)
        self.links_list.delete(idx)


class DownloadForm(metaclass=Singleton):
    def __init__(self, window):
        self.format_label = Label(
            window,
            text="Format",
            bg=BKG_COLOR,
            fg=FG_COLOR,
            font=label_style
        )

        # For the dropdown
        self.vformat = StringVar(window)
        self.vformat.set("mp4")

        self.format_dropdown = OptionMenu(
            window,
            self.vformat, 
            "mp3",
            "mp4"
        )

        self.format_dropdown.config(font=entry_style)
        
        self.download_btn = Button(
            window,
            text = "Download!",
            command = self.download,
            image=download_btn,
            width=450,
            height=47,
            borderwidth=0,
            relief='flat',
            highlightthickness=0, 
            bd=0,
        )

        self.position()
    
    def position(self):
        self.format_label.grid(row=5, columnspan=2, padx=(25, 0), pady=(25,10), sticky="W")
        self.format_dropdown.grid(row=6, columnspan=2, padx=(25,0), pady=0, sticky="W")
        self.download_btn.grid(row=7, columnspan=2, padx=(25,0), pady=(20,0), sticky="W")
    
    def download(self):
        """
        REQUIRES:
        - video list from YouTubeVideoForm
        - path from SaveLocationForm
        
        Downloads all the videos in the ListBox in YoutubeVideoForm
        """
        video_list = YouTubeVideoForm().get_list()
        path = SaveLocationForm().get_path()

        if len(path) > 0 and len(video_list) > 0:
            for vid in video_list:
                if Downloader.download(path, vid, self.vformat.get()) == 1:
                    # Download Successful
                    YouTubeVideoForm().remove_from_list(vid)
                else:
                    # TODO - Display Errors
                    pass
        else:
            # TODO - Display Errors
            pass