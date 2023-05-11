<?php
$response['success'] = true;
if (isset($_POST['user']) && isset($_POST['pass'])) {
    // $flag = false;
    $user = $_POST['user'];
    $pass = $_POST['pass'];
    $pattern = "/true/i";
    $flag = preg_match($pattern, $user, $matches, PREG_OFFSET_CAPTURE);
    if ($flag) {
        $response['success'] = false;
    }
    $pattern = "/1=1/i";
    $flag = preg_match($pattern, $user, $matches, PREG_OFFSET_CAPTURE);
    if ($flag) {
        $response['success'] = false;
    }
    $pattern = "/true/i";
    $flag = preg_match($pattern, $user, $matches, PREG_OFFSET_CAPTURE);
    if ($flag) {
        $response['success'] = false;
    }
    $pattern = "/1=1/i";
    $flag = preg_match($pattern, $user, $matches, PREG_OFFSET_CAPTURE);
    if ($flag) {
        $response['success'] = false;
    }
    $pattern = "/true/i";
    $flag = preg_match($pattern, $pass, $matches, PREG_OFFSET_CAPTURE);
    if ($flag) {
        $response['success'] = false;
    }
    $pattern = "/1=1/i";
    $flag = preg_match($pattern, $pass, $matches, PREG_OFFSET_CAPTURE);
    if ($flag) {
        $response['success'] = false;
    }
}
echo json_encode($response);
