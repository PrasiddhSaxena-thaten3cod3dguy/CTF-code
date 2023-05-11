<?php
include_once('./insert.php');
?>

<html>
<?php
include_once('./cdn.php');
?>
<link href="./signin.css" rel="stylesheet">

<body class="text-center">
    <div id="showHere"></div>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="p-5 text-center bg-image rounded-3" style="background-image: url('./manip.png');height: 400px;">
                    <div class="mask" style="background-color: rgba(0, 0, 0, 0.6);">
                    </div>
                </div>
            </div>
            <form class="form-signin" action="verify.php" method="POST" id="myform">
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
    <script>
        var flag = true;

        function setFlag(x) {
            flag = x;
            // alert(flag)
        }
        $("#myform").submit(function() {
            let formData = new FormData()
            formData.append("user", $("#username").val());
            formData.append("pass", $("#password").val());
            $.ajax({
                url: 'check.php',
                data: formData,
                type: 'POST',
                contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
                processData: false,
                success: function(response) {
                    $("#showHere").empty();
                    response = JSON.parse(response)
                    var flg = response['success'];
                    setFlag(flg);
                    if (!response['success']) {
                        var msg = "<div class='alert alert-danger'>Potential payload detected</div>";
                        $("#showHere").append(msg);
                    }
                },
                error: function(data) {
                    setFlag(false);
                }
            })
            // console.log(response);

            confirm("Are you sure?");
            return flag;

        });
    </script>
</body>

</html>