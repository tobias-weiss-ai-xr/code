# /etc/dirtrockers_backup.conf
##########################################
# hier werden alle zu sichernden Datein mit vollstaendigem Pfad angegeben.
# Verzeichnisnamen oder Dateinamen sind okay (in Verzeichnisse wird ab -
# gestiegen)
#
### dirt rockers ###
/var/www/dirt-rockers/htdocs/
##########################################

cs15-smt:/var/www/dirt-rockers/backup# cat /usr/local/backup/dirtrockers_backup.sh 
# /usr/local/backup/dirtrockers_backup.sh
#####
# SMT DATA Communications GmbH
# Lehmgrubenweg 8
# 78727 Oberndorf/N - Germany
# Tel.: 07423/810997-20
# Fax: 074237810997-22
#
# Script for making a gzipped tar-ball
# and pushing it anywhere by using mutt-email-client
#
# For security reasons we changed the gzipped tar-archive into a
# password secured zip-archive
#
#####################

##### Config #####
DATE=$(date +%d_%m_%Y)
CONFIG_FILE=/etc/dirtrockers_backup.conf
BACKUP_PATH=/var/www/dirt-rockers/backup
BACKUP_FILE=backup_dirtrockers_$DATE.tar
BACKUP_USER=1008516
TMP_OUT=/tmp/backup_$DATE.tmp
HOME=/root/
export HOME=$HOME
MYSQL_USER=1008516
MYSQL_PW=pJ97781J
MYSQL_DB=mag_dirtrockers
##################

############################

##### Main #####
rm -rf $BACKUP_PATH/*

mysqldump -u $MYSQL_USER -p$MYSQL_PW $MYSQL_DB > $BACKUP_PATH/$MYSQL_DB_$DATE.sql

if [ ! -d $BACKUP_PATH ] ; then mkdir -p $BACKUP_PATH ; fi
sed -e '/^$/d' -e '/^#/d' $CONFIG_FILE > $TMP_OUT
tar -T $TMP_OUT -cf $BACKUP_PATH/$BACKUP_FILE
zip -P nd8PvFk45 $BACKUP_PATH/$BACKUP_FILE.zip $BACKUP_PATH/$MYSQL_DB_$DATE.sql $BACKUP_PATH/$BACKUP_FILE
rm -f $BACKUP_PATH/$BACKUP_FILE $BACKUP_PATH/$MYSQL_DB_$DATE.sql
chown $BACKUP_USER:$BACKUP_USER $BACKUP_PATH/*
rm $TMP_OUT
################