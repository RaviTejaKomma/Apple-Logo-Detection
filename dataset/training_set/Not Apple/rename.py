import os

def rename_images():
    files = os.listdir()
    i = 0
    for file in files:
        newfilename = str(i) + ".jpg"
        i+=1
        os.rename(file, newfilename)
        print(file,"renamed to",newfilename)

if __name__ == "__main__":
    rename_images()
