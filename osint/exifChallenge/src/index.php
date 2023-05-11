<?php
// Initialize the session
session_start();
$_SESSION['password'] = "dfhdfkhdfkjfdh";
// Check if the user is already logged in, if yes then redirect him to welcome page
if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
  header("location: welcome.php");
  exit;
}

// Include config file


// Define variables and initialize with empty values
$username = $password = "";
$username_err = $password_err = $login_err = "";

// Processing form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($username_err) && empty($password_err)) { // Password is correct, so start a new session
    $pass = $_POST['password'];
    $user = $_POST['username'];

    // Store data in session variables
    if ($user == 'h1dd3n_username' && $pass == '051n7_g33k') {
      session_start();
      $_SESSION["loggedin"] = true;
      $_SESSION['flag'] = "HACKING_BRAWL{EX1F_D4t4_1s_r15ky}";
      header("location: welcome.php");
    }

    // Redirect user to welcome page
    else {
      $password_err = "<h1 style='color:red'>Wrong password";
    }
  }

  // Close connection

}
?>
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" href="/docs/4.0/assets/img/favicons/favicon.ico">

  <title>Hackershala login</title>

  <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/sign-in/">

  <!-- Bootstrap core CSS -->
  <link href="./css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="./css/signin.css" rel="stylesheet">
</head>

<body class="text-center">
  <form class="form-signin" method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    <h1 class="h3 mb-3 font-weight-normal">Hackershala login</h1>
    <label for="inputEmail" class="sr-only">Username</label>
    <input type="text" name="username" id="inputEmail" class="form-control" placeholder="username" required autofocus>
    <label for="inputPassword" class="sr-only">Password</label>
    <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
    <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
    <button class="btn btn-lg btn-warning btn-block" type="submit"><a href="./forgot.php">Forgot password</a></button>
    <?php echo $password_err; ?>
    <p class="mt-5 mb-3 text-muted"><a href="./testimonial.php">Testimonials</a></p>
  </form>
</body>

</html>