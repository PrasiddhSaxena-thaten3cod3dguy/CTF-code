<?php
$message = "<div class='alert alert-danger'>Insufficient balance. Recharge and try again ! </div>";
$response['message'] = $message;
if (isset($_POST['hash']) && !empty($_POST['hash'])) {
    $str = base64_decode($_POST['hash']);
    $str = json_decode($str);
    if ($str->balance >= $str->cost) {
        $response['message'] = "<div class='alert alert-success'>You have earned your flag -> HACKING_BRAWL{base64_why??}</div>";
    }
    echo json_encode($response);
}
