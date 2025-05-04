import requests
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from translate import Translator

def get_random_text():
    try:
        response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
        response.raise_for_status()
        return response.json()['quoteText']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random text: {e}")
        return "Default text as fallback."


class TranslationApp(App):
    def build(self):
        self.title = 'Translation App'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Add quote display label
        self.random_text = get_random_text()
        self.text_label = Label(
            text=self.random_text,
            font_size=18,
            size_hint_y=None,
            height=100,
            halign='center',
            valign='middle'
        )
        self.text_label.bind(size=self.text_label.setter('text_size'))
        layout.add_widget(self.text_label)

        #Add a refresh button
        refresh_button = Button(text='Refresh Quote', size_hint=(1, None), height=60)
        refresh_button.bind(on_press=self.refresh_quote)
        layout.add_widget(refresh_button)








