<?php
    session_start();
    if(isset($_SESSION["loggedin"]))
    {
        echo $_SESSION["id"];
    }
    else
    {
        echo "wrong password";
    }
?>