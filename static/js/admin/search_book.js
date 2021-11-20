$(document).ready(function() {
    var form = $(".form-search-book");
    var return_first;
    function callback(response) {
        return_first = response;
        books = return_first.books;
        html = "";
        count = 0;
        for (let book of books) {
            count += 1;
            html += "<tr class='clickable-row' style='white-space: pre; text-align: center;'>";
            html += "<td>" + count + "</td>";
            html += "<td style='display: none;'>" + book[0] + "</td>";
            for (let i = 1; i < book.length-1; i++) {
                html += "<td>" + book[i] + "</td>";
            }
            html += "</tr>"
        }
        $("#books tbody").html(html);
    }



    form.on("submit", function(){
        var info = $("input[name='info']")[0].value;
        var choose = $("select[name='choose']").find(":selected").val();
        if (info.trim() == "") {
            location.reload(true);
        } else {
            $.ajax({
                type : "GET",
                url : "/shelf",
                data : {
                    'info': info,
                    'choose': choose,
                },
                dataType : 'json',
                success : function(response) {
                    console.log(response);
                    callback(response);                    
                }
            });
        }
        return false;
    });
})