#!/usr/bin/env python
""" PyGTK GUI for the rocket launcher """
import pygtk
pygtk.require('2.0')
import gtk
from rocket_cmd import *
from rocket_cam import *

class rocketGui:
    def __init__(self):
        #get rocket instance
        self.connect_cmd()
        self.connect_cam()

        #ceate a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        #set the title of the window
        self.window.set_title("Rocket Launcher Control Center")

        #set the border width of the window.
        self.window.set_border_width(20)

        #create box to arrange widgets
        self.box = gtk.VBox(False, 0)
        self.window.add(self.box)

        #create video box
        self.cam.video_window = gtk.DrawingArea()
        self.cam.video_window.set_size_request(640, 480)
        #add table to box
        self.box.pack_start(self.cam.video_window)

        #create movement buttons
        self.button_up = gtk.Button("up (_w)")
        self.button_down = gtk.Button("down (_s)")
        self.button_left = gtk.Button("left (_a)")
        self.button_right = gtk.Button("right (_d)")
        # add a coloured box around the shoot button
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

        #create table for movement buttons
        self.table = gtk.Table(3, 3, True)
        #add table to box
        self.box.pack_start(self.table)
        #define button positions
        self.table.attach(self.button_up, 1, 2, 0, 1)
        self.table.attach(self.button_down, 1, 2, 2, 3)
        self.table.attach(self.button_left, 0, 1, 1, 2)
        self.table.attach(self.button_right, 2, 3, 1, 2)
        self.table.attach(self.button_shoot, 1, 2, 1, 2)

        # Finally show the window
        self.window.show_all()

    # create a rocket cmd instance
    def connect_cmd(self):
        self.cmd = rocketManager()
        self.cmd.connect()

    def connect_cam(self):
        self.cam = rocketCam()

    # callback to pass arguments issued by the buttons to the cmd.
    # The data passed to this method is printed to stdout.
    def button_callback(self, widget, data):
        print "%s was pressed" % data
        self.cmd.issueCommand(data, 10, "gui")

    # callback to pass arguments issued by the buttons to the cmd.
    def key_callback(self, widget, event):
        key = gtk.gdk.keyval_name(event.keyval)
        print "%s was pressed" % key
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
        self.cmd.issueCommand(data, 10, "button")

    # delete event
    def delete_event(self, widget, event, data=None):
        self.cam.exit()
        gtk.main_quit()
        return False

def main():
    gtk.gdk.threads_init()
    gtk.main()
    return 0

if __name__ == "__main__":
    gui = rocketGui()
    main()
