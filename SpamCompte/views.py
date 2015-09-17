# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import *
from django.contrib.auth.models import User
from home.log import add_log
from .models import BattleDArgent, Depense, SpammeurConsommateur


@login_required
def index(request):
    mes_comptes = BattleDArgent.objects.filter(participants__in=[request.user])
    return render(request, 'SpamCompte/index.html', locals())


@login_required
def ajout_battle(request):
    if request.method == "POST":
        form = BattleDArgentForm(request.POST, users=[request.user.pk])
        if form.is_valid():
            battle = form.save(commit=False)
            battle.pub_date = timezone.now()
            battle.save()
            form.save_m2m()
            add_log(text="%s a créé le SpamCompte : %s" % (request.user.username, battle.nom),
                    app="SpamCompte",
                    log_type="SpamCompte_ajout_battle",
                    user=request.user)
            return redirect(reverse('spamCompte:consulter_battle', args=(battle.id,)))
        else:
            error = True
    else:
        form = BattleDArgentForm(users=[request.user.pk])
    return render(request, 'SpamCompte/ajout_battle.html', locals())


@login_required
def consulter_battle(request, id_battle):
    battle = get_object_or_404(BattleDArgent, pk=id_battle)
    participants = battle.participants.all()
    if request.user in participants:
        if request.method == "POST":
            form = BattleDArgentForm(request.POST, instance=battle, users=[u.pk for u in participants])
            if form.is_valid():
                battle = form.save(commit=False)
                battle.pub_date = timezone.now()
                battle.save()
                form.save_m2m()
                add_log(text="%s a modifié le SpamCompte : %s" % (request.user.username, battle.nom),
                        app="SpamCompte",
                        log_type="SpamCompte_modification_battle",
                        user=request.user)
                return redirect(reverse('spamCompte:consulter_battle', args=(battle.id,)))
            else:
                error = True
        else:
            form = BattleDArgentForm(users=[u.pk for u in participants], instance=battle)
        return render(request, 'SpamCompte/battle_detailed.html', locals())
    else:
        return HttpResponse(
            'Désolé, vous ne faites pas partie de ce SpamCompte. Demandez au créateur de vous ajouter !', status=401)


@login_required
def ajout_depense(request, id_battle):
    battle = get_object_or_404(BattleDArgent, pk=id_battle)
    participants = battle.participants.all()
    if request.user in participants:
        if request.method == "POST":
            form = DepenseForm(request.POST)
            if form.is_valid():
                depense = form.save(commit=False)
                depense.date_changement = timezone.now()
                depense.save()
                form.save_m2m()
                add_log(text="%s a ajouté la dépense %s au SpamCompte : %s" % (request.user.username, depense.description[:20], battle.nom),
                        app="SpamCompte",
                        log_type="SpamCompte_ajout_depense",
                        user=request.user)
                return redirect(reverse('spamCompte:consulter_battle', args=(battle.id,)))
            else:
                error = True
        else:
            form = DepenseForm()
        return render(request, 'SpamCompte/ajout_depense.html', locals())
    else:
        return HttpResponse(
            'Désolé, vous ne faites pas partie de ce SpamCompte. Demandez au créateur de vous ajouter !', status=401)
