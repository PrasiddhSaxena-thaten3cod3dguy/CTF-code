$(document).ready(function() {
    $('#signup-form').on("submit", function(event) {
        $.ajax({
            data: {
                username: $('#username').val(),
                password: $('#password').val()
            },
            type: "POST",
            url: "/api/v1/user/create/527e3b6bf06f3d3358905af67c588b1ba621a8599b6010e1a0556632b3c5a2ee"
        })
        .done(function(data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else {
                $('#successAlert').text(data.msg).show();
                $('#errorAlert').hide();
            }
        });
        event.preventDefault();
    });
    $('#login-form').on("submit", function(event) {
        $.ajax({
            data: {
                username: $('#username').val(),
                password: $('#password').val()
            },
            type: "POST",
            url: "/api/v1/user/login/527e3b6bf06f3d3358905af67c588b1ba621a8599b6010e1a0556632b3c5a2ee"
        })
        .done(function(data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else if (data.msg == "ok") {
                window.location = "/";
            }
        });
        event.preventDefault();
    });
});