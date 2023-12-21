import requests
from bs4 import BeautifulSoup
import os
image_folder = "images"
#url= "https://thehackernews.com/2023/12/remote-encryption-attacks-surge-how-one.html"
url= "https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html"
headers={
"Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
}
req = requests.get(url)
src=req.text


with open("index.html", "w") as file:
    file.write(src)


with open("index.html") as file:
    src=file.read()


soup= BeautifulSoup(src,'lxml')



title=soup.find_all(class_="story-title")
for item in title:
    item_text=item.text
    item_link=item.a.get("href")


text=soup.find_all(class_="articlebody")
for item in text:
   
    item_main_text=item.text[:-110]
    print(item_main_text)
images=soup.find_all(class_="separator")


for img_tag in images[1:]:

    img_src = img_tag.find('img')
    img_link = img_src.get('data-src')
 
    response = requests.get(img_link)
    img_filename = os.path.join(image_folder,img_link.split("/")[-1])
    with open(img_filename, 'wb') as f:
        f.write(response.content)