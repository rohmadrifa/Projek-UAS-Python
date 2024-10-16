from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.metrics import dp

# Sample data for table
data = [
    {"No": 1, "Tanggal": "17-08-2024", "Sumber": "kampus", "Jumlah": "2,000,000"},
    {"No": 2, "Tanggal": "18-08-2024", "Sumber": "udin", "Jumlah": "1,000,000"},
    {"No": 3, "Tanggal": "18-08-2024", "Sumber": "udin", "Jumlah": "2,000,000"},
    {"No": 4, "Tanggal": "20-08-2024", "Sumber": "Ketua RT", "Jumlah": "5,000,000"},
    {"No": 5, "Tanggal": "20-08-2024", "Sumber": "bakti sosial", "Jumlah": "5,000,000"},
]

class BudgetApp(App):
    def build(self):
        # Set window size for mobile simulation
        Window.size = (360, 640)
        
        # Root layout with padding and vertical orientation
        root_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Creating Scrollable Table Layout
        table_layout = GridLayout(cols=5, spacing=dp(5), size_hint_y=None)
        table_layout.bind(minimum_height=table_layout.setter('height'))
        
        # Adding Table Headers with bold font
        headers = ["No.", "Tanggal", "Sumber", "Jumlah", "Aksi"]
        for header in headers:
            table_layout.add_widget(Label(text=header, bold=True, size_hint_y=None, height=dp(30)))

        # Adding Rows for each data entry
        for entry in data:
            table_layout.add_widget(Label(text=str(entry["No"]), size_hint_y=None, height=dp(30)))
            table_layout.add_widget(Label(text=entry["Tanggal"], size_hint_y=None, height=dp(30)))
            table_layout.add_widget(Label(text=entry["Sumber"], size_hint_y=None, height=dp(30)))
            table_layout.add_widget(Label(text=entry["Jumlah"], size_hint_y=None, height=dp(30)))
            
            # Action buttons (Edit and Delete) with smaller icons
            action_layout = BoxLayout(orientation='horizontal', spacing=dp(5), size_hint_y=None, height=dp(30))
            edit_button = Button(text="✏️", size_hint=(None, None), width=dp(30), height=dp(30))
            delete_button = Button(text="🗑️", size_hint=(None, None), width=dp(30), height=dp(30))
            action_layout.add_widget(edit_button)
            action_layout.add_widget(delete_button)
            table_layout.add_widget(action_layout)
        
        # Make the table scrollable
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, dp(200)))
        scroll_view.add_widget(table_layout)
        root_layout.add_widget(scroll_view)

        # Display Total Budget at the bottom
        total_label = Label(text="Total Anggaran KKN: Rp. 15,000,000.00", size_hint_y=None, height=dp(40), font_size=dp(16))
        root_layout.add_widget(total_label)

        # Add New Entry Floating Button
        add_button = Button(text="+", size_hint=(None, None), width=dp(50), height=dp(50), pos_hint={'center_x': 0.5})
        add_button.bind(on_press=self.add_entry)
        root_layout.add_widget(add_button)
        
        return root_layout
    
    def add_entry(self, instance):
        # Popup for adding a new entry with proper spacing
        popup_content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        popup_content.add_widget(Label(text="Tambah Data Baru", size_hint_y=None, height=dp(40)))
        
        new_tanggal = TextInput(hint_text="Tanggal Pemasukan", size_hint_y=None, height=dp(40))
        new_sumber = TextInput(hint_text="Sumber", size_hint_y=None, height=dp(40))
        new_jumlah = TextInput(hint_text="Jumlah Dana", size_hint_y=None, height=dp(40))
        
        popup_content.add_widget(new_tanggal)
        popup_content.add_widget(new_sumber)
        popup_content.add_widget(new_jumlah)
        
        # Save new entry logic
        def on_save(instance):
            print(f"Saved: {new_tanggal.text}, {new_sumber.text}, {new_jumlah.text}")
            popup.dismiss()

        # Save button for the popup
        save_button = Button(text="Simpan", size_hint_y=None, height=dp(40))
        save_button.bind(on_press=on_save)
        popup_content.add_widget(save_button)

        # Popup definition
        popup = Popup(title="Tambah Data", content=popup_content, size_hint=(None, None), size=(dp(300), dp(400)))
        popup.open()

if __name__ == '__main__':
    BudgetApp().run()
