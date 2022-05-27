#!/bin/bash
:: check for python if its installed into linux
checkPython(){
if which python3 > /dev/null 2>&1;
then
	runCRON()
else
	sudo apt install python3-pip
}

:: run cron job
runCRON(){
chmod 777 ./dataset_cleaning.py
crontab -e
0 1 * * * dataset_cleaning.py
}

checkPython()