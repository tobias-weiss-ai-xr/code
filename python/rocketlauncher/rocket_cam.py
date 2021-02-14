#!/usr/bin/env python

import sys
from os.path import exists
import pygst
import gst

# Gstreamer constants
gst_src             = 'v4l2src device=' # VideoForLinux driver asociated with specified device
gst_src_format      = 'video/x-raw-yuv' # colorspace specific to webcam
gst_videosink       = 'xvimagesink'     # sink habilitated to manage images
sep                 = ' ! '             # standard gstreamer pipe. Don't change that

device = "/dev/video0"
height = "480"
width = "640"
framerate = "30"
snap_format = "jpeg"

class rocketCam:
    def __init__(self):
        # Before anything, let's be sure that we have a webcam plugged in
        self.device = str(device)
        if not exists(self.device):
            print "No webcam detected: /dev/video0 cannot be found.\n The program is now exiting."
            exit()
        else:
            self.height = str(height)
            self.width = str(width)
            self.framerate = str(framerate)+"/1"
            self.snap_format = str(snap_format)
            self.create_video_pipeline()

    def create_video_pipeline(self):
        #Set up the video pipeline and the communication bus bewteen the video stream and gtk DrawingArea """
        src = gst_src + self.device # video input
        src_format = gst_src_format +',width='+ str(self.width) + ',height=' + str(self.height) +',framerate='+ self.framerate # video parameters
        videosink = gst_videosink # video receiver
        video_pipeline = src + sep  + src_format + sep + videosink
        self.video_player = gst.parse_launch(video_pipeline) # create pipeline
        self.video_player.set_state(gst.STATE_PLAYING)       # start video stream

        bus = self.video_player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)
        bus.enable_sync_message_emission()
        bus.connect("sync-message::element", self.on_sync_message)

    def exit(self):
        """ Exit the program """
        self.video_player.set_state(gst.STATE_NULL)

    def on_message(self, bus, message):
        """ Gst message bus. Closes the pipeline in case of error or EOS (end of stream) message """
        t = message.type
        if t == gst.MESSAGE_EOS:
            print "MESSAGE EOS"
            self.video_player.set_state(gst.STATE_NULL)
            print "Error: %s" % err, debug
            self.video_player.set_state(gst.STATE_NULL)

    def on_sync_message(self, bus, message):
        """ Set up the Webcam <--> GUI messages bus """
        if message.structure is None:
            return
        message_name = message.structure.get_name()
        if message_name == "prepare-xwindow-id":
            # Assign the viewport
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(self.video_window.window.xid) # Sending video stream to gtk DrawingArea
