$(document).ready(function() {
    $('table').on('click','tbody tr', function (evt) {
        var $cell=$(evt.target).closest('td');
        if($cell.index() > 0) {
            window.location.href = $(this).data('link');
        }
    });
});
