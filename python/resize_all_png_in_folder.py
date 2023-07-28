from PIL import Image
import os
path = "c:/Users/tbswe/Desktop/produktbilder/"
dirs = os.listdir( path )
width=1024
hight=768
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            if not item[-4:] == ".png":
                continue
            img = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            stem = f.split("/")[-1]
            small_path  = path + "/small/"
            img = img.resize((width, hight), Image.ANTIALIAS)
            os.makedirs(small_path, exist_ok=True)
            img.save(small_path + stem + '_small.png') 
resize()