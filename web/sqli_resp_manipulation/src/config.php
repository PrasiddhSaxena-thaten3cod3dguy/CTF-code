<?php
$host = 'db';

// Database use name
$user = 'admin';

//database user password
$pass = 'manipulator';

// database name
$mydatabase = 'hackershala';
// check the mysql connection status

$conn = new mysqli($host, $user, $pass, $mydatabase);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
}
