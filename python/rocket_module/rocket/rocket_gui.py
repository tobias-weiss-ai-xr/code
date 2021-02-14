#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
gtk.gdk.threads_init()
import threading
import time
from rocket_cmd import rocketManager
from rocket_facedetect import rocketFacedetect

"""
Todo:
-Add coloured button for shooting
-use config
"""

class rocketGui(object):
    """ PyGTK GUI for the rocket launcher """
    def __init__(self):
        self.step_time = 10
        self.cmd = rocketManager() #get rocket instances
        self.cmd.connect()

        # GUI setup
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(20) #set the border width of the window.
        self.box = gtk.VBox(False, 0) #create box to arrange widgets
        self.window.add(self.box)
        self.video_window = gtk.Image() #create image box
        self.video_window.set_size_request(640, 480)
        self.box.pack_start(self.video_window) #add image to box
        self.table = gtk.Table(3, 3, True) #create table for movement buttons
        self.box.pack_start(self.table, True, True, 0) #add table to box

        #create movement buttons
        self.button_up = gtk.Button("up (_w)")
        self.button_down = gtk.Button("down (_s)")
        self.button_left = gtk.Button("left (_a)")
        self.button_right = gtk.Button("right (_d)")
        self.button_shoot = gtk.Button("shoot (_f)")

        #handle the delete_event
        self.window.connect("delete_event", self.delete_event)

        #connect buttons
        self.button_up.connect("pressed", self.button_callback, "up")
        self.button_up.connect("released", self.button_callback, "stop")
        self.button_down.connect("pressed", self.button_callback, "down")
        self.button_down.connect("released", self.button_callback, "stop")
        self.button_left.connect("pressed", self.button_callback, "left")
        self.button_left.connect("released", self.button_callback, "stop")
        self.button_right.connect("pressed", self.button_callback, "right")
        self.button_right.connect("released", self.button_callback, "stop")
        self.button_shoot.connect("released", self.button_callback, "shoot")

        #connect keyboard movement
        self.window.connect("key-press-event", self.key_callback)

        #define button positions
        self.table.attach(self.button_up, 1, 2, 0, 1)
        self.table.attach(self.button_down, 1, 2, 2, 3)
        self.table.attach(self.button_left, 0, 1, 1, 2)
        self.table.attach(self.button_right, 2, 3, 1, 2)
        self.table.attach(self.button_shoot, 1, 2, 1, 2)

        self.cam = rocketFacedetect() # start facedeetect
        cam_thread = threading.Thread(target=self.get_facedetect_image)
        cam_thread.daemon = True
        cam_thread.start()

        # Finally show the window
        self.window.show_all()

    # callback to pass arguments issued by buttons
    def button_callback(self, widget, data):
        self.cmd.move(data, self.step_time, "gui")

    # callback to pass arguments issued by the keyboard
    def key_callback(self, widget, event):
        key = gtk.gdk.keyval_name(event.keyval)
        if key == "w":
            data = "up"
        elif key == "s":
            data = "down"
        elif key == "a":
            data = "left"
        elif key == "d":
            data = "right"
        elif key == "f":
            data = "shoot"
        else:
            data = "stop"
        self.cmd.move(data, self.step_time, "button")

    # set the cv2 image to the image widget
    def get_facedetect_image(self):
        while True:
            rgb_image, height, width, nChannels= self.cam.capture()
            loader = gtk.gdk.PixbufLoader()
            loader.write("P6 %d %d 255 " % (width, height) + rgb_image.tostring())
            pixbuf = loader.get_pixbuf()
            loader.close()
            self.video_window.set_from_pixbuf(pixbuf)
            time.sleep(500 / 1000.0)

    # delete event
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()

def main():
    gui = rocketGui()
    gtk.gdk.threads_enter()
    gtk.main()
    gtk.gdk.threads_leave()

if __name__ == "__main__":
    main()
