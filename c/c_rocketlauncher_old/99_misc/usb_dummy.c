/* rl1.c 
 * own rocketlauncher implementation 
 *
 * USB Missle launcher info:
 * id-product:  2123  -  0x2123
 * id-vendor:   1010  -  0x1010
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <usb.h>
int main(){
    usb_init();
    printf("Hello world!\n");
    return 0;
}
