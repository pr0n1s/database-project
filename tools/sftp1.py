#!/usr/bin/env python

# Author: pr0n1s
# Description: Connects to the ssh server and copies files to the users local
# machine. Note: This was created for only remote to local copying. As it was
# created to assist in the development of my database project.

import paramiko
import os

# This doesn't change unless your connecting to a diff host
host = ''
# Put your username
username = ''
# Put your password FYI... remove password when finished with the script
password = ''
# This doesn't change
port = 22

# Description: Prompting the user to enter the path/to/file on the remote 
# server. Next, prompting user to enter the path/to/dir on their local machine
def get_input():
  # List of path/to/files on the remote server
  remote_file_list = []
  while(True):
    print("\n[*] Enter the /path/to/file on the remote server")
    # Prompting user for remote path/to/file
    fn = raw_input("[*] /path/to/file: ")
    # Checking if user is done
    if fn == 'done':
      break
    # Checking if user needs help
    elif fn == 'help':
      help()
    # Storing remote path/to/file
    remote_file_list.append(fn)

  print("\n[*] Enter the local directory you want the files stored")
  # Prompting user for the local directory they want the files stored
  local_dir = raw_input("[*] local directory: ")
  # Return list, string
  return remote_file_list, local_dir

# Args: list, string
# Description: creates the local files on the users machine based
# on the input given by the user.
def create_local_file(remote_file_list, local_dir):
  # List of path/to/users/dir
  local_file_list = []
  for f in remote_file_list:
    # Remove forward slashes
    fn = f.split('/')
    # Concat path/to/users/dir with a '/' and the filename the user
    # wants from the remote server.
    tmp = local_dir + '/' + fn[len(fn)-1]
    # Store the path/to/users/dir/filename
    local_file_list.append(tmp)

  for lf in local_file_list:
    # Check if file already exists
    if os.path.exists(lf):
      print 'File {} exists'.format(lf)
    # Create file if it doesn't exist
    else:
      open(lf, 'w')
      print 'File {} created'.format(lf)
  # Return list, list
  return remote_file_list, local_file_list

# Description: Help the user/print shit
def help():
  print("[*] Type 'help' to display the help menu")
  print("[*] Step 1: Enter /path/to/file you wish to copy")
  print("[*] Step 2: Type 'done' when you are done")

# Args: remote of type list, and local of type list
# Description: Connects to the ssh server and copies the files to the
# users local directory
def dowork(remote, local):
  # Setup an SSH Transport
  tp = paramiko.Transport((host, port))
  # Negoiate a session and authenticate with the SSH server
  tp.connect(username=username, password=password)
  # Setup a SFTP session
  sftp = paramiko.SFTPClient.from_transport(tp)
  for rfp in remote:
    for lfp in local:
      # Copy the remote file to the users local directory
      sftp.get(rfp, lfp)
  # Close the SFTP session
  sftp.close()
  # Close the SSH Transport
  tp.close()
  print("Done transfering files")

# Description: main function which executes the script
def main():
  # Help needed?
  help()
  # Getting the path/to/the/remote/files and the users local directory
  remote_file_list, local_dir = get_input()
  # Getting the path/to/the/remote/files again and this time the
  # path/to/user/local/dir
  remote, local = create_local_file(remote_file_list, local_dir)
  # Now the magic happens
  dowork(remote, local)

# Boiler code...
if __name__ == '__main__':
  main()
