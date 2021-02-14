#!/bin/bash
clear
echo "introduce la cantidad de minutos"
read c
for  b in $(seq 1 $c)
do
for a in $(seq 1 60)
do
let u=60-$a
let  v=$c-$b
echo "$v:$u"
sleep 1
clear
done
done
echo  Tiempo!!!
