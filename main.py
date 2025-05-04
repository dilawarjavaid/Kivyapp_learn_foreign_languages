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
        pass



