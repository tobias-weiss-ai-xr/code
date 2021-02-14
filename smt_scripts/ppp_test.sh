#!/bin/sh

if ! [ -e /var/lock/ppp_test ] ; then
        touch /var/lock/ppp_test

        /sbin/ifconfig ppp0
        result="$?"
        while [ $result -ne 0 ] ; do
                logger "DSL Reconnect"
                killall -9 ifup ifdown pppd
                ifdown dsl-provider
                ifup dsl-provider
                sleep 5
                /sbin/ifconfig ppp0
                result="$?"
        done

        #result_vpn=$(ifconfig tun0 | grep "inet addr" | cut -c 21-28)
        #echo $result_vpn
        #if [ "$result_vpn" = "10.10.11" ]
        #then
        #  result_nc=$(nc 109.193.254.9 1190 -u -vvz | grep open)
        #  if [ "$result_vpn" != "" ]
        #  then
        #    logger "VPN Restart"
        #    /etc/init.d/openvpn restart
        #  fi
        #fi
        rm /var/lock/ppp_test
fi
exit 0

