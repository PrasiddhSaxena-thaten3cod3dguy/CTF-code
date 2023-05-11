<?php
session_start();
if (isset($_SESSION["loggedin"])) {
    if (isset($_SESSION['role'])) {
        if ($_COOKIE['role'] == 'user') {
            echo "Only admin can see the flag";
        } else if ($_COOKIE['role'] == 'admin') {
            echo "HACKING_BRAWL{adm1n_pr1l1v1g3s_ftw}";
        }
    }
} else {
    echo "wrong password";
    session_destroy();
    header("location:index.php");
}
