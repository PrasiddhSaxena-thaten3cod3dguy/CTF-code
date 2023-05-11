<?php
$alert = "";
if (isset($_POST['command']) && !empty($_POST['command'])) {
    $alert = "<div class='alert alert-danger'>No noob attempts. The secret is under my robot's protection at locker number - <b>i4dSV</b> </div>";
}
?>
<html lang="en">

<head>
    <title>The Ghost</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php include_once('./cdn.php'); ?>
</head>
<div class="jumbotron">
    <h1 class="display-4">BINny the GHOST</h1>
    <p class="lead">A deadly ghost knows the secrets to all your problems. The secret is hidden in a place inaccessible to humans.</p>
    <hr class="my-4">
    <p>Can you find it??</p>
</div>

<body class="text-center">
    <div class="container" id="showHere">
        <div class="row">
            <div class="col-md-12 text-center">
                <?= $alert; ?>
            </div>
            <div class="col-md-12">
                <div class="p-5 text-center bg-image rounded-3" style="background-image: url('./ghost.png');background-repeat: no-repeat;height:400px;background-position: center;">
                    <div class="mask" style="background-color: rgba(0, 0, 0, 0.6)" ;>
                    </div>
                </div>
            </div>
            <div class="col-md-12">
                <form class="form-signin" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" id="myform">
                    <div class="input-group form-group">
                        <!-- <label for="search">Command cat to spill the secrets!</label> -->
                        <input type="search" id="search" name="command" class="form-control rounded" placeholder="ask" aria-label="Search" aria-describedby="search-addon" />
                        <button type="submit" class="btn btn-outline-primary">Cast spell</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>

</html>