class Menu:
    def loopMenu(self):
        while True:
            choice = input('Zip Multiple Folders (y/n): ').lower().strip()
            if (choice == "y"):   
                print("You have chosen to Zip Multiple Folders\n") 
                print("Choose Folder that Contains the Subfolders you want to ZIP.\n")
                print("e.g.\n"
                    "MAIN_FOLDER\n"
                    "   |_> FOLDER_1\n"
                    "   |_> FOLDER_2\n")
                print("When Choosing the MAIN_FOLDER,\nFOLDER_1, FOLDER_2 will be Zipped.\n")
                return "y"           
            elif(choice == "n"):
                print("You have chosen to Zip a Single Folder\n")
                print("Choose which Folder to Zip.\n")
                return "n"
            else:
                print("\nInvalid Input. Try Again.\n")