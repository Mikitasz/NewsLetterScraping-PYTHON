import requests
from bs4 import BeautifulSoup
import os
from make_word import Word_docx
class Extracting_data:

    def __init__(self,images_folder,url) -> None:
        self._images_folder = images_folder
        self._url = url
        self._item_link=""
        self._img_link=""
        self._titlestext=""
        self._item_main_text=""
        self._img_filename=""
    def delete_files_in_folder_before_parsing(self):
        try:
            files = os.listdir(self._images_folder)
            for file_name in files:
                file_path = os.path.join(self._images_folder, file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        except Exception as e:
            print(f"An error occurred: {e}")


    def parsing_thehackernews(self):    
        #url= "https://thehackernews.com/2023/12/remote-encryption-attacks-surge-how-one.html"
        #self.url= "https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html"
        headers={
        "Accept":"*/*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        }
        req = requests.get(self._url,headers=headers)
        src=req.text

        #with open("index.html", "w") as file:
        #  file.write(src)

        #with open("index.html") as file:
        #   src=file.read()
        soup= BeautifulSoup(src,'lxml')
        title=soup.find_all(class_="story-title")
        for item in title:
            self._titlestext=item.text
            self._item_link=item.a.get("href")

        
        #paragraphs = soup.find_all("p")
        paragraphs=soup.find_all(class_="articlebody")
        print(paragraphs)
        for item in paragraphs:
            self._item_main_text+=item.text
        self._item_main_text=self._item_main_text[:-110]
        images=soup.find_all(class_="separator")

        for img_tag in images[1:]:

            img_src = img_tag.find('img')
            _img_link = img_src.get('data-src')
        
            response = requests.get(_img_link)
            self._img_filename = os.path.join(self._images_folder,_img_link.split("/")[-1])
      
            with open(self._img_filename, 'wb') as f:
                f.write(response.content)


    def get_titletext(self):
        return self._titlestext
    def get_maintext(self):
        return self._item_main_text
    def get_link(self):
        return self._item_link
    def get_foledr(self):
        return self._images_folder