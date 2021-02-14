#!/usr/bin/env python

import sys
import os
import pygst
import gst
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

class rocketCam:
    def __init__(self):
        #  read config
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'defaults.cfg'))
        # is a webcam plugged in
        self.device = config.get('camera', 'device')
        if not os.path.exists(self.device):
            print("No webcam detected: {}  cannot be found.\n The program is now exiting.".format(self.device))
            exit()
        else:
            self.height = str(config.get('camera', 'height'))
            self.width = str(config.get('camera', 'width'))
            self.framerate = str(config.get('camera', 'framerate'))+"/1"
            self.gst_src = config.get('gstreamer', 'gst_src').strip("'")
            self.gst_src_format = config.get('gstreamer', 'gst_src_format').strip("'")
            self.gst_videosink = config.get('gstreamer', 'gst_videosink').strip("'")
            self.sep = config.get('gstreamer', 'sep').strip("'")
            self.create_video_pipeline()

    def create_video_pipeline(self):
        #Set up video pipeline and communication bus bewteen the video stream and gtk DrawingArea
        src = self.gst_src + self.device # video input
        src_format = self.gst_src_format +',width='+ self.width + ',height=' + self.height +',framerate='+ self.framerate # video parameters
        videosink = self.gst_videosink # video receiver
        video_pipeline = src + self.sep  + src_format + self.sep + videosink
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
            print("MESSAGE EOS")
            self.video_player.set_state(gst.STATE_NULL)
            print("Error: %s" % err, debug)
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

