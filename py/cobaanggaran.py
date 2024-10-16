from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.metrics import dp

class MyGrid(GridLayout):
    pass

class MyApp(App):
    def build(self):
        Window.size = (360, 640)
        return self.root

if __name__ == '__main__':
    MyApp().run()
