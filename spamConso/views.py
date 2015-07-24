# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from home.log import add_log

from spamConso.forms import ConsoForm
from spamConso.models import Consommation



@login_required
def index(request):
    csrfContext = RequestContext(request)
    conso_list = Consommation.objects.order_by('conso_date')
    form = ConsoForm()
    context = {'conso_list': conso_list, 'form': form, 'csrfContext': csrfContext}
    return render(request, 'spamConso/index.html', context)


@login_required
def get_conso(request):
    conso_list = Conso.objects.filter(type_exact = request.type)
    user_conso_list = conso_list.filter(consommateur=request.user)
    context = {'conso_list': conso_list, 'user_conso_list': user_conso_list}
    return render(request, 'spamConso/%s.html'.format(conso.type), context)


def add_conso(request):
    error = False
    if request.method == "POST":
        form = ConsoForm(request.POST)
        if form.is_valid():
            conso = form.save(commit=False)
            conso.conso_date = timezone.now()
            conso.consommateur = request.user
            conso.save()
            #add_log(text="%s a s'est fait plaiz : %s" % (request.user.username, conso.type),
            #        app="spamConso",
            #        log_type="spamConso_add_conso",
            #        user=request.user)
        else:
            error = True
    else:
        form = ConsoForm()
    return redirect('index.html')
