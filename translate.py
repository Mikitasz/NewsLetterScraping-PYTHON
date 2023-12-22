from googletrans import Translator

class Translate:
    def __init__(self,english_text,li) -> None:
        self._english_text=english_text
        self._li=li
        self._polish_text=[]
        self._polish_li=[]
    def translate(self):
        
        translator = Translator()# Translating
        for i in self._english_text:   
            self._polish_text.append(translator.translate(str(i), src='en', dest='pl'))
        print(str(len(self._li))+"sadsadas")
        for i in self._li:   
            self._polish_li.append(translator.translate(str(i), src='en', dest='pl'))
      
    def get_polish(self):
        return self._polish_text
    def get_polish_li(self):
        return self._polish_li
