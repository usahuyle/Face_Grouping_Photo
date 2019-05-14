import face_recognition
from PIL import Image
import pathlib
import tkinter as tk
from tkinter import filedialog



def Get_Directory_Location():
    # hide the root windows using withdraw method
    root = tk.Tk()
    root.withdraw()

    # open the dialog to ask for directory
    directory = filedialog.askdirectory()

    return directory

# function get file the name of image into text file
# Pre:Need to open directory Dialog
def Locate_File_name(Find_Dir):
    name_ima = "All_Name_image.txt"
    # define the path & call function to get path dialog
    currentDirectory = pathlib.Path(Find_Dir)

    # define Type of image extension
    currentPattern = "*.jpg"

    # open to write all file name to txt file
    with open(name_ima,"w") as file_name:
        for currentFile in currentDirectory.glob(currentPattern):
            file_name.write(str(currentFile) + "\n")
    return name_ima



#function get face identification
def Get_Face_Identi(file_name):

    #read the txt file contain all photo name
    texts_list_loca =[]
    new_file = open(file_name, "r")
    for line in new_file:
        # location of file
        location = line.strip("\n")
        texts_list_loca.append(location)
    for i in range(len(texts_list_loca)):
        for j in range(i+1, len(texts_list_loca)):
            # load image for face_recognition
            image = face_recognition.load_image_file(texts_list_loca[i])
            image_2 = face_recognition.load_image_file(texts_list_loca[j])
            # encoding two image to compare
            face_encoding = face_recognition.face_encodings(image)
            face_encoding_2 = face_recognition.face_encodings(image_2)
            # loop through all face in both array of encoding of two image
            # compare two item in this list
            for face in face_encoding:
                for face_2 in face_encoding_2:
                    # call compare function to compare each faced in both image together
                    compare = face_recognition.compare_faces([face], face_2)
                    if compare == [True]:
                        print("This face is the same")
                        print(texts_list_loca[i] + "   ****   " +texts_list_loca[j])



    new_file.close()


File_name = Locate_File_name(Get_Directory_Location())
Get_Face_Identi(File_name)
