import os
import shutil

fromdir="C:/Users/negis/Downloads"
todir="C:/Users/negis/Desktop/White/Project-102/Document_files"

listoffile=os.listdir(fromdir)
for filename in listoffile:
    name,extension=os.path.splitext(filename)
    if extension=="":
        continue
    if extension in [".pdf"]:
        path1=fromdir+"/"+filename
        path2=todir+"/"+"pdffile"
        path3=todir+"/"+"pdffile"+"/"+filename
        if os.path.exists(path2):
            print("Moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving")
            shutil.move(path1,path3)