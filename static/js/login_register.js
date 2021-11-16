
$(document).ready(function() {

    $('.login-btn').on('click', function() {
        window.location.href = "/user/login";
    })
    $('.register-btn').on('click', function() {
        window.location.href = "/user/register";
    })
    $('.profile-btn').on('click', function() {
        window.location.href = "/user/profile";
    })
    
    $('input[name="phone"]').keyup(function() {
        this.value = this.value.replace(/[^0-9\.]/g, '');
    });

    if ($('.register input[name="success"]').val()) {
        $(".register #overlay").css({ "display": "block" });
        $(".register #popup").css({ "display": "block" });
        $(".register .form-box").css({ "display": "none" });
    }
})