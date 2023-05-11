<?php
if (isset($_POST['username']) && !empty($_POST['username'])) {

    $user = $_POST['username'];
    $pass = $_POST['password'];
    $alert = "";
    if ($user == 'admin' && $pass == 'admin') {
        $alert = ' <a href="./secret.txt" download> <button class="btn"><i class="fa fa-download"></i> Download your flag</button></a>';
    } else {
        $alert = '<div class="alert alert-danger">You do not seem to be aware of the default credentials</div>';
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <?php include_once('./cdn.php'); ?>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Add icon library -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .btn {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 30px;
            cursor: pointer;
            font-size: 20px;
        }

        .btn:hover {
            background-color: RoyalBlue;
        }
    </style>
</head>

<body>

    <h2>Holaaaa!!!!!!!</h2>
    <?= $alert ?>

</body>

</html>