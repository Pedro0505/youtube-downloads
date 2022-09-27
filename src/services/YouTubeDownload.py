import os


class YouTubeDownload:
    def __init__(self, youtube):
        self.youtube = youtube

    def only_song(self, url, path):
        print('Baixando...')
        yt = self.youtube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    def video(self, url, res, path):
        print('Baixando...')
        yt = self.youtube(url)
        video_fillter = yt.streams.filter(file_extension='mp4', res=res)
        video_fillter.first().download(output_path=path)
