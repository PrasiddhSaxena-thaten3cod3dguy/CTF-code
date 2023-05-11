<html>
<?php
include_once('./cdn.php');
$alert = "";
$source = "";

if (isset($_GET['password']) && !empty($_GET['password'])) {
    $payload = $_GET['password'];
    if (md5($payload) == "9fd8301ac24fb88e65d9d7cd1dd1b1ec") {
        $alert = "<div class='alert alert-success'>HACKING_BRAWL{y0u_k33n_obs3rv3r}</div>";
    } else {
        $alert = "<div class='alert alert-danger'>No. Absolutely not. That's FALSE!!!</div>";
    }
}
if (isset($_GET['view-source']) && $_GET['view-source'] == 'true') {
    $source = "if(md5(password) == '9fd8301ac24fb88e65d9d7cd1dd1b1ec')
    {
        showFlag();}
    else
    {
        hideFlag();};";
}
?>

<body class="text-center">
    <div class="container" id="showHere">
        <div class="row">
            <div class="col-md-12 text-center">
                <?= $alert; ?>
            </div>
            <div class="col-md-12">
                <div class="p-5 text-center bg-image rounded-3" style="background-image: url('./true-false.webp');background-repeat: no-repeat;height:400px;background-position: center;">
                    <div class="mask" style="background-color: rgba(0, 0, 0, 0.6)" ;>
                    </div>
                </div>
            </div>
            <div class="col-md-12">
                <form class="form-signin" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="GET" id="myform">
                    <div class="input-group form-group">
                        <!-- <label for="search">Command cat to spill the secrets!</label> -->
                        <input type="search" id="search" name="password" class="form-control rounded" placeholder="Enter password to fetch flag" aria-label="Search" aria-describedby="search-addon" />
                        <input type='hidden' name='view-source' value='false'>
                        <button type="submit" class="btn btn-outline-primary">fetch</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <pre><?= $source ?></pre>
</body>

</html>