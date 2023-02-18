// Clear sign up fields ==>>
$('.sign_up_back_btn').on('click', function(){
    $('#id_username').val('');
    $('#id_password').val('');
    $('#id_email').val('');
})

// Clear sign in fields ==>>
$('.sign_in_back_btn').on('click', function(){
    $('#login_username').val('');
    $('#login_password').val('');
})

// Sign up ==>>
$('.sign_up_btn').on('click', function(){
    // let username = $('#id_username').val();
    // let password = $('#id_password').val();
    // let email = $('#email').val();
    let form_data = $('.sign_up_form').serialize();
    console.log(form_data)
    data = {
        form_data: form_data,
        csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val()
    }
    $.ajax({
        type: 'POST',
        url: '/sign-up',
        data: data,
        success: function(response){
            if (response.success){
                toastr.success(response.success);
            }
            else if (response.fail){
                toastr.error(response.fail);
            }
            else{
                toastr.error(response.error);
            }
        }
    })
})

// Sign in ==>>
$('.sign_in_btn').on('click', function(){
    let username = $('#login_username').val();
    let password = $('#login_password').val();
    data = {
        username: username,
        password: password,
        csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val()
    }
    $.ajax({
        type: 'POST',
        url: '/sign-in',
        data: data,
        success: function(response){
            if (response.success){
                toastr.success(response.success);
            }
            else if (response.fail){
                toastr.error(response.fail);
            }
            else{
                toastr.error(response.error);
            }
        }
    })
})