import os
from pytube import YouTube


class Downloader:

    @staticmethod
    def download(path, link, vformat):
        """
        Called in DownloaderForm in forms.py
        Downloads YouTube Videos with a given format using PyTube.
        """

        try:
            # Object creation using YouTube
            yt = YouTube(link)
        except:
            return -1

        # TODO - ERROR CHECKS
        if vformat == "mp4":
            # Filters out all the files with 'mp4' extension 
            video = yt.streams.get_highest_resolution()
            video.download(path)
        elif vformat == "mp3":
            video = yt.streams.filter(only_audio=True).first()
            out = video.download(path)

            # Edit the extension
            base = out[:len(out)-4]
            os.rename(out, base + '.mp3')

        return 1
