#/bin/bash

# Author: pr0n1s
# Description: Setup for python scripts by extracting data from the auth.logs,
# Copies the config.ini file to /var/tmp directory, run the python script dowork,
# and lastly opens the browser to the website

# Extracts data from the auth.log's
zgrep "Accepted password" auth/auth.log* | cut -d':' -f5 > files/accept.txt
zgrep ": Failed password for " auth/auth.log* | cut -d':' -f5 > files/failed.txt
zgrep "POSSIBLE BREAK" auth/auth.log* | cut -d':' -f5 > files/possible-breakin.txt

# Copies config.ini to /var/tmp dir
cp scripts/config.ini /var/tmp

# Runs to Python script dowork
cd scripts
python dowork.py

# Opens default browser
x-www-browser webmaster@localhost
