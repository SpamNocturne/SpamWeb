# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from home.log import add_log
from django.db.models import Count
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
def add_conso(request):
    error = False
    if request.method == "POST":
        form = ConsoForm(request.POST)
        if form.is_valid():
            conso = form.save(commit=False)
            conso.conso_date = timezone.now()
            conso.consommateur = request.user
            conso.save()
            add_log(text="%s a consommé %s" % (conso.type, conso.consommateur.username),
                    app="spamConso",
                    log_type="spamConso_add_conso",
                    user=request.user)
        else:
            error = True
    else:
        form = ConsoForm()

    return redirect(reverse('spamConso:index'))


@login_required
def beer_view(request):
    user = User.objects.values('username', 'id')
    biere_list = Consommation.objects.filter(type='biere').select_related('consommateur')
    user_biere_list = biere_list.values('consommateur').annotate(total=Count('type'))

    for i in user_biere_list:
        i['username'] = user.get(id = i['consommateur'])['username']

    chouffe_list = biere_list.filter(description='chouffe') \
        .values('consommateur') \
        .annotate(total=Count('type'))
    for i in chouffe_list:
        i['username'] = user.get(id = i['consommateur'])['username']
    bpm = biere_list.extra(select={'month': 'extract( month from conso_date )'})\
        .values('month')\
        .annotate(total=Count('type'))
    context = {'user_biere_list':user_biere_list, 'chouffe_list':chouffe_list, 'bpm':bpm}
    return render(request, 'spamConso/biere.html', context)
