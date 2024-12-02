# class MediaPlayer:
#
#     def play_audio(self):
#         raise NotImplementedError("Not implemented")
#
#     def play_video(self):
#         raise NotImplementedError("Not implemented")


class AudioPlayer:

    def play_audio(self):
        raise NotImplementedError("Not implemented")


class VideoPlayer:
    def play_video(self):
        raise NotImplementedError("Not implemented")


class MP3Player(AudioPlayer):

    def play_audio(self):
        print("Play MP3 file")


class MP4Player(VideoPlayer):

    def play_video(self):
        print("Play MP4 file")


class MultiMediaPlayer(AudioPlayer, VideoPlayer):

    def play_audio(self):
        print("Play audio file")

    def play_video(self):
        print("Play video file")

