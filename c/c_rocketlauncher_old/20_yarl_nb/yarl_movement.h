/* 
 * File:   yarl_movement.h
 * Author: homaar
 *
 * Created on September 8, 2014, 2:28 AM
 */
#include <libusb.h> // for device handle

#ifndef YARL_MOVEMENT_H
#define	YARL_MOVEMENT_H

#ifdef	__cplusplus
extern "C" {
#endif

void msleep(unsigned long milisec); //use nanosleep for movement duration
int action(libusb_device_handle *handle, unsigned char mov, double delay);



#ifdef	__cplusplus
}
#endif

#endif	/* YARL_MOVEMENT_H */

