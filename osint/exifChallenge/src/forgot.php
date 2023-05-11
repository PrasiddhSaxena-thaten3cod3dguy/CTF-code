<?php
$password_result= "";
 
// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){
    if(empty($username_err) && empty($password_err)){// Password is correct, so start a new session
            $artist = $_POST['artist'];
            $user = $_POST['username'];

            // Store data in session variables
            if($user == 'h1dd3n_username' && $artist== 'andrew_symonds')
            {
                $password_result= "Password changed. New password is : '051n7_g33k'";
            }                           

            // Redirect user to welcome page
            else{
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

    <title>Reset password</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/sign-in/">

    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="./css/signin.css" rel="stylesheet">
  </head>

  <body class="text-center">
    <form class="form-signin" method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
      <h1 class="h3 mb-3 font-weight-normal">Reset password</h1>
      <label for="inputEmail" class="sr-only">Username</label>
      <input type="text" name="username" id="inputEmail" class="form-control" placeholder="username" required autofocus>
      <label for="artist" class="sr-only">Password</label>
      <input type="text" name="artist" id="artist" class="form-control" placeholder="favourite artist" required>
      <button class="btn btn-lg btn-primary btn-block" type="submit">Reset password</button>
      <button class="btn btn-lg btn-success btn-block" type="submit"><a style="color:white" href="./index.php">Login</button>
      <?php echo $password_result;?>
      <p class="mt-5 mb-3 text-muted"><a href="./testimonial.php">Testimonials</a></p>
    </form>
  </body>
</html>
