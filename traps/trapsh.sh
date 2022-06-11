#!/bin/sh
read host
read ip
vars=
while read oid val
do
	if [ "$vars" = "" ]
	then
		vars="$oid = $val"
	else
		vars="$vars, $oid = $val"
	fi
done
echo trap: $1 $host $ip $vars >> /var/log/traps_logs.txt
python3 traps_parser.py
