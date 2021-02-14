/* 
 * File:   yarl_movement.c
 * Desc:    Movement for YARL
 * Author: homaar
 * 
 *
 * Created on September 8, 2014, 2:28 AM
 */
#include "yarl_movement.h"
#include <time.h> // for nanosleep
#include <string.h> // for memset

void msleep(unsigned long milisec) {

    struct timespec req = {0};
    time_t sec = (int) (milisec / 1000);
    milisec = milisec - (sec * 1000);
    req.tv_sec = sec;
    req.tv_nsec = milisec * 1000000L;
    while (nanosleep(&req, &req) == -1)
        continue;
}

int action(libusb_device_handle *handle, unsigned char mov, double delay) {
    int r;
    //Movement array
    //Todo: use malloc() to get rid of the arrays for educational purpose
    unsigned char buf0[8], stopper[8];
    memset(buf0, 0, sizeof (buf0));
    buf0[0] = 2;
    // stopper
    memset(stopper, 0, sizeof (stopper));
    stopper[0] = 2;
    stopper[1] = 32;
    switch (mov) {
        case 'w':
            // up
            buf0[1] = 2;
            break;
        case 's':
            // down
            buf0[1] = 1;
            break;
        case 'a':
            // left
            buf0[1] = 4;
            break;
        case 'd':
            // right
            buf0[1] = 8;
            break;
        case 'f':
            //fire
            buf0[1] = 16;
            stopper[0] = 1;
            stopper[1] = 0;
            break;
        default:
            return -1;
    }

    r = libusb_control_transfer(handle, 0x21, 0x9, 0x200, 0, buf0, sizeof (buf0), 1000);
    msleep(delay);
    r = libusb_control_transfer(handle, 0x21, 0x9, 0x200, 0, stopper, sizeof (stopper), 1000);
    return r;
}

