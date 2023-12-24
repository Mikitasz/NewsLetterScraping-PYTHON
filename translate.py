from googletrans import Translator

class Translate:
    def __init__(self,english_text,li,title) -> None:
        self._english_text=english_text
        self._li=li
        self._polish_text=[]
        self._polish_li=[]
        self._eanglosh_title=title
        self._title=""
    def translate(self):
        
        translator = Translator()# Translating
        for i in self._english_text:   
            self._polish_text.append(translator.translate(str(i), src='en', dest='pl'))
        
        for i in self._li:   
            self._polish_li.append(translator.translate(str(i), src='en', dest='pl'))
       
        self._title=translator.translate(str(self._eanglosh_title),src='en', dest='pl')
       
    def get_polish(self):
        return self._polish_text
    def get_polish_li(self):
        return self._polish_li
    def get_polish_title(self):
        return self._title.text