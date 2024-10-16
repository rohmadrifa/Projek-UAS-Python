from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import os
from py.login import LoginScreen
from py.homescreen import ProfilScreen
from py.cobahome import HomeScreen

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):    
        # Set the window size
        Window.size = (360, 640)

        # Load the .kv files
        kv_path = os.path.join(os.path.dirname(__file__), 'kivy')
        Builder.load_file(os.path.join(kv_path, 'login.kv'))
        Builder.load_file(os.path.join(kv_path, 'homescreen.kv'))
        

        # Initialize the ScreenManager and add screens
        sm = MyScreenManager()  # Notice the parentheses to initialize
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ProfilScreen(name='profil'))
        sm.add_widget(HomeScreen(name='home'))

        # Set the initial screen
        sm.current = 'login'
        return sm

if __name__ == '__main__':
    MyApp().run()
