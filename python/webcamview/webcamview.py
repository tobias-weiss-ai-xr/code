#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import sys
from PIL import Image, ImageTk
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
if len(sys.argv) < 2:
    print( """webcamview.py
    Please pass a URL as argument.""")
    sys.exit()

pic_url = sys.argv[1]

root = tk.Tk()
root.title("Webcam-URL: " + pic_url)
label = tk.Label(root)

def get_image():
    my_page = urlopen(pic_url)
    my_picture = io.BytesIO(my_page.read())
    pil_img = Image.open(my_picture)
    tk_img = ImageTk.PhotoImage(pil_img)
    label = tk.Label(root, image=tk_img)
    label.pack(padx=5, pady=5)

get_image()
# root.after(1000, func=get_img)
root.mainloop()
