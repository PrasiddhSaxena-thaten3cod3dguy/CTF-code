<?php
// Initialize the session
session_start();
 
// Check if the user is already logged in, if yes then redirect him to welcome page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: welcome.php");
    exit;
}
 
// Define variables and initialize with empty values
$username = $password = "";
$username_err = $password_err = $login_err = "";
 
// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){
    if(empty($username_err) && empty($password_err)){// Password is correct, so start a new session
            $pass = $_POST['password'];
            $user = $_POST['username'];

            // Store data in session variables
            if($user == 'alpha' && $pass== 'butterfly')
            {
                session_start();
                http_response_code(200);
                $_SESSION["loggedin"] = true;
                $_SESSION["id"] ="HACKING_BRAWL{Bru73_C00k13}";
                $_SESSION["username"] = $username; 
                header("location: welcome.php");
            }                           

            // Redirect user to welcome page
            else{
                setcookie("username","alpha",24*24*6400);
                $password_err = "<h1 style='color:red;'>Wrong password.
                <br> Grab a cookie and try again!</h1>";
                http_response_code(403);
            }
    }
    
    // Close connection

}
?>
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
<div class="alert alert-danger"><?php echo $password_err;?></div>
</div>
</body>