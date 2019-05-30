#!/bin/bash 

#--------------------------------------------
# name:vacuumgp.sh
# author：yichao
# date：2019-06-01
# description：vacuum significant bloated tables
# parameter:$1:dbname
#--------------------------------------------
database=$1

if [ $# -ne 1 ];then
        echo -e "Usage: ./vacuumgp.sh  < dbname > \n "
        echo -e "Example : ./vacuumgp.sh postgres"
        exit 8
fi

source /home/gpadmin/.bash_profile

date=`date +"%Y-%m-%d %H:%M:%S"` 
echo "begin time is: $date" >>/tmp/pg_vacuum.log 


tables=$(psql -d $database -c "select bdirelname from gp_toolkit.gp_bloat_diag order by bdirelpages desc, bdidiag;"|tail -n +3|grep -v "row") 
echo $tables >>/tmp/pg_vacuum.log 

for table in $tables 
do 
vacuumdb --analyze --table $table $database 
echo "table $table has finished vacuum.">>/tmp/pg_vacuum.log 
done 
