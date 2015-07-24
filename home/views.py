from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from home.log import add_log
from .models import Log

# Create your views here.


@login_required
def index(request):
    context = {
    }
    return render(request, 'home/index.html', context)
