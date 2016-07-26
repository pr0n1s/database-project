#!/usr/bin/env python

# Author: pr0n1s
# Description: Connects to the MySQL database 'auth', and inserts all of the
# parsed data from all of the auth.logs

import parse
import database
import database_insert

# accept: default dictionary of type list. Username is the key, and the value is
# a list of the users ip and total count per ip.
accept = parse.accept()
# accept_factory: list of lists of a default dictionary of lists of which includes
# another dictionary of Geo-IP information of the respective users ip/s.
accept_factory = parse.user_list(accept)
# kiddies: default dictionary of type list. Username is the key, and the value is
# a list of the users ip and total count per ip.
kiddies = parse.possible_breakin()
# kiddies_factory: list of lists of a default dictionary of lists of which includes
# another dictionary of Geo-IP information of the respective users ip/s.
kiddies_factory = parse.user_list(kiddies)
# failed: default dictionary of type list. Username is the key, and the value is
# a list of the users ip and total count per ip.
failed = parse.failed()
# failed_factory: list of lists of a default dictionary of lists of which includes
# another dictionary of Geo-IP information of the respective users ip/s.
failed_factory = parse.user_list(failed)
# conn: MySQL connection object
conn = database.connect()
# Create the database tables
database.create_tables(conn)

# Unpack the kiddies_factory
for wtf in kiddies_factory:
  # ip_count: dictionary of key(users ip), value(total count of users ip)
  ip_count = wtf[1][0].items()
  # Unpack ip_count dictionary
  for ip, count in ip_count:
    # Getting SQL statement to insert into ScriptKiddies
    sql = database_insert.kiddies()
    # Setup a cursor to execute SQL statements
    cursor = conn.cursor()
    # kiddy: tuple of values to be substituted into the SQL statement
    # wtf[0].strip(): username
    # ip: users ip
    # count: total count of each users ip per ip
    kiddy = (wtf[0].strip(), ip, count, wtf[0].strip())
    # Insert all data into ScriptKiddies
    cursor.execute(sql, kiddy)
    # Commit the entries
    conn.commit()
# Close the cursor
cursor.close()

# Unpack the accept_factory
for wtf in accept_factory:
  # ip_count: dictionary of key(users ip), value(total count of users ip)
  ip_count = wtf[1][0].items()
  # Unpack ip_count dictionary
  for ip, count in ip_count:
  # Getting SQL statements to insert into the Users, Inets, and SuccessLogins tables
    users, inets, mapping = database_insert.success()
    print('Table: {} inserting\n'.format('Users'))
    # user: tuple of values to be substituted into the SQL statement for Users
    # wtf[0]: username
    user = (wtf[0], wtf[0])
    # Setup a cursor to execute SQL statements
    cursor = conn.cursor()
    # Insert all data into Users
    cursor.execute(users, user)
    # Commit the entries
    conn.commit()
    print('Table: {} inserting\n'.format('Inets'))
    # inet: tuple of values to be substituted into the SQL statement for Inets table
    # ip: the users ip
    # wtf[2][ip]['latitude']: latitude per users ip per ip
    # wtf[2][ip]['longitude']: longitude per users ip per ip
    # wtf[2][ip]['country_name']: country per users ip per ip
    inet = (ip, wtf[2][ip]['latitude'], wtf[2][ip]['longitude'], wtf[2][ip]['country_name'], ip)
    # Insert all data into Inets table
    cursor.execute(inets, inet)
    # Commit the entries
    conn.commit()
    print('Table: {} inserting\n'.format('SuccessLogins'))
    # mapp: tuple of values to be substituted into the SQL statement for SuccessLogins
    # count: total count per ip
    # wtf[0]: username
    # ip: users ip
    mapp = (count, wtf[0], ip)
    # Insert all data into SuccessLogins
    cursor.execute(mapping, mapp)
    # Commit the entries
    conn.commit()
# Close cursor
cursor.close()

# Unpack failed_factory:
for wtf in failed_factory:
  # ip_count: dictionary of key(users ip), value(total count of users ip)
  ip_count = wtf[1][0].items()
  # Unpack ip_count dictionary
  for ip, count in ip_count:
    # Getting SQL statements to insert into the Users, Inets, and FailLogins tables
    users, inets, mapping = database_insert.fail()

    print('Table: {} inserting\n'.format('Users'))
    # wtf[0]: username
    user = (wtf[0], wtf[0])
    # Setup a cursor to execute SQL statements
    cursor = conn.cursor()
    # Insert all data into Users
    cursor.execute(users, user)
    # Commit the entries
    conn.commit()
    print('Table: {} inserting\n'.format('Inets'))
    # inet: tuple of values to be substituted into the SQL statement for Inets table
    # ip: the users ip
    # wtf[2][ip]['latitude']: latitude per users ip per ip
    # wtf[2][ip]['longitude']: longitude per users ip per ip
    # wtf[2][ip]['country_name']: country per users ip per ip
    inet = (ip, wtf[2][ip]['latitude'], wtf[2][ip]['longitude'], wtf[2][ip]['country_name'], ip)
    # Insert all data into Inets
    cursor.execute(inets, inet)
    # Commit the entries
    conn.commit()
    print('Table: {} inserting\n'.format('FailLogins'))
    # mapp: tuple of values to be substituted into the SQL statement for FailLogins
    # count: total count per ip
    # wtf[0]: username
    # ip: users ip
    mapp = (count, wtf[0], ip)
    # Insert all data into FailLogins
    cursor.execute(mapping, mapp)
    # Commit the entries
    conn.commit()
# Close cursor
cursor.close()
