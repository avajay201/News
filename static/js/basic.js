// Clear sign up fields ==>>
$('.sign_up_back_btn').on('click', function(){
    $('#id_username').val('');
    $('#id_password').val('');
    $('#id_email').val('');
    $('.errorlist').remove();
})

// Clear sign in fields ==>>
$('.sign_in_back_btn').on('click', function(){
    $('#login_username').val('');
    $('#login_password').val('');
    $('.errorlist').remove();
})


// Like button ==>>
$(function() {
    $('.button-like')
      .bind('click', function(event) {
        $(this).toggleClass("liked");
        $($(this).children()[1]).toggleClass("liked-span");
    })
});

// Count likes ==>>
$(document).on('click', '.button-like', function(){
    let post_id = $(this).prev().val();
    let user_id = $(this).prev().prev().val();
    var like_status = ''
    let self = $(this);
    if ($(this).hasClass('liked')){
        like_status = 'plus';
    }
    else{
        like_status = 'minus';
    }
    $.ajax({
        type: 'post',
        url: '/manage-likes',
        data: {
            post_id: post_id,
            user_id: user_id,
            like_status: like_status,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $($(self).find('span')[1]).text(response.post_likes);
            if ($(self).hasClass('liked')){
                $($(self).find('span')[1]).addClass('liked-span');
                $($(self).find('span')[0]).addClass('liked-span');
            }
            else{
                $($(self).find('span')[0]).removeClass('liked-span');
                $($(self).find('span')[1]).removeClass('liked-span');
            }
        }
    })    
})

// Default liked post ==>>
if ($('.button-like').hasClass('liked')){
    $($(this).find('span')[1]).css('color', 'white');
}
else{
    $($(this).find('span')[1]).css('color', '#0d6efd');
}


// Reload ==>>
function reload(){
    window.location = '';
}

// Sign up ==>>
$('.sign_up_btn').on('click', function(){
    let form_data = $('.sign_up_form').serialize();
    $.ajax({
        type: 'POST',
        url: '/sign-up',
        data: form_data,
        success: function(response){
            if (response.success){
                $('.errorlist').remove();
                toastr.success(response.success);
                $('.sign_up_back_btn').click();
                $('#sign_in_id').click();
            }
            else if (response.fail){
                $('.errorlist').remove();
                toastr.error(response.fail);
            }
            else if (response.errors){
                $('.errorlist').remove();
                for (err in response.errors){
                    $(`#id_${err}`).after(`<p class="errorlist">${response.errors[err][0]}</p>`);
                }
            }
            else{
                toastr.error('Please try agagin.');
            }
        }
    })
})

// Sign in ==>>
$('.sign_in_btn').on('click', function(){
    let form_data = $('.sign_in_form').serialize();
    $.ajax({
        type: 'POST',
        url: '/sign-in',
        data: form_data,
        success: function(response){
            if (response.success){
                $('.errorlist').remove();
                toastr.success(response.success);
                setTimeout(reload, 1000);
            }
            else if (response.fail){
                $('.errorlist').remove();
                toastr.error(response.fail);
            }
            else if(response.errors){
                $('.errorlist').remove();
                for (err in response.errors){
                    $(`#login_${err}`).after(`<p class="errorlist">${response.errors[err][0]}</p>`);
                }
            }
            else{
                toastr.error('Please try again.');
            }
        }
    })
})

// Logout
$('#logout').on('click', function(){
    $.ajax({
        type: 'post',
        url: '/logout',
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            if (response.success == true){
                toastr.success('Logout Successfully.');
                setTimeout(reload, 1000);
            }
            else{
                toastr.error('Please try again.');
            }
        }
    })
})
