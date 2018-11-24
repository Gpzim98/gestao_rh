function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log('Sucesso!!!');
            $("#mensagem").text('Hora extra marcada como utilizada');
        }
    });
}
