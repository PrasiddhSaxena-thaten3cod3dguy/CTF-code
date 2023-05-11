<?php
$payload = "";
$pattern = '/script/i';

if (isset($_GET['q']) && !empty($_GET['q'])) {
  $payload = $_GET['q'];
  $payload = preg_replace($pattern, '', $payload);
  if ($payload == "<script>alert(document.cookie)</script>") {
    // session_start();
    setcookie("flag-value", "XSS_EV3Rywh3re", time() + 86400);
  }
  $payload = "You searched for - " . $payload;
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie shop</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" integrity="sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
  <div class="jumbotron jumbotron-fluid">
    <div class="container text-center">
      <h1>Welcome to </h1>
      <h1>Hackershala cookie shop!</h1>
    </div>
  </div>
  <div class="container">
    <div class="row gx-5">
      <div class="col-md-12">
        <div class="p-5 text-center bg-image rounded-3" style="background-image: url('./cookie.jpg');height: 400px;">
          <div class="mask" style="background-color: rgba(0, 0, 0, 0.6);">
            <div class="d-flex justify-content-center align-items-center h-100">
              <div class="text-white">
                <a class="btn btn-outline-light btn-lg" href="./coffee.html" role="button">Get free filter coffee!</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <form method="GET" action='<?php $_SERVER['PHP_SELF']; ?>'>
          <div class="input-group md-form form-sm form-1 pl-0">
            <div class="input-group-prepend">
              <span class="input-group-text pink lighten-3" id="basic-text1"><i class="fas fa-search text-white" aria-hidden="true"></i></span>
            </div>
            <input class="form-control my-0 py-1" type="text" name='q' placeholder="Search" aria-label="Search">
          </div>
        </form>
      </div>
    </div>
  </div>

  <?= $payload ?>
</body>

</html>