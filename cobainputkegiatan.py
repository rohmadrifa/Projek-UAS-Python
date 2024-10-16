from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

class ProgramKerjaApp(App):
    def build(self):
        Window.size = (360, 640)

        # Root layout with padding and vertical orientation
        root_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        with root_layout.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Set background color (dark grey)
            self.rect = RoundedRectangle(size=root_layout.size, pos=root_layout.pos, radius=[20])

        # Bind the root layout size to update the rectangle size
        root_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Title Label
        title_label = Label(text="Program Kerja", font_size='26sp', bold=True, size_hint_y=None, height=dp(50),
                            color=(1, 1, 1, 1), halign='center')  # White text
        root_layout.add_widget(title_label)

        # Report Day Title
        day_label = Label(text="Hari 1", font_size='22sp', bold=True, size_hint_y=None, height=dp(40),
                          color=(0.2, 0.8, 0.2, 1), halign='center')  # Green text
        root_layout.add_widget(day_label)

        # Description Label
        description_label = Label(text="Kerja bakti membersihkan sampah", size_hint_y=None, height=dp(30),
                                  color=(1, 1, 1, 1))  # White text
        root_layout.add_widget(description_label)

        # TextInput for report
        report_input = TextInput(hint_text="Input hasil laporan...", multiline=True, size_hint_y=None,
                                  height=dp(120), background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1),
                                  padding=(10, 10), write_tab=False)  # White background, black text
        root_layout.add_widget(report_input)

        # Create a button layout
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10))

        # Upload button for documentation
        upload_button = Button(text="Upload Dokumentasi", size_hint_x=None, width=dp(150),
                               background_color=(0.2, 0.6, 0.8, 1), color=(1, 1, 1, 1))
        upload_button.bind(on_press=self.open_filechooser)
        button_layout.add_widget(upload_button)

        # Submit button for report
        submit_button = Button(text="Kirim Laporan", size_hint_x=None, width=dp(150),
                               background_color=(0.2, 0.8, 0.2, 1), color=(1, 1, 1, 1))
        submit_button.bind(on_press=self.submit_report)
        button_layout.add_widget(submit_button)

        root_layout.add_widget(button_layout)

        # Label for Dokumentasi
        dok_label = Label(text="DOKUMENTASI", font_size='22sp', bold=True, size_hint_y=None, height=dp(30),
                          color=(1, 1, 1, 1))  # White text
        root_layout.add_widget(dok_label)

        # BoxLayout for displaying the selected image
        self.image_display_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(150))
        self.image_display_layout.add_widget(Label(text="Gambar yang Dipilih", size_hint_y=None, height=dp(30), color=(1, 1, 1, 1)))

        # Placeholder for the image
        self.image_display = Image(source='', size_hint_y=None, height=dp(120))
        self.image_display_layout.add_widget(self.image_display)

        root_layout.add_widget(self.image_display_layout)

        return root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def open_filechooser(self, instance):
        # Open a file chooser to upload an image
        filechooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'])
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(filechooser)

        popup = Popup(title="Select Image", content=popup_layout, size_hint=(0.9, 0.9))
        popup.open()

        # Choose an image and update UI
        filechooser.bind(on_selection=lambda *x: self.on_selection(filechooser.selection, popup))

    def on_selection(self, selection, popup):
        if selection:
            self.update_image_display(selection[0])  # Update image display
        popup.dismiss()  # Close the popup

    def update_image_display(self, file_path):
        # Update the image display with the selected image
        self.image_display.source = file_path
        self.image_display.reload()  # Reload the image to display

    def submit_report(self, instance):
        # Placeholder function for submitting the report
        print("Laporan telah dikirim!")

if __name__ == '__main__':
    ProgramKerjaApp().run()
