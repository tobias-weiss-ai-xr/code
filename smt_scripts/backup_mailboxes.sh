#!/bin/bash

LOCAL=/mnt/dasi
SHARE=//192.168.0.251/dasi$
BACKUP_PATH=/var/spool/mail
#BACKUP_PATH=/tmp
USER=storagecraft
PASSWORD=TRP%cag6

MOUNT=$(which mount)
UMOUNT=$(which umount)
ZIP=$(which gzip)
MKDIR=$(which mkdir)
TOUCH=$(which touch)
POSTFIX=/etc/init.d/postfix


$MOUNT -t smbfs -o username=$USER,password=$PASSWORD $SHARE $LOCAL
if [ "$(df | grep $LOCAL)" ]; then
  DIR="Sicherung_$(date "+%Y-%m-%d")"
  LOG="backup_$(date "+%Y-%m-%d").log"
  $MKDIR -p $LOCAL/$DIR
  echo -e "$(date "+%d-%m-%Y")\t$(date "+%H:%M:%S")\tBackup Job hat begonnen......" > $LOCAL/$DIR/$LOG 
  $POSTFIX stop
else
  echo "Fehler"
  exit 0
fi


for i in `find $BACKUP_PATH/ -name "*"`; do

   echo -e "$(date "+%d-%m-%Y")\t$(date "+%H:%M:%S")\tSicherung von $i wird gestartet...." >> $LOCAL/$DIR/$LOG
   FILE=$(basename $i)
   $ZIP -c $BACKUP_PATH/$FILE > $LOCAL/$DIR/$FILE.gz
   if [ $? -ne 0 ]
	then
	echo -e "$(date "+%d-%m-%Y")\t$(date "+%H:%M:%S")\tBackup $i ist fehlgeschlagen" >> $LOCAL/$DIR/$LOG
	else
	echo -e "$(date "+%d-%m-%Y")\t$(date "+%H:%M:%S")\tBackup $i war erfolgreich" >> $LOCAL/$DIR/$LOG
	fi

done
echo -e "$(date "+%d-%m-%Y")\t$(date "+%H:%M:%S")\tBackup Job ist beendet" >> $LOCAL/$DIR/$LOG
$POSTFIX start
$UMOUNT $LOCAL

exit 0





