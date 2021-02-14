/* 
 * File:   yarl_usb.c
 * Desc:   USB for YARL
 * Author: homaar
 * 
 *
 * Created on September 8, 2014, 2:28 AM
 */
#include <stdio.h>
#include <libusb.h> // for device handle

void getLibusbVersion(void) {
    const struct libusb_version* version;
    version = libusb_get_version();
    printf("Using libusbx v%d.%d.%d.%d\n\n", version->major, version->minor, version->micro, version->nano);
}
