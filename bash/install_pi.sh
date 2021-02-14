#!/bin/bash

IP=10.1.0.104

cd -- # go home

mount /dev/mmcblk0p1 /mnt
echo "enable ssh" > /mnt/ssh
sed -i '1 s/$/ net.ifnames=0/' /mnt/cmdline.txt
sync
umount /mnt 

mount /dev/mmcblk0p2 /mnt
cat <<EOF >> /mnt/etc/dhcpcd.conf

# running static IP configuration:                                              
interface eth0                                                                  
static ip_address=$IP/24                                                 
#static ip6_address=fd51:42f8:caae:d92e::ff/64                                  
static routers=10.1.10.1                                                        
static domain_name_servers=10.1.0.1 8.8.8.8   
EOF
sync
umount /mnt 

