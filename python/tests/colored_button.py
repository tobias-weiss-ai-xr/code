#!/usr/bin/env python

import gtk

class ColoredButton(gtk.EventBox):
    '''
    This class implements a simple unanimated button 
    whose color can be changed
    '''

    def __init__(self, widget = gtk.Label()):
        '''
        widget must be a gtk.Label
        this is not checked in this simple version
        '''

        #initialize superclass EventBox
        super(ColoredButton, self).__init__()

        #embed widget inside vbox and hbox 
        self.widget = widget 
        self.vbox = gtk.VBox(homogeneous=False, spacing=0) 
        self.hbox = gtk.HBox(homogeneous=False, spacing=0)
        self.hbox.pack_start(self.vbox, expand = True, fill=False)
        self.vbox.pack_start(self.widget, expand = True, fill = False)

        #draws a frame around the entire construct to make everything look more like a button
        self.frame = gtk.Frame()
        self.frame.add(self.hbox)

        #add the final "button" to this EventBox in order to handle events
        self.add(self.frame)

        #define which events should be reacted to, those constants can be found in pygtk docs
        self.add_events(gtk.gdk.BUTTON_RELEASE_MASK)
        self.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.add_events(gtk.gdk.ENTER_NOTIFY_MASK)
        self.add_events(gtk.gdk.LEAVE_NOTIFY_MASK)

        #activate focus
        self.set_can_focus(True)

        #align the "button" text in the middle of the box
        self.widget.set_alignment(xalign=0.5, yalign=0.5)

    def show(self):
        super(ColoredButton, self).show()
        self.hbox.show()
        self.vbox.show()
        self.frame.show()
        self.widget.show()

    def set_label(self, label):
        self.set_text(label)

    def set_text(self, text):
        self.widget.set_text(text)

    def changeColor(self, color, state = gtk.STATE_NORMAL):
        if color is not None:
            currentcolor = self.style.bg[state]
            #too lazy to look up in docs if color != currentcolor also works
            if color.red != currentcolor.red or color.green != currentcolor.green or color.blue != currentcolor.blue:
                self.modify_bg(state, color)

    def changeTextColor(self, color, state = gtk.STATE_NORMAL):   
        if color is not None:
            currentcolor = self.style.bg[state]
            if color.red != currentcolor.red or color.green != currentcolor.green or color.blue != currentcolor.blue:
                self.widget.modify_fg(gtk.STATE_NORMAL, color)

def onButtonClick(widget, event = None):
    if event.button == 1:
        widget.set_label("left click")
    elif event.button == 2:
        widget.set_label("middle click")
    elif event.button == 3:
        widget.set_label("right click")

import gtk

w = gtk.Window()
w.connect('destroy', gtk.main_quit)

coloredbutton=ColoredButton(widget = gtk.Label("Hello there"))
coloredbutton.changeColor(gtk.gdk.color_parse("black"))
coloredbutton.changeTextColor(gtk.gdk.color_parse("yellow"))
coloredbutton.set_size_request(width = 100, height = 50)
coloredbutton.connect("button-release-event", onButtonClick)

w.add(coloredbutton)

w.show_all()
gtk.main()
