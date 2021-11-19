$(document).ready(function(){

    content = $(".trending");
    buttons = $(".type-btn");

    buttons.each(function(index){
        $(this).on('click',function(){
            buttons.removeClass('active');
            $(this).addClass('active');
            content.removeClass('active');
            $(content[index]).addClass('active');
        })
    })
})