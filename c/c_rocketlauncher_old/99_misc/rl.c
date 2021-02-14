/* rl.c 
 * own rocketlauncher implementation 
 *
 * USB Missle launcher info:
 * id-product:  2123  -  0x2123
 * id-vendor:   1010  -  0x1010
 *
 */
#include <stdio.h>
#include <usb.h>

int main(void){
  struct usb_bus *busses;
  
  usb_init();
  usb_find_busses();
  usb_find_devices();
  
  busses = usb_get_busses();
  
      	struct usb_bus *bus;
    
  for (bus = busses; bus; bus = bus->next) {
  	struct usb_device *dev;
  
  	for (dev = bus->devices; dev; dev = dev->next) {
  		/* Check if this device is a printer */
  		if (dev->descriptor.idVendor == 0x2123){
  			/* Open the device, claim the interface and do your processing */
  			int a = usb_claim_interface(usb_device,1);
  			//libusb_set_debug(usb_bus,4);
  		}

  	}
  	
  }  	
  return 0;
}
