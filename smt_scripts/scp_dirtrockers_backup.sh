# 
#####
# SMT DATA Communications GmbH
# Lehmgrubenweg 8
# 78727 Oberndorf/N - Germany
# Tel.: 07423/810997-20
# Fax: 074237810997-22
#####################

##### Config #####

##################
scp 1008516@cs15-smt.de:/var/www/dirt-rockers/backup/* /srv/backup/dirt-rockers/
find /srv/backup/dirt-rockers -mtime 7 -type f -exec rm {} \;