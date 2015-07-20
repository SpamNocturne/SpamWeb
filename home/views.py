from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Log

# Create your views here.


@login_required
def index(request):
    logs = Log.objects.order_by('-date')
    context = {
        'logs': logs
    }
    return render(request, 'home/index.html', context)