<?php
include_once('./insert.php');
?>

<html>
<?php
include_once('./cdn.php');
?>
<link href="./signin.css" rel="stylesheet">

<body class="text-center">
    <div class="container" id="showHere">
        <div class="row">
            <div class="col-md-12">
                <div class="p-5 text-center bg-image rounded-3" style="background-image: url('./syringe.jpg');height: 400px;">
                    <div class="mask" style="background-color: rgba(0, 0, 0, 0.6);">
                    </div>
                </div>
            </div>
            <form class="form-signin" action="./verify.php" method="POST" id="myform">
                <h1 class="h3 mb-3 font-weight-normal">Login</h1>
                <div class="form-group">
                    <label for="username" class="sr-only">username</label>
                    <input type="text" id="username" class="form-control" name="username" required>
                    <label for="password" class="sr-only">password</label>
                    <input type="password" id="password" class="form-control" name="password" required>
                    <button class="btn btn-lg btn-success btn-block" type="submit">Sign in</button>
                </div>
            </form>
        </div>
    </div>
</body>

</html>