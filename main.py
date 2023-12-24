
from extract_data import Extracting_data
from make_word import Word_docx
from translate import Translate
from user_interfase import Menu
from GUI import GUI
if __name__ == "__main__":
    #gui=GUI()
    #gui.dearpy()
    UI=Menu()
    UI.welcome()
    UI.options()
    links=UI.get_links()
    for i in range(len(links)):
        
      Start=Extracting_data('images',links[i])
      #Start=Extracting_data('images',"https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html")
      Start.delete_files_in_folder_before_parsing()
      print(links[i][0:25])
      match links[i][0:25]:
        case "https://thehackernews.com":
          Start.parsing_thehackernews()
       # case "https://thehackernews.com":
         # Start.parsing_thehackernews()
      titletext=Start.get_titletext()
      maintext=Start.get_maintext()
      tags=Start.get_tags()
      li=Start.get_li()
      link=Start.get_link()
      folder=Start.get_foledr()
      imgname=Start.get_imgname()
      h2=Start.get_h2()

      Google_translate=Translate(maintext,li,titletext,h2)
      Google_translate.translate()
      main_text_polish=Google_translate.get_polish()
      li_text_polish=Google_translate.get_polish_li()
      h2_polish=Google_translate.get_polish_h2()
      polish_title=Google_translate.get_polish_title()
      Word=Word_docx(folder,link,polish_title,main_text_polish,tags,li_text_polish,imgname,i,h2_polish)
      Word.word_format()

    if len(links)>1:
      Word.merge()



    