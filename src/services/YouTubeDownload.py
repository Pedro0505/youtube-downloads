import os
import shutil
import moviepy.editor as mpe


class YouTubeDownload:
    def __init__(self, youtube):
        self.youtube = youtube
        self.v_name = "video.mp4"
        self.a_name = "audio.mp3"

    def only_song(self, url, path):
        yt = self.youtube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    def video(self, url, res, path):
        yt = self.youtube(url)

        video = yt.streams.filter(file_extension='mp4', res=res)
        video_download = video.first().download(output_path=path)
        shutil.move(video_download, path + self.v_name)

        audio = yt.streams.filter(only_audio=True)
        audio_download = audio.first().download(output_path=path)
        shutil.move(audio_download, path + self.a_name)

        self.merge_video_with_audio(yt.title, path)

    def merge_video_with_audio(self, video_title, path):
        video = mpe.VideoFileClip(path + self.v_name)
        audio = mpe.AudioFileClip(path + self.a_name)
        final = video.set_audio(audio)

        final.write_videofile(path + video_title + '.mp4')

        os.remove(path + self.v_name)
        os.remove(path + self.a_name)
