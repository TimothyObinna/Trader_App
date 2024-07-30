
$(window).on('load', function () {
    $('#loader').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        setTimeout(function () {
            $('#loader').hide()

        }, 1500)

    })

})



$(document).ready(function () {
    $("#form-l").on('submit', function (event) {
        event.preventDefault();
        const $forms = $(this);
        const $spinner = $('#spin');
        const $btnsubmit = $('#btnsubmit');
        const $login = $('#login');
        const $message = $('#message');
        $btnsubmit.prop('disabled', true)
        $login.text('processing...')
        $spinner.show()

        $.ajax({
            type: 'POST',
            url: '/login/',
            data: $forms.serialize(),
            datatype: 'json',


            success: function (event) {
                if (event.home) {        
                  $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(event.home)
                    .show();
                  setTimeout(function(){
                    window.location = "/";
                  }, 3000);
                } 
            },




            error: function (e) {
                if (e.responseJSON.email || e.responseJSON.password) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.email)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $login.text('Login')

                }


                if (e.responseJSON.password || e.responseJSON.email) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.password)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $login.text('Login')

                }


                if (e.responseJSON.invalid) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.invalid)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $login.text('Login')

                }


                if (e.responseJSON.reverify) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.reverify)
                        .show();
                    setTimeout(function(){
                        window.location = "/reverify/";
                        $btnsubmit.prop('disabled', false)
                        $spinner.hide()
                        $login.text('Login')      
                    }, 3000)

                }


                if (e.responseJSON.signup) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.signup)
                        .show();
                    setTimeout(function(){
                        window.location = "/signup/";
                        $btnsubmit.prop('disabled', false)
                        $spinner.hide()
                        $login.text('Login')      
                    }, 3000)

                }
                // console.log(e.responseJSON)
            },    

        });    


    });

})




