
$(window).on('load', function () {
    $('#loader').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        setTimeout(function () {
            $('#loader').hide()
        }, 1500)

    })

})



$(document).ready(function () {
    $("#form").on('submit', function (event) {
        event.preventDefault();  
        const $forms = $(this); 
        const $spinner = $('#spin');
        const $btnsubmit = $('#btnsubmit');
        const $signup = $('#signup'); 
        const $message = $('#message'); 
        $btnsubmit.prop('disabled', true)
        $signup.text('processing...')  
        $spinner.show()  


        $.ajax({
            type: 'POST',
            url: '/signup/',
            data: $forms.serialize(),
            datatype: 'json',

            success: function (event) {
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(event.verify)
                    .show();
                   setTimeout(function(){
                      window.location = "/verify/"

                   }, 2000)
                
                // console.log(e)    // to log the error on console

            },


            error: function (e) {
                if (e.responseJSON.email) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.email)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.username) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.username)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.first_name) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.first_name)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.lastname) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.lastname)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.email_exist) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.email_exist)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.username_exist) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.username_exist)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.signup) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.signup)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }

            }

        });

    });

})
