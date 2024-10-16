from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class PengelolaanProgramKerja(BoxLayout):
    pass
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
import os
import sys


class PengelolaanProgramKerja(BoxLayout):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
    pass

class cobapengelolaanApp(App):
    def build(self):
        Window.size = (360, 640)
        kv_file_path = os.path.join(os.path.dirname(__file__), '..', 'kivy','login.kv')
        Builder.load_file(kv_file_path)
        return PengelolaanProgramKerja()

if __name__ == '__main__':
    cobapengelolaanApp().run()
