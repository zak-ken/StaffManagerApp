$(document).ready(function () {
    var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var table = $('#DataTable');
    sort_columns(table);

    $(document).on('click','button[type=button]',function() {
        console.log(this.id);
        var row_action = this.id;
        var row_edit_or_del = row_action.split("_", 1);
        var row_name = row_action.split('_')[1];
        if (row_edit_or_del == 'delete'){
            console.log('row_name = ', row_name)
            delete_user(row_name);
        };

   });
});


function delete_user(row_name){

    var param_data = {'param_data': {'id': row_name}};
    var url = 'ajax/delete/';
    var result = $.ajax({
        url: url,
        data: param_data,
        dataType: "json",
        method: 'post',
        async: false
    }).responseText;

    var json_Data = JSON.parse(result);
    if (json_Data.user_delete){
        $('#' + row_name).remove();
    }
    else{
        console.log('A Error occured whilst deleting the record');
    };

};


function sort_columns(table){
$('#name, #surname, #job_title, #start_date, #job_descrip')
        .wrapInner('<span title="sort this column"/>')
        .each(function(){
            var th = $(this),
                thIndex = th.index(),
                inverse = false;
            th.click(function(){
                table.find('td').filter(function(){
                    return $(this).index() === thIndex;
                }).sortElements(function(a, b){
                    return $.text([a]) > $.text([b]) ?
                        inverse ? -1 : 1
                        : inverse ? 1 : -1;
                }, function(){
                    // parentNode is the element we want to move
                    return this.parentNode;
                });
                inverse = true;
            });
        });
};
