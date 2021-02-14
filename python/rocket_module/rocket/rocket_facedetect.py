#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os

class rocketFacedetect(object):
    def __init__(self):
        cascPath = os.path.abspath(os.path.dirname(__file__) + '/../data/haarcascade_frontalface_default.xml')
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
        # convert from RGB to GBR
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # get size information
        height, width, nChannels = rgb_image.shape
        return rgb_image, height, width, nChannels
