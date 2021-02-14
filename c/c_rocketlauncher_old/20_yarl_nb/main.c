#include <stdio.h>
#include <stdlib.h>
#include <libusb.h>
#include <unistd.h>
#include <termios.h>
#include <unistd.h>
#include "yarl_movement.h"
#define usb_interface interface // for compatibility with new libusb versions

static uint16_t vid, pid;
libusb_device_handle *handle;
libusb_device *dev;
uint8_t bus;

static struct termios new_io;
static struct termios old_io;

/* Funktion schaltet das Terminal in den cbreak-Modus:        */
/* Kontrollflag ECHO und ICANON auf 0 setzen                  */
/* Steuerzeichen: Leseoperation liefert 1 Byte VMIN=1 VTIME=1 */
int cbreak(int fd) {
    /*Sichern unseres Terminals*/
    if ((tcgetattr(fd, &old_io)) == -1)
        return -1;
    new_io = old_io;
    /* Wir verändern jetzt die Flags für den cbreak-Modus. */
    new_io.c_lflag = new_io.c_lflag & ~(ECHO | ICANON);
    new_io.c_cc[VMIN] = 1;
    new_io.c_cc[VTIME] = 0;

    /*Jetzt setzen wir den cbreak-Modus*/
    if ((tcsetattr(fd, TCSAFLUSH, &new_io)) == -1)
        return -1;
    return 1;
}

int getch(void) {
    int c;

    if (cbreak(STDIN_FILENO) == -1) {
        printf("Fehler bei der Funktion cbreak ... \n");
        exit(EXIT_FAILURE);
    }
    c = getchar();
    /* alten Terminal-Modus wiederherstellen */
    tcsetattr(STDIN_FILENO, TCSANOW, &old_io);
    return c;
}

int main(int argc, char** argv) {
    int debug_level = 0;
    double delay = 5;
    char mov = 'u';
    int r, i;

    vid = (uint16_t) 0x2123;
    pid = (uint16_t) 0x1010;

    //Init Libusb
    r = libusb_init(NULL);
    libusb_set_debug(0, debug_level);
    if (r < 0)
        return r;

    //Opening device
    handle = libusb_open_device_with_vid_pid(NULL, vid, pid);
    if (handle == NULL) {
        printf("Opening device failed.\n");
        return -1;
    }

    libusb_set_auto_detach_kernel_driver(handle, 1);


    //Claiming interface
    r = libusb_claim_interface(handle, 0);
    if (r != LIBUSB_SUCCESS) {
        printf(" Claiming interface failed.\n");
    }

    char input;
    while ((input = getch()) != 'q') {
        //Send data
        r = action(handle, input, delay);
    }
    r = action(handle, 'w', 500);
    r = action(handle, 'a', 500);
    r = action(handle, 's', 500);
    r = action(handle, 'd', 500);
    

    //Releasing interface
    r = libusb_release_interface(handle, 0);

    //Closing device
    libusb_close(handle);

    libusb_exit(NULL);

    return r;
}