#!/bin/bash

for z in `find ~ -type f -name *.old`
do
	echo -e "\nDie Datei $z kann vermutlich gelöscht werden"
done
