from googletrans import Translator
from extract_data import item_main_text
translator = Translator()# Translating
translated = translator.translate(item_main_text, src='en', dest='pl')

polish_text=translated.text