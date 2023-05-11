<?php
include_once('./config.php');
if (isset($_POST['username']) && !empty($_POST['username'])) {

    $user = $_POST['username'];
    $pass = $_POST['password'];

    $alert = "";

    $verify = "SELECT username from users WHERE username = '$user' and password = '$pass'";
    if ($result = $conn->query($verify)) {
        if (mysqli_num_rows($result)) {
            $alert = "<div class='alert alert-success'>HACKING_BRAWL{SQLi_with0ut_3rr0r}</div>";
        } else {
            $alert = "<div class = 'alert alert-danger'>Wrong password mate !</div>";
        }
    } else {
        echo "request failed";
    }
}
?>
<html>
<?php include_once('./cdn.php'); ?>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-8">
                <?= $alert; ?>
            </div>
            <div class="col-md-6">
                <button class="btn btn-danger"><a style="color:white;" href="./index.php">Go back</a></button>
            </div>
        </div>
    </div>
</body>

</html>