#!/bin/bash

user=$(find /var/spool/mail/ -size +600M -exec ls -lah "{}" ";" | cut -d" " -f 3)

for element in $(seq 0 $((${#user[@]}-1)))
do

#echo -n "${user[$element]}"
echo ${#user[@]}
#echo -n "Das Postfach ${user[$element]} hat die Warnschwelle von 750 MB ueberschritten. Ihr Postfach droht voll zu laufen. Bitte loeschen sie alte Mails" |  mutt -s "Postfach droht voll zu laufen" j.pfau@dreher.de
done

