import face_recognition
import pathlib
import tkinter as tk
from tkinter import filedialog
import os
import uuid
import time

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
    unique_filename = str(uuid.uuid4())
    name_ima = unique_filename+".txt"
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
def Get_Face_Identi(file_name, file_name_2):
    # make folder contain photo already compared
    os.system("mkdir Done")

    # read the txt file contain sample photo
    texts_list_loca =[]
    new_file = open(file_name, "r")

    # read the txt file contain photo need to compare
    texts_list_loca_2 = []
    new_file_2 = open(file_name_2 , "r")

    count =0
    # append the path of the photo to list
    for line in new_file:
        # location of file
        location = line.strip("\n")
        texts_list_loca.append(location)
    # append the path of the photo need to compare to list
    for line in new_file_2:
        # location of file
        location = line.strip("\n")
        texts_list_loca_2.append(location)
    #loop through all of the list to compare faces
    for i in texts_list_loca:
        for j in texts_list_loca_2:
            # load image for face_recognition
            image = face_recognition.load_image_file(i)
            image_2 = face_recognition.load_image_file(j)
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
                        # count number of True in the array
                        count += 1
            # if there are more than two "True" value just return one
            if count >= 1:
                print("This face is the same")

                os.system("cp " + j + " Done")





    new_file.close()
    new_file_2.close()

    os.system("rm *txt")

sample_photo_name = Locate_File_name(Get_Directory_Location())
time.sleep(2)
photo_being_compared = Locate_File_name(Get_Directory_Location())
Get_Face_Identi(sample_photo_name, photo_being_compared)

