
$(window).on('load', function () {
    $('#loader').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        setTimeout(function () {
            $('#loader').hide()
        }, 2000)
    })

})



$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: '/', 
        dataType: 'json',

        success: function (event) {
            const $message = $('#message');

            if (event.vendor) {
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(event.vendor)
                    .show();
                setTimeout(function(){
                    $message.hide();
                }, 3000 );

            } else if (event.customer) {
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(event.customer)
                    .show();
                setTimeout(function(){
                    $message.hide();
                }, 3000 );
            }
        },
    });
});
