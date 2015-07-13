$(function(){
    //préparation CSRF pour l'AJAX
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //ajout d'une playlist
    $("#add-playlist-btn").click(function(event){
        event.preventDefault();
        var $this = $(this);
        var $input = $("#add-playlist-form").find("input[name='name']");
        var name = $input.val().trim();
        if(name.length>0)
        {
            $this.attr('disabled','disabled').find("i").removeClass("fa-plus").addClass("fa-refresh fa-spin");

            setTimeout(function(){
                $this.removeAttr('disabled').find("i").removeClass("fa-refresh fa-spin").addClass("fa-plus");
                $input.val("");
            },2000);
        }
    });
});