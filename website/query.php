<!DOCTYPE html>

<!-- Author: pr0n1s  
     Description: Querys the database based on the value received from the Ajax
     request and then echo's a table filled with information from the query into the
     div id 'query' on the website.
-->

<html>
<head>
  <link href="css/pr0n1s.css" rel="stylesheet">
</head>
<body>
<?php
  # path: path/to/config.ini
  $path = "/var/tmp/config.ini";
  # q: value received from the Ajax request
  $q = intval($_GET['q']);
  # config: MySQL database credentials
  $config = parse_ini_file($path);
  # Connect to the MySQL database
  $conn = new mysqli($config['host'], $config['user'], $config['password'], $config['database']);
  
  # Switch statement to check the value of 'q'
  switch($q){
    # If q equals 1
    case 1:
      # results: result from the SQL query for Top successful logins
      $results = $conn->query("SELECT u.username, i.ip, i.country, s.ip_total, i.lat, i.log FROM Users u INNER JOIN SuccessLogins s ON s.user_id=u.user_id INNER JOIN Inets i ON s.ip_id=i.ip_id ORDER BY s.ip_total DESC");
      # Send the results to dowork function
      dowork($results);
      break;
    # If q equals 2
    case 2:
      # results: result from the SQL query for Top failed logins
      $results = $conn->query("SELECT u.username, i.ip, i.country, f.ip_total, i.lat, i.log FROM Users u INNER JOIN FailLogins f ON f.user_id=u.user_id INNER JOIN Inets i ON f.ip_id=i.ip_id ORDER BY f.ip_total DESC");
      # Send results to dowork function
      dowork($results);
      break;
    # If q equals 3
    case 3:
      # results: result from the SQL query for Script Kiddies
      $results = $conn->query("SELECT u.username, i.ip, i.country, f.ip_total, i.lat, i.log FROM Users u INNER JOIN FailLogins f ON f.user_id=u.user_id INNER JOIN Inets i ON f.ip_id=i.ip_id INNER JOIN ScriptKiddies s WHERE s.ip=i.ip ORDER BY f.ip_total DESC");
      # Send results to dowork function
      dowork($results);
      break;
    # If q equals 4
    case 4:
      # results: result from the SQL query for Top Countries
      $results = $conn->query("SELECT i.country, SUM(f.ip_total) AS total FROM FailLogins f INNER JOIN Inets i ON f.ip_id=i.ip_id INNER JOIN Inets ii WHERE i.country=ii.country GROUP BY i.country ORDER BY total DESC");
      # Send results to topCountries function
      topCountries($results);
      break;
    # If q equals 5
    case 5:
      # results: result from the SQL query for Top Successful Logins by Ip
      $results = $conn->query("SELECT i.ip, SUM(s.ip_id) AS total FROM SuccessLogins s INNER JOIN Inets i ON s.ip_id=i.ip_id GROUP BY i.ip ORDER BY total DESC");
      # Send results to topSuccessByIps function
      topSuccessByIps($results);
      break;
    # If q equals 6
    case 6:
      # results: result from the SQL query for Top Failed Login Attemps by Ip
      $results = $conn->query("SELECT i.ip, SUM(f.ip_id) AS total FROM FailLogins f INNER JOIN Inets i ON f.ip_id=i.ip_id GROUP BY i.ip ORDER BY total DESC");
      # Send results to topFailByIps function
      topFailByIps($results);
      break;
    # If q equals 7
    case 7:
      # results: result from the SQL query for Top Successful Logins By User
      $results = $conn->query("SELECT u.username, SUM(s.ip_total) AS total FROM Users u INNER JOIN SuccessLogins s ON u.user_id=s.user_id GROUP BY u.username ORDER BY total DESC");
      # Send results to topSuccessByUser function
      topSuccessByUser($results);
      break;
    # If q equals 8
    case 8:
      # results: result from the SQL query for Top Failed Login Attempts by User
      $results = $conn->query("SELECT u.username, SUM(f.ip_total) AS total FROM Users u INNER JOIN FailLogins f ON u.user_id=f.user_id GROUP BY u.username ORDER BY total DESC");
      # Send results to topFailByUser function
      topFailByUser($results);
      break;
  }
  
  # Arg: results from SQL queries: Top Successful Logins, Top Failed Logins, and ScriptKiddies
  # Description: create table from the possible results returned from the queries metioned above
  function dowork($results){
    # Echo table and table header into the 'query' id
    echo "<table id='table'>
    <tr>
    <th>Username</th>
    <th>Ip</th>
    <th>Country</th>
    <th>Logins</th>
    <th>Latitude</th>
    <th>Longitude</th>
    </tr>";
    # Iterate through the returned rows
    while($row = $results->fetch_assoc()){
      # Echo table row with data filled in into the 'query' id
      echo "<tr>";
      echo "<td>" . $row['username'] . "</td>";
      echo "<td>" . $row['ip'] . "</td>";
      echo "<td>" . $row['country'] . "</td>";
      echo "<td>" . $row['ip_total'] . "</td>";
      echo "<td>" . $row['lat'] . "</td>";
      echo "<td>" . $row['log'] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
  }

  # Arg: result from SQL query for Top Countries
  # Description: create table from the Top Countries query
  function topCountries($results){
    # Echo table and table header into the 'query' id
    echo "<table>
    <tr>
    <th>Country</th>
    <th>Total Login Attempts</th>
    </tr>";
    # Iterate through the returned rows
    while($row = $results->fetch_assoc()){
      # Echo table rows with data filled in into the 'query' id
      echo "<tr>";
      echo "<td>" . $row['country'] . "</td>";
      echo "<td>" . $row['total'] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
  }

  # Arg: result from the SQL query for Top Countries
  # Description: create table from the Top Successful Logins by Ip
  function topSuccessByIps($results){
    # Echo table and table header into the 'query' id
    echo "<table>
    <tr>
    <th>Ip</th>
    <th>Total Successful Logins by Ip</th>
    </tr>";
    # Iterate through the returned rows
    while($row = $results->fetch_assoc()){
      # Echo table rows with data filled in into the 'query' id
      echo "<tr>";
      echo "<td>" . $row['ip'] . "</td>";
      echo "<td>" . $row['total'] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
  }

  # Arg: result from the SQL query for Top Failed Login Attempts by Ip
  # Descripton: create table from the Top Failed Login Attempts by Ip
  function topFailByIps($results){
    # Echo table and table header into the 'query' id
    echo "<table>
    <tr>
    <th>Ip</th>
    <th>Total Failed Login Attempts by Ip</th>
    </tr>";
    # Iterate through the returned rows
    while($row = $results->fetch_assoc()){
      # Echo table rows with data filled in into the 'query' id
      echo "<tr>";
      echo "<td>" . $row['ip'] . "</td>";
      echo "<td>" . $row['total'] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
  }
  
  # Arg: results: result from the SQL query for Top Successful Logins by User
  function topSuccessByUser($results){
    # Echo table and table header into the 'query' id
    echo "<table>
    <tr>
    <th>Username</th>
    <th>Total Success Logins by User</th>
    </tr>";
    # Iterated through the returned rows
    while($row = $results->fetch_assoc()){
      # Echo table rows with data filled in into the 'query' id
      echo "<tr>";
      echo "<td>" . $row['username'] . "</td>";
      echo "<td>" . $row['total'] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
  }

  # Arg: results: result from the SQL query for Top Failed Login Attempts by User
  function topFailByUser($results){
    # Echo table and table header into the 'query' id
    echo "<table>
    <tr>
    <th>Username</th>
    <th>Total Failed Login Attempts by User</th>
    </tr>";
    # Iterate through the returned rows
    while($row = $results->fetch_assoc()){
      # Echo table rows with data filled in into the 'query' id
      echo "<tr>";
      echo "<td>" . $row['username'] . "</td>";
      echo "<td>" . $row['total'] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
  }
  # Close connection to MySQL
  $conn->close();
?>
</body>
</html>
