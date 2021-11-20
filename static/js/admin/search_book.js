$(document).ready(function() {
    form = $(".form-search-book");
    form.on("submit", function(){
        var info = $("input[name='info']")[0].value;
        var choose = $("select[name='choose']").find(":selected").val();
        var token = $('input[name="csrfmiddlewaretoken"]').val();
        if (info.trim() == "") {
            location.reload(true);
        } else {
            $.ajax({
                type : "GET",
                url : "/shelf",
                data : {
                    'info': info,
                    'choose': choose,
                    'csrfmiddlewaretoken': token,
                },
                dataType : 'json',
                success : function(response) {
                    var books = response.books;
                    html = "";
                    count = 0;
                    for (let book of books) {
                        count += 1;
                        html += "<tr style='white-space: pre; text-align: center;'>";
                        html += "<td>" + count + "</td>";
                        for (let i = 1; i < book.length-1; i++) {
                            html += "<td>" + book[i] + "</td>";
                        }
                        html += "</tr>"
                    }
                    $("#books tbody").html(html);
                }
            })
        }
        return false;
    })
    
})