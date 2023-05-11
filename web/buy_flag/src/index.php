<?php
// $str['name'] = 'aamir';
// $str['age'] = 22;
// $resp = json_encode($str);
// $resp = base64_encode($resp);
// echo $resp;
// echo "\n";
// $resp = base64_decode($resp);
// echo $resp;
?>
<html lang="en">

<head>
    <title>Flag shop</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
    <input type='hidden' id='hash' value='eyJiYWxhbmNlIjowLCJjb3N0IjoxMH0='>
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Flag-Kart</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Home</a></li>
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#">Page 1 <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Page 1-1</a></li>
                            <li><a href="#">Page 1-2</a></li>
                            <li><a href="#">Page 1-3</a></li>
                        </ul>
                    </li>
                    <li><a href="#">Page 2</a></li>
                    <li><a href="#">Page 3</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Balance</li>
                    <li><i class="fa fa-dollar" style="font-size:48px;color:red">0</i><a href="#"></a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        <h2>Flag of destiny</h2>
        <div class="card" style="width:400px">
            <img class="card-img-top" src="peace.jpg" alt="Card image" style="width:100%">
            <div class="card-body">
                <h4 class="card-title"><i class="fa fa-dollar" style="font-size:48px;color:red">10</i></h4>
                <button class='btn btn-success' id='buy'>Buy flag </button>
                <span class="spinner-border spinner-border-sm"></span>
            </div>
        </div>
        <br>
        <div class="loader" id="loader"></div>
        <div id="result"></div>
    </div>

    <script>
        $("#buy").click(function() {
            let formData = new FormData()
            formData.append("hash", $("#hash").val());
            $.ajax({
                url: 'buy.php',
                data: formData,
                type: 'POST',
                contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
                processData: false,
                success: function(response) {
                    $("#result").empty();
                    var msg = JSON.parse(response);
                    $("#result").append(msg['message']);
                },
                error: function(data) {}
            })
            // console.log(response)

        })
    </script>

</body>

</html>