<?php

$alert = "<div class = 'alert alert-danger'>Sorry you can't access the dashboard</div>";
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