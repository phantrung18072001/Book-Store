(function($) {
  'use strict';
  $(function() {
    $('.file-upload-browse').on('click', function() {
      var file = $(this).parent().parent().parent().find('.file-upload-default');
      file.trigger('click');
    });
    $('.file-upload-default').on('change', function() {
      $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
    });
  });
})(jQuery);

const FrontCover = document.querySelector("#FrontCover");
const BackCover = document.querySelector("#BackCover");
var uploaded_FrontCover;
var uploaded_BackCover;

FrontCover.addEventListener('change', function() {
  const FrontCover_reader = new FileReader();
  FrontCover_reader.addEventListener('load', () => {
    uploaded_FrontCover = FrontCover_reader.result;
    document.querySelector("#displayFrontCover").style.backgroundImage = `url(${uploaded_FrontCover})`;
  });
  FrontCover_reader.readAsDataURL(this.files[0]);
  document.getElementById("FrontCover_Image").setAttribute("value", this.files[0])
});

BackCover.addEventListener('change', function() {
  const BackCover_reader = new FileReader();
  BackCover_reader.addEventListener('load', () => {
    uploaded_BackCover = BackCover_reader.result;
    document.querySelector("#displayBackCover").style.backgroundImage = `url(${uploaded_BackCover})`;
  });
  BackCover_reader.readAsDataURL(this.files[0]);
  document.getElementById("BackCover_Image").setAttribute("value", this.files[0])
});