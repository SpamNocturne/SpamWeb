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

    //loader, to append in a relative div
    var loaderTemplate = '<div class="my-overlay row"><i class="fa fa-refresh fa-spin"></i></div>';

    var toggle_playlist = function(event){
        event.preventDefault();
        $(".main-header a[data-toggle='control-sidebar']").click();
        $("a[href='#control-sidebar-playlist-tab']").click();
    };

    var search_video_list = function(event){
        event.preventDefault();
        var $this = $(this);
        var $input = $("#search-video-form").find("input[name='q']");
        var q = $input.val().trim();
        if(q.length>0)
        {
            $this.attr('disabled','disabled').find("i").removeClass("fa-plus").addClass("fa-refresh fa-spin");
            $input.attr('disabled','disabled');
            var params = {
                q: q
            };
            console.log("GO AJAX GO");
            var paramsEncoded = $.param(params);
            $.ajax({
                method: "POST",
                url: URLS.spamusicRechercherVideos,
                data: paramsEncoded,
                dataType : 'html',
                cache: false,
                success: function(html){
                    console.log("AJAX OK");
                    console.log(html);
                    $("#yt-tab-search-results").html($(html));
                },
                error: function(resultat, statut, erreur){
                    console.log("AJAX NOK");
                    alert("Désolé ! Une erreur serveur est survenue, réessayez, sinon actualisez la page.");
                },
                complete: function(){
                    console.log("AJAX DONE");
                    $this.removeAttr('disabled').find("i").removeClass("fa-refresh fa-spin").addClass("fa-plus");
                    $input.removeAttr('disabled');
                }
            });
        }
    };
    //ajout d'une playlist
    $("#add-playlist-btn").click(function(event){
        event.preventDefault();
        var $this = $(this);
        var $input = $("#add-playlist-form").find("input[name='name']");
        var name = $input.val().trim();
        if(name.length>0)
        {
            $this.attr('disabled','disabled').find("i").removeClass("fa-plus").addClass("fa-refresh fa-spin");
            $input.attr('disabled','disabled');
            var params = {
                name: name
            };
            console.log("GO AJAX GO");
            var paramsEncoded = $.param(params);
            $.ajax({
                method: "POST",
                url: URLS.spamusicAjouterPlaylist,
                data: paramsEncoded,
                dataType : 'html',
                cache: false,
                success: function(html){
                    console.log("AJAX OK");
                    console.log(html);
                    $(html).prependTo('#control-playlist-list').find(".playlist-play-link").click(clik_playlist);
                    $input.val("");
                },
                error: function(resultat, statut, erreur){
                    console.log("AJAX NOK");
                    alert("Désolé ! Une erreur serveur est survenue, réessayez, sinon actualisez la page.");
                },
                complete: function(){
                    console.log("AJAX DONE");
                    $this.removeAttr('disabled').find("i").removeClass("fa-refresh fa-spin").addClass("fa-plus");
                    $input.removeAttr('disabled');
                }
            });
        }
    });

    //Obtention des details d'une playlist et placement dans les details
    var clik_playlist = function(event){
        var $this = $(this);
        event.preventDefault();
        var playlist_id = $this.attr("data-playlistid");
        if(playlist_id.length>0)
        {
            var $loader = $(loaderTemplate).appendTo("#main-content");
            var params = {
                playlist_id: playlist_id
            };
            console.log("GO AJAX GO");
            var paramsEncoded = $.param(params);
            $.ajax({
                method: "POST",
                url: URLS.spamusicDetailsPlaylist,
                data: paramsEncoded,
                dataType : 'html',
                cache: false,
                success: function(html){
                    console.log("AJAX OK");
                    console.log(html);
                    var $html = $(html);

                    //binds
                    $html.find("[data-toggle='control-sidebar-playlist']").click(toggle_playlist);
                    $html.find('#search-video-btn').click(search_video_list);

                    //insertion
                    $("#main-content").html($html);

                    //recherche des vidéos de la playlist
                    var $loaderVideo = $(loaderTemplate).appendTo("#yt-tab-videos");
                    $.ajax({
                        method: "POST",
                        url: URLS.spamusicPlaylistItems,
                        data: paramsEncoded,
                        dataType : 'html',
                        cache: false,
                        success: function(html){
                            console.log("AJAX OK");
                            console.log(html);
                            var $html = $(html);
                            //binds

                            //insertion
                            $html.appendTo($("#yt-tab-videos"));
                        },
                        error: function(resultat, statut, erreur){
                            console.log("AJAX NOK");
                            alert("Désolé ! Une erreur serveur est survenue, réessayez, sinon actualisez la page.");
                        },
                        complete: function(){
                            console.log("AJAX DONE");
                            $loaderVideo.remove();
                        }
                    });
                },
                error: function(resultat, statut, erreur){
                    console.log("AJAX NOK");
                    alert("Désolé ! Une erreur serveur est survenue, réessayez, sinon actualisez la page.");
                },
                complete: function(){
                    console.log("AJAX DONE");
                    $loader.remove();
                }
            });
        }
    };



    var test = function(){alert("click");};
    //Binds
    $(".playlist-play-link").click(clik_playlist);
});