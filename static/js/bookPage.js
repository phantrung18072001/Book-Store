
$(document).ready(function() {
    if ($('input[name="success"]').val()) {
        $("#overlay").css({ "display": "block" });
        $("#popup").css({ "display": "block" });
    }
    $('.clearfix .submitbtn').on('click', function() {
        $("#overlay").css({ "display": "none" });
        $("#popup").css({ "display": "none" });
    });
    $('.view-cart').click(function() {
        $('.cart-interface').show(500);
    })

    let bookQuantity = Number($(".quantity")[0].textContent);
    $('.book-btn-sub').click(function() {
        $('.book-num-input').val(parseInt($('.book-num-input').val()) - 1);
        if ($('.book-num-input').val() <= 1) {
            $('.book-num-input').val(1);
        }
    })
    $('.book-btn-add').click(function() {
        $('.book-num-input').val(parseInt($('.book-num-input').val()) + 1);
        if ($('.book-num-input').val() >= bookQuantity) {
            $('.book-num-input').val(bookQuantity);
        }
    })
    $('.book-num-input').keyup(function() {
        this.value = this.value.replace(/[^0-9\.]/g, '');
    });
    $('.book-num-input').blur(function() {

        if ($(this).val() == "") {
            $(this).val(1);
        }
        if (parseInt($(this).val()) >= bookQuantity) {
            $(this).val(bookQuantity);
        }
        if (parseInt($(this).val()) <= 1) {
            $(this).val(1);
        }
    })

    let listImg = $('.list-img');
    let mainImg = $('.book-main-img img');

    function load(cur) {
        listImg.removeClass('active');
        cur.addClass('active');
        mainImg.attr('src', cur.attr('src'));
    }

    load($(listImg[0]));

    listImg.each(function(index) {
        $(this).click(function() {
            load($(this));
            console.log($(this))
        })
    })

    $('.close').click(function() {
        $('.slider-view-img').fadeOut(500);
    })
    /* $('.header__notify-header #readed').on('click', function() {
        let id = $(this).attr('attr-id');
        let data = {
            id: id
        }
        axios.post('/user/alert/readed', data).then(res => {
            if (res.data.success) {
                $('.header__notify-item').each(function() {
                    $(this).addClass("bg-readed");
                    $(this).removeClass("bg-not-read");
                })
                $('#count-alert').css('display', 'none');
            } else {
                alert('Lỗi hệ thống, không thể thực hiện!');
            }
        }).catch(err => {
            alert('Lỗi hệ thống, không thể thực hiện!');
        })
    }); */
});
