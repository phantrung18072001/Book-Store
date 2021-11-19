$(".btn-upload").on('click', function() {
    let parent = $(this).closest('.form-upload');
    let input = parent.find("input[type='file']");
    input.click();
});