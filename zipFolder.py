import os
import shutil
from Imports.GetFolderInfo import GetFolderInfo
from Imports.Menu import Menu

def zipSingleFolder(folder_path, folder_name):
    print(f'Converting folder "{folder_name}" into a zip file.')
    shutil.make_archive(f"{folder_name}", format="zip", root_dir=folder_path)

def zipMultipleFolders(subfolder_paths, subfolder_names):
    for i, (sub_path, sub_name) in enumerate(zip(subfolder_paths, subfolder_names)):
        print(f"{i+1}/{len(subfolder_names)}")
        print(f'Converting folder "{sub_name}" into a zip file.\n')
        shutil.make_archive(f"{sub_name}", format="zip", root_dir=sub_path)

def main():
    getFolderInfo = GetFolderInfo()
    choice = Menu().loopMenu()
    if (choice == "y"):
        folder_path = getFolderInfo.askFolderLoc()
        if folder_path is None:
            print("\nCancelled")
        else:
            subfolder_paths = getFolderInfo.getSubFolders(folder_path)
            subfolder_names = getFolderInfo.getSubFolderNames(subfolder_paths)
            os.chdir(folder_path)
            zipMultipleFolders(subfolder_paths, subfolder_names)
            print("\nCompleted\n")
    elif (choice == "n"):
        folder_path = getFolderInfo.askFolderLoc()
        if folder_path is None:
            print("\nCancelled")
        else:
            folder_name = getFolderInfo.getFolderName(folder_path)
            folder_base_name = getFolderInfo.getBaseFolderName(folder_path)
            os.chdir(folder_base_name)
            zipSingleFolder(folder_path, folder_name)
            print("\nCompleted\n")
    else:
        print("Error")

if __name__=="__main__":
    main()