from googletrans import Translator

class Translate:
    def __init__(self,english_text) -> None:
        self._english_text=english_text
        self._polish_text=""
    def translate(self):
        translator = Translator()# Translating
        self._polish_text = translator.translate(self._english_text, src='en', dest='pl')

      
    def get_polish(self):
        return self._polish_text
