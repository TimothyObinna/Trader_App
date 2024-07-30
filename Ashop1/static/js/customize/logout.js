
$(window).on('load', function () {
    $('#loader').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        setTimeout(function () {
            $('#loader').hide()
        }, 1500)
    })

})



$(document).ready(function () {
    $("#linksubmit").on('click', function (event) {
        event.preventDefault();

        const $linksubmit = $('#linksubmit');
        const $logout = $('#logout');
        const $message = $('#message');
        const csrftoken = $("[name='csrfmiddlewaretoken']").val();

        if (confirm("Are you sure you want to log out?")) {
            $linksubmit.prop('disabled', true);
            $logout.text('processing...');

            if (csrftoken) {
                $.ajax({
                    type: 'POST',
                    url: '/logout/',
                    headers: { 'X-CSRFToken': csrftoken },
                    dataType: 'json',

                    success: function (event) {
                        if (event.logout) {
                            $message
                                .removeClass('alert-danger')
                                .addClass('alert-success')
                                .text(event.logout)
                                .show();
                            setTimeout(function () {
                                window.location.href = "/login/";
                                $linksubmit.prop('disabled', false);
                                $logout.text('Logout');
                            }, 3000);
                        }
                    }
                });
            } else {
                console.error('CSRF token is not defined');
            }
        }
    });
});


























// // INITIAL CODE 
// $(document).ready(function () {
//     $("#linksubmit").on('click', function (event) {
//         event.preventDefault();
//         // const $spinner = $('#spin');
//         const $linksubmit = $('#linksubmit');
//         const $logout = $('#logout');
//         const $message = $('#message');
//         $linksubmit.prop('disabled', true)
//         $logout.text('processing...')
//         // $spinner.show()
//         const csrftoken = $("[name='csrfmiddlewaretoken']").val();

//         // Now use ajax to communicate with the views
//         if (csrftoken) {
//             $.ajax({
//                 type: 'POST',
//                 url: '/logout/',
//                 headers: { 'X-CSRFToken': csrftoken },
//                 dataType: 'json',

//                 success: function (event) {
//                     if (event.logout) {
//                         $message
//                             .removeClass('alert-danger')
//                             .addClass('alert-success')
//                             .text(event.logout)
//                             .show();
//                         setTimeout(function () {
//                             // window.location = "/login/";
//                             window.location.href = "/login/";
//                             $linksubmit.prop('disabled', false)
//                             $logout.text('logout')
//                         }, 3000);
//                     }
//                 }
//             });
//         } else {
//             console.error('CSRF token is not defined');
//         }
//     });
// }) 