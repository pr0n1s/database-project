#!/user/bin/env python

# Author: pr0n1s
# Description: This is my database schema

# Description: Returns a dictionary of SQL statements to create the tables
# for the database 'auth' when called.
def table_factory():
  tables = {}
  tables['Users'] = (
    "CREATE TABLE IF NOT EXISTS `Users` ("
    " `user_id` int(5) NOT NULL AUTO_INCREMENT,"
    " `username` varchar(50) NOT NULL,"
    " PRIMARY KEY `pk_Users`(`user_id`))")
  
  tables['Inets'] = (
    "CREATE TABLE IF NOT EXISTS `Inets` ("
    " `ip_id` int(5) NOT NULL AUTO_INCREMENT,"
    " `ip` varchar(15) NOT NULL,"
    " `lat` decimal(20, 17) NOT NULL,"
    " `log` decimal(20, 17) NOT NULL,"
    " `country` varchar(30) NOT NULL,"
    " PRIMARY KEY `pk_Inets`(`ip_id`))")
  
  tables['SuccessLogins'] = (
    "CREATE TABLE IF NOT EXISTS `SuccessLogins` ("
    " `user_id` int(5) NOT NULL,"
    " `ip_id` int(5) NOT NULL,"
    " `ip_total` int(5) NOT NULL," 
    " PRIMARY KEY (`user_id`, `ip_id`))")

  tables['FailLogins'] = (
    "CREATE TABLE IF NOT EXISTS `FailLogins` ("
    " `user_id` int(5) NOT NULL,"
    " `ip_id` int(5) NOT NULL,"
    " `ip_total` int(5) NOT NULL,"
    " PRIMARY KEY (`user_id`, `ip_id`))")
  
  tables['ScriptKiddies'] = (
    "CREATE TABLE IF NOT EXISTS `ScriptKiddies` ("
    " `id` int(5) NOT NULL AUTO_INCREMENT,"
    " `hostname` varchar(55) NOT NULL,"
    " `ip` varchar(15) NOT NULL,"
    " `ip_count` int(5) NOT NULL,"
    " PRIMARY KEY (`id`))")
  return tables
