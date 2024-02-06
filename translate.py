from googletrans import Translator


class Translate:
    def __init__(self, english_text, li, title, h2) -> None:
        self._english_text = english_text
        self._li = li
        self._h2 = h2
        self._polish_text = []
        self._polish_li = []
        self._english_title = title
        self._title = ""
        self._h2_polish = []

    def translate(self):
        print("-- Make translation")
        print(self._li)
        translator = Translator()  # Tra    nslating
        for i in self._english_text:
            
            self._polish_text.append(translator.translate(str(i), src='en', dest='pl').text)
     
        for i in self._li:
           
            self._polish_li.append(translator.translate(str(i), src='en', dest='pl'))

        self._title = translator.translate(str(self._english_title), src='en', dest='pl')
        for i in self._h2:
            self._h2_polish.append(translator.translate(str(i), src='en', dest='pl'))

    def get_polish(self):
        return self._polish_text

    def get_polish_li(self):
        return self._polish_li

    def get_polish_title(self):
        return self._title.text

    def get_polish_h2(self):
        return self.get_polish_h2
