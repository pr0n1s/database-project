#!/usr/bin/env python

# Description: Returns SQL statement to insert into the ScriptKiddies(noobs) table.
def kiddies():
  noobs = """INSERT INTO ScriptKiddies
           (hostname, ip, ip_count)
           SELECT * FROM (SELECT %s, %s, %s) AS tmp
           WHERE NOT EXISTS (SELECT hostname FROM ScriptKiddies
           WHERE hostname=%s)"""
  return noobs

# Description: Returns SQL statements to insert into the Users(users), Inets(inets)# and SuccessLogins(mapping) tables.
def success():
  users = """INSERT INTO Users (username) 
             SELECT * FROM (SELECT %s) AS tmp WHERE NOT EXISTS 
             (SELECT username FROM Users WHERE username=%s)"""
  
  inets = """INSERT INTO Inets (ip, lat, log, country)
             SELECT * FROM (SELECT %s, %s, %s, %s) AS tmp
             WHERE NOT EXISTS (SELECT ip FROM Inets WHERE ip=%s)"""

  mapping = """INSERT INTO SuccessLogins (user_id, ip_id, ip_total)
               SELECT user_id, ip_id, (SELECT * FROM (SELECT %s) AS tmp)
               FROM Users, Inets WHERE Users.username=%s AND Inets.ip=%s"""
  return users, inets, mapping

# Description: Returns SQL statements to insert into the Users(users), Inets(inets)
# and FailLogins(mapping) tables.
def fail():
    users = """INSERT INTO Users (username) 
               SELECT * FROM (SELECT %s) AS tmp WHERE NOT EXISTS 
               (SELECT username FROM Users WHERE username=%s)"""
                                
    inets = """INSERT INTO Inets (ip, lat, log, country)
               SELECT * FROM (SELECT %s, %s, %s, %s) AS tmp
               WHERE NOT EXISTS (SELECT ip FROM Inets WHERE ip=%s)"""

    mapping = """INSERT INTO FailLogins (user_id, ip_id, ip_total)
                 SELECT user_id, ip_id, (SELECT * FROM (SELECT %s) AS tmp)
                 FROM Users, Inets WHERE BINARY Users.username=%s AND Inets.ip=%s"""
    return users, inets, mapping
