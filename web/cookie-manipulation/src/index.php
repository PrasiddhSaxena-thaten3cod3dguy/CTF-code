<?php

// Check if the user is already logged in, if yes then redirect him to welcome page
if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
    header("location: welcome.php");
    exit;
}

// Define variables and initialize with empty values
$username = $password = "";
$test_ps = $test_user = "";
$alert = "";
// Processing form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") { // Password is correct, so start a new session
    $pass = $_POST['password'];
    $user = $_POST['username'];

    // Store data in session variables
    if ($user == 't357_user' && $pass == 'l0gm31n') {
        session_start();
        http_response_code(200);
        $_SESSION["loggedin"] = true;
        $_SESSION["role"] = "user";
        $_SESSION["username"] = $username;
        setcookie("role", "user", time() + 86400);
        header("location: welcome.php");
    }

    // Redirect user to welcome page
    else {
        $test_ps = "l0gm31n";
        $test_user = "t357_user";
        $alert = "<div class='alert alert-success'>
                            Use following credentials to login<br>
                            username:" . $test_user . '<br>password:' . $test_ps .
            "</div>
                         </div>";
    }

    // Close connection

}
?>
<html>

<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>

<body>
    <div class="container" id="showHere">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" id="myform">
            <div class="form-group">
                <label for="username">username</label>
                <input type="text" id="username" class="form-control" name="username">
                <label for="password">password</label>
                <input type="password" id="password" class="form-control" name="password">
                <button type="submit">Login </button>
            </div>
        </form>
        <?php echo $alert; ?>
</body>

</html>