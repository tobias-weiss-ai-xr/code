#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

from gi.repository import Gtk, Gdk, GdkPixbuf

class rocketFacedetect(object):
    def __init__(self):
        cascPath = os.path.join(os.path.abspath(
            os.path.dirname(__file__)),'haarcascade_frontalface_default.xml')
        self.faceCascade = cv2.CascadeClassifier(cascPath)
        self.video_capture = cv2.VideoCapture(0)

    def __del__(self):
        self.video_capture.release()

    def capture(self):
        ret, frame = self.video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(50, 50),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
                )
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show directly via opencv highgui
        # cv2.imshow('Video', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        height, width, nChannels = rgb_image.shape
        return rgb_image, height, width, nChannels

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.cam = rocketFacedetect()
        self.box = Gtk.VBox()
        self.add(self.box)
        self.img = Gtk.Image()
        self.img.set_size_request(640, 480)
        self.box.pack_start(self.img, True, True, 0)
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        rgb_image, height, width, nChannels= self.cam.capture()
        # http://stackoverflow.com/questions/7906814/converting-pil-image-to-gtk-pixbuf
        # new_from_data() doesn't manage memory correctly, new_from_bytes() was recently added and
        # will be available in 3.14 (bugzilla.gnome.org/show_bug.cgi?id=732297).
        # See also: stackoverflow.com/questions/24062779/
        pixl = GdkPixbuf.PixbufLoader.new_with_type('pnm')
        # P6 is the magic number of PNM format,
        # and 255 is the max color allowed, see [2]
        pixl.write("P6 %d %d 255 " % (width, height) + rgb_image.tostring())
        pix = pixl.get_pixbuf()
        pixl.close()
        self.img.set_from_pixbuf(pix)

if __name__ == "__main__":
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
