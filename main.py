from extract_data import ExtractingData
from make_word import WordDocx
from translate import Translate
from user_interfase import Menu
from datetime import date
from create_folder import Create_foleder

if __name__ == "__main__":
    #init date

    todays_date = date.today() 


    # Init Ui
    UI = Menu()

    # print art
    UI.welcome()

    # print Main menu text 
    UI.options()

    # get links from user
    links = UI.get_links()

    # make dir for images if it dose not exist
    folder = Create_foleder('images')
    folder.create_folder()

    # for cycle for extract data
    for i in range(len(links)):

        Start = ExtractingData('images', links[i])
        Start.delete_files_in_folder_before_parsing()

        match links[i][0:25]:
            # check what siet it is
            case "https://thehackernews.com":
                Start.parsing_thehackernews()

        # main params
        titletext = Start.get_titletext()
        maintext = Start.get_maintext()
        tags = Start.get_tags()
        li = Start.get_li()
        link = Start.get_link()
        folder = Start.get_foledr()
        imgname = Start.get_imgname()
        h2 = Start.get_h2()

        # translate params
        Google_translate = Translate(maintext, li, titletext, h2)
        Google_translate.translate()


        # translate params
        main_text_polish = Google_translate.get_polish()
        li_text_polish = Google_translate.get_polish_li()
        h2_polish = Google_translate.get_polish_h2()
        polish_title = Google_translate.get_polish_title()

        # make word file
        Word = WordDocx(folder, link, polish_title, main_text_polish, tags, li_text_polish, imgname, i, h2_polish)
        Word.word_format()
    print("*" * 45)
    if len(links) > 1:
        Word.merge()
        print(f"Final file is Newsletter {todays_date.day}.{todays_date.month}.docx")
    else:
        print(f"Final file is Newsletter {todays_date.day}.{todays_date.month}.docx")
    print("*" * 45)
    x = input("Press Enter to escape...")
