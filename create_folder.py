import os

#Thist file "create_folder" folder colled images to serve images from web sites 

class Create_foleder:

    #init folder name
    def __init__(self,folder_name) -> None:
        self.folder_name=folder_name

    #checks if folder exist
    def create_folder(self):
        if os.path.exists(self.folder_name):
            print("Folder images exist!!!!")
            print("")
            print("")
            print("")
        else:
            print("Creating folder images")
            print("")
            print("")
            print("")
            os.makedirs(self.folder_name)

   