$(function() {
    $('#obtener_repetido').on("click", function(e) {
        e.preventDefault();
        total_names = $('#total_names').val();
        $.ajax({
            url: '/api/v1/masrepetido',
            data: $('#data').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
              if(!response.error)
                $('#resultado').val(response.nombre);
            },
            error: function(error) {
              var response = JSON.parse(error);
                console.log(error);
            }
        });
    });
});