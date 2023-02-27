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
        url: 'manage-likes',
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