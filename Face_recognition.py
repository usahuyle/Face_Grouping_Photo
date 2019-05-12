import face_recognition
import pathlib

#function get file the name of image into text file
def Locate_File_name():
    # define the path
    currentDirectory = pathlib.Path('.')

    #define Type of image extension
    currentPattern = "*.jpg"

    #open to write all file name to txt file
    File_Name = open("Name_File.txt","w")

    for currentFile in currentDirectory.glob(currentPattern):
        File_Name.write(str(currentFile) + "\n")
    File_Name.close()

#function get face identification
def Get_Face_Identi():
    New_File = open("Name_File.txt", "r")
    print("Enter the folder location: ")
    Folder_Loca =input(str())
    for line in New_File:
        #location of file
        location = Folder_Loca + line.strip("\n")
        #load image for face_recognition
        image = face_recognition.load_image_file(location)
        #get information of face location in the image
        face_loca = face_recognition.face_locations(image)
        print(face_loca)
    New_File.close()


Locate_File_name()
Get_Face_Identi()