#!/bin/bash

for((i=1; i<254;i++))
do
  nmap -sT -PN 93.$i.1-254.2-253 -n -p80 --open -v -T3 | grep "Discovered open port" | cut -d" " -f6 >> /pentest/testhosts
  echo $i
done
