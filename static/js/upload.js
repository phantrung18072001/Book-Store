$(".btn-upload").on('click', function() {
    let parent = $(this).closest('.form-upload');
    let input = parent.find("input[type='file']");
    input.click();
    input[0].addEventListener('change', function() {
        const input_reader = new FileReader();
        input_reader.addEventListener('load', () => {
          uploaded = input_reader.result;
          $(".avatar")[0].src = `${uploaded}`;
        });
        input_reader.readAsDataURL(this.files[0]);
    });
});