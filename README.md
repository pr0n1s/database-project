Author: pr0n1s (Robert Edstrom)
Project: SSH/Auth Log Analysis

Dependencies:
  
  auth.log's:
    All of the auth.log's need to be copied to the auth folder located in the root of the database-project directory. Example:
      /path/to/database-project/auth/auth.log's

  MySQL:
    - version 5.7.11
    - Make sure you update the config.ini with your database credentials (See below)

  Python:
    - MySQL connector:

      sudo dpkg -i dependency/mysql-connector-python_2.1.3-1ubuntu14.04_all.deb

      Note: if you use something different go to the following URL:
        
          https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html

    - GeoIP:
    
      apt-get install libgeoip-dev
      pip install GeoIP

  Apache2:
    sudo apt-get install apache2

    - Make sure the website directory contents are copied to /var/www/html
      Note: remove the default files in /var/www/html directory to /var/www

    - Open /etc/apache2/sites-available/000-default.conf
      - Make sure the following is in the above file:
        
          ServerName localhost
          ServerAdmin webmaster@localhost
          DocumentRoot /var/www/html
  
    - Open /etc/apache2/apache2.conf
      - Make sure the follow is in the above file around line 154
        Note: By no means is this a secure setup for Apache2

          <Directory />
            Options FollowSymLinks
            AllowOverride None
            Order deny,allow
            Allow from all
          </Directory>

          <Directory /usr/share>
            AllowOverride None
            Require all granted
          </Directory>

          <Directory /var/www/>
            Options Indexes FollowSymLinks
            AllowOverride None
            Require all granted
          </Directory>

    - Set permissions for the html directory located @ /var/www/html
      
        sudo chmod 0655 html/

    - Once you are sure the website is ready to go type:
        Note: Make sure the full/path/to/config.ini is set in the query.php script. Example:
          /root/home/name/database-project/scripts/config.ini

        sudo service mysql start
        sudo service apache2 start
  
      Note: make sure you type the following when you are done:
        
        sudo service apache2 stop

  config.ini:
    - Located in the scripts directory. Get's copied to /var/tmp when run.sh is executed.
      - Set the respective information to login to your MySQL server

  run.sh:
    - Located in the projects root directory
      Note: If webmaster@localhost doesn't work replace it with http://your-ip (last line in run.sh)

Run the BASH script: ./run.sh

Note: The, back-end, Python scripts are not dependent on where the root directory
      of the project is stored on your local machine. However, the website 
      directory contents are. Please, follow the Apache2 depency steps above. 
      If by any means you can't get the website to work with Apache2 please feel 
      free to contact me @ redstrom83@gmail.com.
