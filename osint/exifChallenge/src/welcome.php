<?php
    session_start();
    if(isset($_SESSION["loggedin"]))
    {
        echo "<h1 style='align:center; color:red'> Your flag is ".$_SESSION["flag"]."</h1>";
    }
    else
    {
        header("location:index.php");
    }
?>
