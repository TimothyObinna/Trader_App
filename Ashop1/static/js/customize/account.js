
$(window).on('load', function () {
    $('#loader').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        setTimeout(function () {
            $('#loader').hide()
        }, 1500)
    })

})


$(document).ready(function () {
    $("#alinksubmit").on('click', function (event) {
        event.preventDefault();

        const $alinksubmit = $('#alinksubmit');
        const $account = $('#account');
        const $message = $('#message');
        const csrftoken = $("[name='csrfmiddlewaretoken']").val();
        $alinksubmit.prop('disabled', true);
        $account.text('processing...');

        if (csrftoken) {
            $.ajax({
                type: 'GET',
                url: '/account/',
                headers: { 'X-CSRFToken': csrftoken },
                dataType: 'json',

                success: function (event) {
                    if (event.account) {
                        $message
                            .removeClass('alert-danger')
                            .addClass('alert-success')
                            .text(event.account)
                            .show();
                        setTimeout(function () {
                            window.location.href = "/account/";
                            $alinksubmit.prop('disabled', false);
                            $account.text('My Account');
                        }, 3000);
                    }
                }
            });
        } else {
            console.error('CSRF token is not defined');
        }

    });
});