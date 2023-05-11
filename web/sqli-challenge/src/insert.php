<?php
include_once('./config.php');

$check_dup = 'drop table if exists `users`;';
if ($result = $conn->query($check_dup)) {
} else {
}
$create_table = '
create table `users` (
    id int not null auto_increment,
    username text not null,
    password text not null,
    primary key (id)
);';

if ($result = $conn->query($create_table)) {

    $sql = 'insert into `users` (username, password) values
    ("admin","HACKING_BRAWL{Inj3ct10n_achieved}")';

    if ($result = $conn->query($sql)) {
    } else {
        die("error");
    }
} else {
    echo "failed to create table";
}
