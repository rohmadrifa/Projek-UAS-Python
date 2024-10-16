from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import os
import sys


class HomeScreen(Screen):
    # def __init__(self, **kwargs):
    #      super().__init__(**kwargs)
    pass

# class cobahomeApp(App):
#     def build(self):
#         Window.size = (360, 640)
#         kv_file_path = os.path.join(os.path.dirname(__file__), '..', 'kivy','login.kv')
#         Builder.load_file(kv_file_path)
#         return Dashboard()

# if __name__ == '__main__':
#     cobahomeApp().run()
