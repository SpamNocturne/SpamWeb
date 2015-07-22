from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from home.log import add_log
from .models import Log

# Create your views here.


@login_required
def index(request):
    logs = Log.objects.order_by('-date')
    context = {
        'logs': logs
    }
    return render(request, 'home/index.html', context)



'''
    AJAX LOG
'''


@login_required
def home_add_log(request):
    # recupération des parametres
    text = request.POST["text"]
    app = request.POST["app"]
    log_type = request.POST["log_type"]
    if text is None or app is None or log_type is None:
        return HttpResponseBadRequest()
    user = request.user
    log = add_log(text=text, app=app, log_type=log_type, user=user)
    return HttpResponse()
