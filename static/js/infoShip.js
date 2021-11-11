
$(document).ready(function() {
    let order = $('.order_row');

    if(order.length == 0) {
        $('.empty-order').show();
        $('.history').hide();
    }

    order.each(function(index){
        $(this).find('.stt')[0].textContent = index+1;
    })
});