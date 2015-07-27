# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from home.log import add_log

from jacquesIdea.forms import IdeeForm
from jacquesIdea.models import Idee, Commentaire


# liste les commentaire
# TODO les trier dans un certain ordre ?
@login_required
def index(request):
    latest_question_list = Idee.objects.order_by('-pub_date')
    context = {'idee_list': latest_question_list}
    return render(request, 'jacquesIdea/index.html', context)


@login_required
def createIdea(request):
    error = False
    if request.method == "POST":
        form = IdeeForm(request.POST)
        if form.is_valid():
            idee = form.save(commit=False)
            idee.pub_date = timezone.now()
            idee.auteur = request.user
            idee.save()
            add_log(text="%s a eu une nouvelle idée : %s" % (request.user.username, idee.titre),
                    app="jacquesIdea",
                    log_type="jacquesIdea_create_idea",
                    user=request.user)
            return redirect(reverse('jacquesIdea:index'))
        else:
            error = True
    else:
        form = IdeeForm()
    return render(request, 'jacquesIdea/createIdea.html', locals())
