import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from PIL import Image


class ExtractingData:

    def __init__(self, images_folder, url) -> None:
        self._images_folder = images_folder
        self._url = url
        self._item_link = ""
        self._img_link = ""
        self._titlestext = ""
        self._item_main_text = []
        self._img_filename = []
        self._tags = []
        self._li = []
        self._count = 0
        self._h2 = []

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

        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        }
        req = requests.get(self._url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, 'lxml')
        title = soup.find_all(class_="story-title")

        for item in title:
            print("-- Geting title name")
            self._titlestext = item.text
            self._item_link = item.a.get("href")

        tags = soup.find_all('div', class_='articlebody')[0].find_all()
        print("-- Add tags")
        for tag in tags:
            if tag.name == 'img' and 'lazyload' in tag.get('class', []):
                pass
            elif tag.name == 'p' and 'wn-description' in tag.get('class', []):
                pass
            else:

                self._tags.append(tag.name)

        exclude_tags = ['div', 'a', 'center', 'br', 'i', 'ul', 'section', 'span', 'table', 'tr', 'td', 'em', 'tbody',
                        'script', 'noscript', 'strong', 'center']
        self._tags = [tag for tag in self._tags if tag not in exclude_tags]
        self._tags.remove('img')

        paragraphs = soup.find_all("p")
  
        li = soup.find_all('div', class_='articlebody')[0].find('ul')
        h2 = soup.find_all('h2')

        try:
            for item in list(h2):
                self._h2.append(item.text)
            exclude_tags3 = ['\n']
            self._h2 = [tag for tag in self._h2 if tag not in exclude_tags3]
            print("-- Getting <h2> tags")
        except:
            print("-- No <h2> tags")

        for item in paragraphs:
            if item.name == 'p' and 'wn-description' in item.get('class', []):
                pass
            else:

                self._item_main_text.append(item.text)
        try:
            for item in list(li):
                self._li.append(item.text)
            exclude_tags2 = ['\n']
            self._li = [tag for tag in self._li if tag not in exclude_tags2]
            print("-- Getting <li> tags")
        except:
            print("-- No <li> tags")
        for item in paragraphs:
            self._item_main_text.append(item.text)

        self._item_main_text = self._item_main_text[:-1]

        images = soup.find_all(class_="separator")
        print("-- Download images")
        for img_tag in images[1:]:
            img_src = img_tag.find('img')

            _img_link = img_src.get('data-src')


            self._img_filename.append(os.path.join(self._images_folder, _img_link.split("/")[-1]))
            urllib.request.urlretrieve(_img_link, self._img_filename[self._count])
            img = Image.open(self._img_filename[self._count])
            img = img.save(self._img_filename[self._count])
            self._count += 1

    def get_titletext(self):
        return self._titlestext

    def get_maintext(self):
        return self._item_main_text

    def get_link(self):
        return self._item_link

    def get_foledr(self):
        return self._images_folder

    def get_tags(self):
        return self._tags

    def get_li(self):
        return self._li

    def get_imgname(self):
        return self._img_filename

    def get_h2(self):
        return self._h2
