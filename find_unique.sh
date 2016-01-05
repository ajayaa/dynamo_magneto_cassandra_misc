DB_USER=root
DB_PASS=123
databases=`mysql -u$DB_USER -p$DB_PASS -e "show databases;"`
for db in keystone
do
    echo "Inspecting tables of db $db"
    tables=`mysql -u$DB_USER -p$DB_PASS -e "use $db; show tables;"`
    #echo "tables: $tables"
    for table in $tables
    do
        t_schema=`mysql -u$DB_USER -p$DB_PASS -e "use $db; show create table $table"`
        if [[ $t_schema =~ .*UNIQUE.* ]]
        then
            echo "-$table: $t_schema" | sed "s/UNIQUE/$(tput setaf 1)UNIQUE$(tput sgr0)/"
        fi

    done
done
