from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

# Define your HomeScreen class
class HomeScreen(Screen):
    pass

# Define your ProfilScreen class
class ProfilScreen(Screen):
    pass

# Define the main App class with methods for navigation
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        
        # Add the HomeScreen and ProfilScreen to the ScreenManager
        sm.add_widget(HomeScreen(name="home_screen"))
        sm.add_widget(ProfilScreen(name="profil_screen"))
        
        return sm

    # Define the methods to manage screens (you can add real functionality here)
    def manage_program_kerja(self):
        print("Navigating to Program Kerja management screen...")

    def manage_budget(self):
        print("Navigating to Budget management screen...")

    def view_activity_report(self):
        print("Navigating to Activity Report screen...")

    def quit(self):
        print("Exiting the app...")
        self.stop()

# Run the app
if __name__ == '__main__':
    MyApp().run()
