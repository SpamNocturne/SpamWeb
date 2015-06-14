from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
@login_required
def index(request):
    template_name='home/index.html'
    context = {
    }
    return render(request, template_name, context)