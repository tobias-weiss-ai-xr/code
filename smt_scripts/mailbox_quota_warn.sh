#!/bin/bash

PFAD=/var/spool/mail/
# Warnschwelle in Prozent (15 = 15% unter der Gesamtgoesse)
WARN=20

for i in `find $PFAD -name "*"`; do

   # Eigentuemer der Datei ermitteln
   USER=$(stat -c %U $i);

   # Dateigroesse in Byte ermitteln
   SIZE=$(stat -c %s $i);

   # max. Mailboxgoesse aus /etc/postfix/main.cf ermitteln
   MAXMAILBOX=$(grep "mailbox_size_limit" /etc/postfix/main.cf | cut -d "=" -f 2);

   # Warnschwelle berechnen
   ((TEMP1=(($MAXMAILBOX*$WARN)/100)));
   ((ALARM=$MAXMAILBOX-$TEMP1));

   # Vergleiche Dateigroesse mit Warnschwelle
   if [ $SIZE -ge $ALARM ]
   then
      ((SIZEMB=$SIZE/1048576))
      ((ALARMMB=$ALARM/1048576))
      mutt -s "Postfachwarnung $USER@dreher.de | Groesse: $SIZEMB MB | Warnschwelle: $ALARMMB MB" $USER@dreher.de,internet@dreher.de < /usr/local/scripts/mailbox_warn_message.txt
      
      if [ -r /var/log/mail.warn ]
      then
         DATE=$(date)
         echo "$DATE Benutzer $USER hat die Warnschwelle ueberschritten die aktuelle Dateigoesse betraegt $SIZEMB MB eine Warnmeldung wurde gesendet" >> /var/log/mail.warn
      fi 
   fi
done
