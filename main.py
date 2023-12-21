
from extract_data import Extracting_data
from make_word import Word_docx
from translate import Translate

if __name__ == "__main__":
 
    Start=Extracting_data('images',"https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html")
    Start.delete_files_in_folder_before_parsing()
    Start.parsing_thehackernews()
    titletext=Start.get_titletext()
    maintext=Start.get_maintext()
    print(maintext)
    link=Start.get_link()
    folder=Start.get_foledr()



    Google_translate=Translate(maintext)
    Google_translate.translate()
    main_text_polish=Google_translate.get_polish()
  
    Word=Word_docx(folder,link,titletext,main_text_polish)
    Word.word_format()



    