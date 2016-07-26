#!/usr/bin/env python

# Step 1: put your whole project in one directory
# Step 2: tar -zcvf outputfile foldertocompress

import paramiko
import os

host = ''
port = 22
# Put your username for Dr. Neel's server
username = ''
# Put your password for Dr. Neel's server
password = ''
# Put your remote directory on Dr. Neel's server
remote_dir = ''
# Put your local path/to/project 
local_file = ''

# Setup a Transport
tp = paramiko.Transport((host, port))
# Negotiate an SSH session
tp.connect(username=username, password=password)
# Setup a SFTP session
sftp = paramiko.SFTPClient.from_transport(tp)
# Copies the local file to the remote dir
sftp.put(local_file, remote_dir)
# Close the SFTP session
sftp.close()
# Close the Transport
tp.close()
