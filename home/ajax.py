
'''
    AJAX LOG
'''
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from home.log import add_log, get_logs


@login_required
def ajax_home_add_log(request):
    # recupération des parametres
    text = request.POST["text"]
    app = request.POST["app"]
    log_type = request.POST["log_type"]
    if text is None or app is None or log_type is None:
        return HttpResponseBadRequest()
    user = request.user
    log = add_log(text=text, app=app, log_type=log_type, user=user)
    return HttpResponse()


@login_required
def ajax_get_notifications(request):
    number = 20
    logs = get_logs(number)
    unseenlog = None
    user = request.user
    if hasattr(user, 'firstunseenlog'):
        unseenlog = user.firstunseenlog.log

    context = {
        'logs': logs,
        'unseenlog': unseenlog,
    }
    return render(request, 'home/notifications.html', context)
