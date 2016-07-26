#!/usr/bin/env python

# Author: pr0n1s
# Description: Reads config.ini which contains the information needed to connect
# to my MySQL database
from configparser import ConfigParser

# Args: config.ini, and the section name located in config.ini
def read_config(file='config.ini', section='database'):
  # Setup a ConfigParser object
  parser = ConfigParser()
  # Read config.ini
  parser.read(file)
  db = {}
  # Check if the section(database) exists
  if parser.has_section(section):
    # items: dictionary of information located in config.ini
    items = parser.items(section)
    # Setting key value pairs in dictionary
    for item in items:
      db[item[0]] = item[1]
  else:
    raise Exception('{0} not fount in the {1} file'.format(section, file))
  # Return dictionary
  return db
