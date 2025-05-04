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
        # Grid layout for input and spinner
        grid_layout = GridLayout(cols=2, padding=10, spacing=20, size_hint_y=None, height=80)

        # User translation input
        self.translation_input = TextInput(
            hint_text='Type your translation here',
            font_size=18,
            multiline=True,
            size_hint_x=0.7,
            height=100
        )
        grid_layout.add_widget(self.translation_input)

        # Language selection spinner
        self.language_spinner = Spinner(
            text='Select language',
            values=('es', 'fr', 'de', 'it', 'pt'),
            size_hint=(0.3, None),
            height=44
        )
        grid_layout.add_widget(self.language_spinner)
        layout.add_widget(grid_layout)

        # Translate button layout
        button_layout = BoxLayout(size_hint_y=None, height=60)
        self.translate_button = Button(text='Translate', size_hint=(1, 1))
        self.translate_button.bind(on_press=self.translate_text)
        button_layout.add_widget(self.translate_button)
        layout.add_widget(button_layout)

        #Translation output
        self.translation_output = Label(
            text='',
            font_size=18,
            size_hint_y=None,
            height=100,
            halign='center',
            valign='middle'
        )
        self.translation_output.bind(size=self.translation_output.setter('text_size'))
        layout.add_widget(self.translation_output)

        return layout

    # Update the quote displayed when refresh button is pressed.
    def refresh_quote(self, instance):
        self.random_text = get_random_text()
        self.text_label.text = self.random_text

    # Translate the current quote using the selected language and show it.
    def translate_text(self, instance):
        target_language = self.language_spinner.text
        if target_language == 'Select language':
            self.translation_output.text = 'Please select a language'
        else:
            translator = Translator(to_lang=target_language)
            translated_text = translator.translate(self.random_text)
            self.translation_output.text = translated_text

if __name__ == '__main__':
    TranslationApp().run()













