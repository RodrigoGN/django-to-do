console.log('scripts-base.js carregado!');

$('body').ready(function(){

    var baseUrl = 'http://127.0.0.1:8000/';
    var filter = $('#filter');

    var deleteBtn = $('.delete-btn');
    $(deleteBtn).on('click', function(e) {
        e.preventDefault();
        var dellink = $(this).attr('href');
        var result = confirm('Tem certeza que deseja deletar este item?');
        if(result) {
            window.location.href = dellink;
        }
    });
    $(filter).change(function(){
        var filterValue = $(this).val();
        window.location.href = baseUrl + '?filter=' + filterValue;
    });
    
});
function searchTask(){
    var searchForm = document.getElementById('search-form');
    searchForm.submit();
};

