from kivy.app import App
import vlc

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def play_echo(bl):
    music = vlc.MediaPlayer('https://msk47-echomsksni.cdnvideo.ru/stream3_128')

    if music:
        music.play()


class MusicWindow(App):

    def play_retro(self, bl):
        music = vlc.MediaPlayer('https://hls-01-retro.emgsound.ru/12/96/playlist.m3u8')

        if music:
            music.play()

    def play_record(self, bl):
        music = vlc.MediaPlayer('https://hls-01-radiorecord.hostingradio.ru/record/96/playlist.m3u8')

        if music:
            music.play()

    def build(self):

        bl = BoxLayout(orientation='vertical')

        bl.add_widget(Button(text="Эхо Москвы", font_size=26, size_hint=(1, .3), on_press=play_echo))
        bl.add_widget(Button(text="Ретро FM", font_size=26, size_hint=(1, .3), on_press=self.play_retro))
        bl.add_widget(Button(text="Нафталин FM", font_size=26, size_hint=(1, .3), on_press=self.play_record))

        return bl


if __name__ == "__main__":
    MusicWindow().run()
