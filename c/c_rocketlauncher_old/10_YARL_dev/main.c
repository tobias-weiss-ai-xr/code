#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libusb.h>
#include <time.h>
#include <unistd.h>
#include <termios.h>
#include <unistd.h>
#define usb_interface interface

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

void msleep(unsigned long milisec) {
    //use nanosleep for movement
    struct timespec req = {0};
    time_t sec = (int) (milisec / 1000);
    milisec = milisec - (sec * 1000);
    req.tv_sec = sec;
    req.tv_nsec = milisec * 1000000L;
    while (nanosleep(&req, &req) == -1)
        continue;
}

void getLibusbVersion(void) {
    const struct libusb_version* version;
    version = libusb_get_version();
    printf("Using libusbx v%d.%d.%d.%d\n\n", version->major, version->minor, version->micro, version->nano);
}

int fire(unsigned char *buf0, unsigned char *stopper) {
    int r;
    buf0[0] = 2;
    buf0[1] = 16;
    stopper[0] = 1;
    stopper[1] = 0;
    r = libusb_control_transfer(handle, 0x21, 0x9, 0x200, 0, buf0, sizeof (buf0), 1000);
    msleep(10);
    r = libusb_control_transfer(handle, 0x21, 0x9, 0x200, 0, stopper, sizeof (stopper), 1000);
    return r;
}

int action(unsigned char mov) {
    int r;
    //Movement array
    //Todo: use malloc() to get rid of the arrays for educational purpose
    unsigned char buf0[8], stopper[8];
    memset(buf0, 0, sizeof (buf0));
    switch (mov) {
        case 'w':
            // up
            buf0[0] = 2;
            buf0[1] = 2;
            break;
        case 's':
            // down
            buf0[0] = 2;
            buf0[1] = 1;
            break;
        case 'a':
            // left
            buf0[0] = 2;
            buf0[1] = 4;
            break;
        case 'd':
            // right
            buf0[0] = 2;
            buf0[1] = 8;
            break;
        case 'f':
            //fire
            // runs flawless as own function but not in main... obscure!
            r = fire(buf0, stopper);
            return r;
        default:
            return -1;
    }
    memset(stopper, 0, sizeof (stopper));
    // stop
    stopper[0] = 2;
    stopper[1] = 32;
    r = libusb_control_transfer(handle, 0x21, 0x9, 0x200, 0, buf0, sizeof (buf0), 1000);
    msleep(10);
    r = libusb_control_transfer(handle, 0x21, 0x9, 0x200, 0, stopper, sizeof (stopper), 1000);
    return r;
}

int main(int argc, char** argv) {
    int debug_level = 0;
    char mov = 'u';
    int r, i;

    vid = (uint16_t) 0x2123;
    pid = (uint16_t) 0x1010;

    r = libusb_init(NULL);
    libusb_set_debug(0, debug_level);
    if (r < 0)
        return r;

    //Opening device
    handle = libusb_open_device_with_vid_pid(NULL, vid, pid);
    if (handle == NULL) {
        printf("  Failed.\n");
        return -1;
    }

    dev = libusb_get_device(handle);
    bus = libusb_get_bus_number(dev);
    libusb_set_auto_detach_kernel_driver(handle, 1);


    //Claiming interface
    r = libusb_claim_interface(handle, 0);
    if (r != LIBUSB_SUCCESS) {
        printf("   Failed.\n");
    }

    char input;
    while ((input = getch()) != 'q') {
        //Send data
        r = action(input);
    }

    //Releasing interface
    r = libusb_release_interface(handle, 0);

    //Closing device
    libusb_close(handle);

    libusb_exit(NULL);

    return r;
}