import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from PIL import Image

class Extracting_data:

    def __init__(self,images_folder,url) -> None:
        self._images_folder = images_folder
        self._url = url
        self._item_link=""
        self._img_link=""
        self._titlestext=""
        self._item_main_text=[]
        self._img_filename=[]
        self._tegs=[]
        self._li=[]
        self._count=0
        self._h2=[]
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
            print(item.text)
            self._titlestext=item.text
            self._item_link=item.a.get("href")

        tags=soup.find_all('div', class_='articlebody')[0].find_all()
      
        for tag in tags:
            if tag.name == 'img' and 'lazyload' in tag.get('class', []):
                print("lazyload")
            elif tag.name == 'p' and 'wn-description' in tag.get('class', []):
                print("lisznije p")
            else:
                self._tegs.append(tag.name)
       
        exclude_tags = ['div', 'a', 'center','br','i','ul','section','span','table','tr','td','em','tbody','script','noscript','strong','center']     
        self._tegs = [tag for tag in self._tegs if tag not in exclude_tags]
        self._tegs.remove('img')
        print(self._tegs)

        paragraphs = soup.find_all("p")
       # paragraphs=soup.find_all(class_="articlebody")
        li= soup.find_all('div', class_='articlebody')[0].find('ul')
        h2= soup.find_all('h2')
       
        try:
            for item in list(h2):
                self._h2.append(item.text)
            exclude_tags3 = ['\n']     
            self._h2 = [tag for tag in self._h2 if tag not in exclude_tags3]
        except:
            print("No h2 tags")
        
        for item in paragraphs:
            if item.name == 'p' and 'wn-description' in item.get('class', []):
                print("nothing")
            else:
                self._item_main_text.append(item.text)
        try:
            for item in list(li):
                self._li.append(item.text)
            exclude_tags2 = ['\n']     
            self._li = [tag for tag in self._li if tag not in exclude_tags2]
        except:
            print("No li tags")
        for item in paragraphs:
            self._item_main_text.append(item.text)

        
        self._item_main_text=self._item_main_text[:-1]
      
        images=soup.find_all(class_="separator")
     
        for img_tag in images[1:]:

            img_src = img_tag.find('img')
      
            _img_link = img_src.get('data-src')

            response = requests.get(_img_link)
            self._img_filename.append(os.path.join(self._images_folder,_img_link.split("/")[-1]))
            urllib.request.urlretrieve(_img_link, self._img_filename[self._count])
            img=Image.open(self._img_filename[self._count])
            img=img.save(self._img_filename[self._count])
            self._count+=1
           # with open(self._img_filename, 'wb') as f:
            #    f.write(response.content)
            

    def get_titletext(self):
        return self._titlestext
    def get_maintext(self):
        return self._item_main_text
    def get_link(self):
        return self._item_link
    def get_foledr(self):
        return self._images_folder
    def get_tags(self):
        return self._tegs
    def get_li(self):
        return self._li
    def get_imgname(self):
        return self._img_filename  
    def get_h2(self):
        return self._h2