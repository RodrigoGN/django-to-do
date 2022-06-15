console.log('scripts-base.js carregado!');

$('body').ready(function(){

    var deleteBtn = $('.delete-btn');
    $(deleteBtn).on('click', function(e) {
        e.preventDefault();
        var dellink = $(this).attr('href');
        var result = confirm('Tem certeza que deseja deletar este item?');
        if(result) {
            window.location.href = dellink;
        }
    });

    
});
function searchTask(){
    var searchForm = document.getElementById('search-form');
    searchForm.submit();
};

