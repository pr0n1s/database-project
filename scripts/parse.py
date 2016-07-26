#!/usr/bin/env python

# Author: pr0n1s
# Description: Parses the auth.log's and calculates the total number of times
# each users ip connected or tried to connect to the SSH server. In addition to
# getting the Geo-location data of each ip per user.

import GeoIP, sys
from collections import defaultdict, Counter

# Description: reads the file accept.txt and extracts the username and ip's
# associated with that username
def accept():
  # accept_dic: default dictionary of type list
  accept_dic = defaultdict(list)
  try:
    # fh: file handler object 
    fh = open('../files/accept.txt', 'r')
  except:
    print '[*] File: accept.txt not found!'
    sys.exit()
  # Reading one line at a time of accept.txt
  for line in fh:
    # line: list of each line splitted on spaces and stripped of newlines
    line = line.strip().split()
    # Setting key(username) and value(list of ip's respective to username)
    accept_dic[line[3]].append(line[5])
  # Close file handler
  fh.close()
  # Return dictionary as arg to count_ip
  return count_ip(accept_dic)

# Description:: reads the file failed.txt and extracts the username and ip's
# associated with that username
def failed():
  # failed_dic: default dictionary of type list
  failed_dic = defaultdict(list)
  try:
    # fh: file handler object
    fh = open('../files/failed.txt', 'r')
  except:
    print '[*] File: failed.txt not found!'
    sys.exit()
  # Reading one line at a time of failed.txt
  for line in fh:
    # Check if '127.0.0.1' is not in the line read
    if '127.0.0.1' not in line:
      # Check if 'invalid' is in the line
      if 'invalid' in line:
        # line: list of each line splitted on spaces and stripped of newlines
        line = line.strip().split()
        # Checking if index 7 of the list is equal to 'from'
        if line[7] == 'from':
          # Setting key(username) and value(list of ip's respective to username)
          failed_dic[line[5]].append(line[8])
        # 'from' is not in the line
        else:
          # Check if index 5 of the list is equal to 'from'
          if line[5] == 'from':
            # Setting key(username) and value(list of ip's respective to username)
            failed_dic[line[4]].append(line[6])
          # 'from' not in the line
          else:
            # Setting key(username) and value(list of ip's respective to username)
            failed_dic[line[5]].append(line[7])
      # 'invalid' not in the line
      else:
        # line: list of each line splitted on spaces and stripped of newlines
        line = line.strip().split()
        # Setting key(username) and value(list of ip's respective to username)
        failed_dic[line[3]].append(line[5])
  # Close file handler
  fh.close()
  # Return dictionary as arg to count_ip
  return count_ip(failed_dic)

# Description: reads the file possible-breaking.txt and extracts the host and ip
def possible_breakin():
  # kiddies: default dictionary of type list
  kiddies = defaultdict(list)
  try:
    # fh: file handler object
    fh = open('../files/possible-breakin.txt', 'r')
  except:
    print '[*] File: possible-breakin.txt not found!'
    sys.exit()
  # Reading one line at a time from possible-breakin.txt
  for line in fh:
    # Check if line starts with ' reverse'
    if line.startswith(' reverse'):
      # Temporary holder for each line
      tmp = line
      # ip: ip from each line
      ip = line.split('[')[1].split(']')[0]
      # host: host from each line
      host = tmp.split('for')[1].split('[')[0]
      # Setting key(host) and value(list of ip's respective to host)
      kiddies[host].append(ip)
    # Line does not start with ' reverse'
    else:
      # Check if line starts with ' Address'
      if line.startswith(' Address'):
        # ip: ip from each line
        ip = line.split(' ')[2]
        # host: host from each line
        host = line.split(' ')[5].replace(',', '')
        # Setting key(host) and value(list of ip's respective to host)
        kiddies[host].append(ip)
  # Close file handler
  fh.close()
  # Return default dictionary of type list as arg to count_ip
  return count_ip(kiddies)

# Arg: default dictionary of type list
def count_ip(dic):
  # accept_dict: default dictionary of type list
  accept_dic = defaultdict(list)
  # Unpacking dictionary
  for key, item in dic.items():
    # Setting key(user/host) and value(list of dictionary(key(ip) and value(count))
    accept_dic[key].append(Counter(item))
  # Return default dictionary of type list
  return accept_dic

# Arg: list of ip's
# Description: gets the Geo-Location of each ip
def get_geolocation(lst):
  # gi: handler for GeoLiteCity database
  gi = GeoIP.open("../files/GeoLiteCity.dat", GeoIP.GEOIP_INDEX_CACHE | 
  GeoIP.GEOIP_CHECK_CACHE)
  # rip: dictionary
  rip = {}
  # Iterating through the list of ip's
  for ip in lst:
    # Setting key(ip) and value(dictionary of Geo-location data respective to ip)
    rip[ip] = gi.record_by_name(ip)
  # Return list
  return rip

# Arg: default dictionary of type list
# Description: Stores each user and their data in a list
def user_list(dic):
  # rip: list
  rip = []
  # Iterating through arg dic key and values
  for key, item in dic.items():
    # Iterating through ip_list key and values
    for ip_list in item:
      # Unpacking dictionary thereby returning a list of keys(ip's)
      ip_list = ip_list.keys()
      # Appending a list of users and their data
      rip.append([key, item, get_geolocation(ip_list)])
  # Return a list of lists of a dictionary of lists... etc. lol... fun shit!
  return rip
  
