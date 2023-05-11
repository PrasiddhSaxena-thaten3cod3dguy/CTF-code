<html>
<?php
include_once('./cdn.php');
$alert = "";

if (isset($_POST['command']) && !empty($_POST['command'])) {
    $payload = $_POST['command'];
    if ($payload == "cat flag.txt") {
        $alert = "<div class='alert alert-success'>HACKING_BRAWL{ev3ry1_l0v3s_ki77y}</div>";
    } else {
        $alert = "<div class='alert alert-danger'>Kitty.txt isn't impressed. Try harder!!</div>";
    }
}
?>
<div class="jumbotron">
    <h1 class="display-4">Agent kitty!!</h1>
    <p class="lead">She knows all the secrets but won't reveal unless you utter the right command.</p>
    <hr class="my-4">
    <p>Look around and see if you can come up with the right command.</p>
</div>

<body class="text-center">
    <div class="container" id="showHere">
        <div class="row">
            <div class="col-md-12 text-center">
                <?= $alert; ?>
            </div>
            <div class="col-md-12">
                <div class="p-5 text-center bg-image rounded-3" style="background-image: url('./kitty.jpg');background-repeat: no-repeat;height:400px;background-position: center;">
                    <div class="mask" style="background-color: rgba(0, 0, 0, 0.6)" ;>
                    </div>
                </div>
            </div>
            <div class="col-md-12">
                <form class="form-signin" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" id="myform">
                    <div class="input-group form-group">
                        <!-- <label for="search">Command cat to spill the secrets!</label> -->
                        <input type="search" id="search" name="command" class="form-control rounded" placeholder="ask" aria-label="Search" aria-describedby="search-addon" />
                        <button type="submit" class="btn btn-outline-primary">Ask</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>

</html>