from extract_data import ExtractingData
from make_word import WordDocx
from translate import Translate
from user_interfase import Menu
from datetime import date
from create_folder import Create_foleder
import tldextract
import os

#--------------------------
#       MAIN FILE
#--------------------------
if __name__ == "__main__":

    # Init date to add for file name
    todays_date = date.today() 


    # Init UI
    UI = Menu()

    # Print art
    UI.welcome()

    # Print Main menu text 
    UI.options()

    # Get links from user
    links = UI.get_links()

    # Make dir for images if it dose not exist
    folder = Create_foleder('images')
    folder.create_folder()

    # For cycle for extract data
    for i in range(len(links)):
        
        # Init class ExtractingData
        Start = ExtractingData('images', links[i])

        # delete_files_in_folder_before_parsing
        Start.delete_files_in_folder_before_parsing()

        # Determining which site it is
        ext = tldextract.extract(links[i])
        match ext.domain:   
            case "thehackernews":
                Start.parsing_thehackernews()
            case "bleepingcomputer":
                Start.parsing_bleepingcomputer()

        # Main params for creating word file
        titletext = Start.get_titletext()
        maintext = Start.get_maintext()
        tags = Start.get_tags()
        li = Start.get_li()
        link = Start.get_link()
        folder = Start.get_foledr()
        imgname = Start.get_imgname()
        h2 = Start.get_h2()
        
        # Translate title and main text
        Google_translate = Translate(maintext, li, titletext, h2)
        Google_translate.translate()


        # Get polish text
        main_text_polish = Google_translate.get_polish()
        li_text_polish = Google_translate.get_polish_li()
        h2_polish = Google_translate.get_polish_h2()
        polish_title = Google_translate.get_polish_title()

        # Creating word file
        Word = WordDocx(folder, link, polish_title, main_text_polish, tags, li_text_polish, imgname, i, h2_polish)
        Word.word_format()

    # Save docx format file
    print("*" * 45)
    if len(links) > 1:
        Word.merge()
        print(f"Final file is Newsletter {todays_date.day:02d}.{todays_date.month:02d}.docx")
    else:
        os.rename('0file.docx',f"Newsletter {todays_date.day:02d}.{todays_date.month:02d}.docx")
        print(f"Final file is Newsletter {todays_date.day:02d}.{todays_date.month:02d}.docx")
    print("*" * 45)

x = input("Press Enter to escape...")
