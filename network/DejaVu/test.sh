#!/bin/bash

file=pwd_$RANDOM
mkdir /tmp/key
cat /root/pwd.txt > /tmp/key/$file

var=`cat /tmp/key/$file`
if [ -z "$var" ]
then
      echo "Pwd is stolen"
else
      echo "All good"
fi

rm -rf /tmp/key