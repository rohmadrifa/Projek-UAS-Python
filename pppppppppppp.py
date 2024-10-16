from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label  # Add this import
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.lang import Builder  # Import for loading .kv files

# # Load the .kv file manually
# Builder.load_file('myapp.kv')

# Custom button with shadow
class ShadowButton(Button):
    pass

class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)

        # Set window size
        Window.size = (360, 640)

    def create_text_input(self, hint_text, password=False):
        """Create a text input with rounded corners."""
        return TextInput(
            hint_text=hint_text,
            multiline=False,
            password=password,
            size_hint=(1, None),
            height=dp(50),
            background_normal='',
            background_color=(1, 1, 1, 0.1),  # Input background
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            font_size='16sp',
            halign='left',
            padding=(dp(15), dp(10))
        )

    def create_account(self):
        name = self.ids.name_input.text
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text

        if not name or not email or not password or not confirm_password:
            self.show_popup("Error", "Semua field harus diisi.")
        elif password != confirm_password:
            self.show_popup("Error", "Kata sandi tidak cocok.")
        else:
            self.show_popup("Sukses", f"Akun telah dibuat untuk {name}!")

    def show_popup(self, title, message):
        popup_content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        popup_content.add_widget(Label(text=message, color=(0, 0, 0, 1)))  # Label is used here
        close_button = Button(text="Tutup", size_hint=(1, None), height=dp(40))
        popup_content.add_widget(close_button)
        
        popup = Popup(title=title, content=popup_content, size_hint=(0.8, 0.3))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CreateAccountScreen(name="create_account"))
        return sm

if __name__ == "__main__":
    MyApp().run()
