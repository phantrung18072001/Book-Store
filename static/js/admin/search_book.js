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
                if (i == 5) {
                    html += "<td>" + format(book[i]) + ' VNĐ' + "</td>";
                } else {
                    html += "<td>" + book[i] + "</td>";
                }
            }
            html += "</tr>"
        }
        $(".table-book tbody").html(html);
        load();
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

    function load(){
        $('.clickable-row').on('click', function () {
            var currentRow=$(this).closest('tr');
            var book_id = parseInt(currentRow.find("td:eq(1)").text());
            console.log(book_id);
            document.getElementById("bookUpdate").setAttribute("value", book_id);
            document.getElementById("bookInfo").setAttribute("action", "/book_Modify");
            document.getElementById("bookInfo").submit();
        })
    }
    load();
})