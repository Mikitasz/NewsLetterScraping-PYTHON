import requests
from bs4 import BeautifulSoup
import os

def delete_files_in_folder(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files and delete each one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
      

    except Exception as e:
        print(f"An error occurred: {e}")

image_folder = "images"
delete_files_in_folder(image_folder)
input("Пожалуйста сонце введи количество линков и укажи сайты:\n 1)thehackernews.com\n 2)xxx\n 3)xxx\n")
input("А теперь вставь конкретные линки: ")
#url= "https://thehackernews.com/2023/12/remote-encryption-attacks-surge-how-one.html"
#url= "https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html"
headers={
"Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
}
#req = requests.get(url)
#src=req.text


#with open("index.html", "w") as file:
  #  file.write(src)


with open("index.html") as file:
    src=file.read()


soup= BeautifulSoup(src,'lxml')



title=soup.find_all(class_="story-title")
for item in title:
    item_text=item.text
    item_link=item.a.get("href")



item_main_text=""
paragraphs = soup.find_all("p")

for item in paragraphs:
 
    
    item_main_text+=item.text
item_main_text=item_main_text[:-94]
images=soup.find_all(class_="separator")


for img_tag in images[1:]:

    img_src = img_tag.find('img')
    img_link = img_src.get('data-src')
 
    response = requests.get(img_link)
    img_filename = os.path.join(image_folder,img_link.split("/")[-1])
    with open(img_filename, 'wb') as f:
        f.write(response.content)