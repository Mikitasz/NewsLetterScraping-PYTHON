import os
import shutil
class Create_foleder:
    def __init__(self,folder_name) -> None:
        self.folder_name=folder_name
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

   