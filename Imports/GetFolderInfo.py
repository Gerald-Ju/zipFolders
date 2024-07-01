import os
from tkinter.filedialog import askdirectory

class GetFolderInfo:
    def askFolderLoc(self):
        print("\nChoose Folder\n")
        folder_path = askdirectory(title='Folder Location')
        if folder_path == "":
            return None
        else:
            return folder_path

    def getFolderName(self, folder_path):
        return os.path.basename(folder_path)

    def getBaseFolderName(self, folder_path):
        return os.path.dirname(folder_path)

    def getSubFolders(self, folder_path):
        sub_folder_paths = []
        sub_folders = os.listdir(folder_path)
        for folder in sub_folders:
            sub_folder_paths.append(rf"{folder_path}/{folder}")
        return sub_folder_paths
    
    def getSubFolderNames(self, subfolder_paths):
        list_subfolder_names = []
        for subfolder in subfolder_paths:
            list_subfolder_names.append(self.getFolderName(subfolder))
        return list_subfolder_names
