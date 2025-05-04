This is a language learning app built using Python and Kivy. It helps users practice translation by comparing their own translations of English quotes to automatically generated translations using a translation API.

The app has a simple and intuitive interface, but leverages powerful tools to make language learning effective and engaging.

🚀 Project Overview
When the app is launched:

A random quote is fetched from the internet using a public REST API.

The user can type their own translation of the quote into a text field.

The user then selects the target language they’re learning.

When the “Translate” button is clicked, the app uses an automatic translator to show the correct translation.

Users can click “Refresh Quote” to get a new quote and repeat the process.

This app is ideal for language learners who want to practice their skills and check their translations in real time.

🖼️ App Interface
Displays a random English quote

Text input area for user translation

Dropdown menu to choose a target language

“Translate” button to show correct translation

“Refresh Quote” button to load a new quote

🌍 Supported Target Languages
Spanish (es)

French (fr)

German (de)

Italian (it)

Portuguese (pt)

⚙️ Environment Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/translation-practice-app.git
cd translation-practice-app
Install required dependencies:

bash
Copy
Edit
pip install requests kivy
Run the application:

bash
Copy
Edit
python main.py
Note: Make sure Python 3 is installed on your system.

🧠 How It Works
Quotes API: Uses the Forismatic API to fetch motivational quotes.

Translation Engine: Uses the translate Python module to convert quotes into the selected target language.

UI Framework: Built with Kivy for cross-platform GUI support.

🛠️ Dependencies
Kivy – GUI framework for building interactive apps

Requests – HTTP library for making API calls

translate – Python module for text translation

🧪 Example Use Case
Launch the app.

Read the quote.

Try translating it yourself.

Select a language like Spanish.

Click Translate to compare your translation.

Press Refresh Quote and repeat.

📚 License
This project is open-source and free to use under the MIT License.
