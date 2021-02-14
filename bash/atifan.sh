#!/bin/bash

##
# atifan.sh v1.0
# by chort
##

# Which GPU device you're modifying. If you have only one GPU, it's 0
DEVICE=0

# If you have more than one GPU, change DISPLAY value to match the specific card
# :0.0 = device 1, :0.1 = device 2, :0.2 = device 3, etc.
# Cards with 2 GPUs (5970, 6990) might have two fans, which are treated as separate device
export DISPLAY=":0.${DEVICE}"

function usage {
        echo "Usage: $0 [get|set <%>]"
}

if [ -z "$1" ]
then  
        usage
fi

if [ X"$1" == "Xget" ]
then  
        aticonfig --pplib-cmd "get fanspeed 0"
        aticonfig --adapter=$DEVICE --odgt
fi

if [ X"$1" == "Xset" ]
then  
        if [ $2 -gt -1 2>/dev/null ] && [ $2 -lt 99 ]
        then  
                echo "Setting fanspeed to ${2}%"
                aticonfig --pplib-cmd "set fanspeed 0 $2"
                aticonfig --pplib-cmd "get fanspeed 0"
        else
                # Only values from 10% to 100% are valid
                usage
        fi
fi
