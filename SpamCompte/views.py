# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import *
from home.log import add_log
from .models import BattleDArgent, Depense, SpammeurConsommateur


def fait_partie_battle():
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            battle = get_object_or_404(BattleDArgent, pk=kwargs['battle_id'])
            if request.user not in battle.participants.all():
                return redirect(reverse('home:index'))
            else:
                return view(request, *args, **kwargs)

        return wrapper

    return decorator


@login_required
def index(request):
    mes_comptes = BattleDArgent.objects.filter(participants__in=[request.user])
    mes_scores = {}
    for c in mes_comptes:
        score_participants = c.calcul_score()
        mes_scores[c.nom] = score_participants[request.user.username]
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
@fait_partie_battle()
def consulter_battle(request, battle_id):
    battle = get_object_or_404(BattleDArgent, pk=battle_id)
    participants = battle.participants.all()
    reste_users_a_ajouter = len(participants) < len(User.objects.all())
    score_participants, equilibrage = battle.calcul_equilibre()
    depenses_et_montant = {}
    for depense in battle.depense_set.all():
        depenses_et_montant[depense] = depense.argent_depense()
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


@login_required
@fait_partie_battle()
def ajouter_depense(request, battle_id):
    battle = get_object_or_404(BattleDArgent, pk=battle_id)
    participants = battle.participants.all()
    if request.method == "POST":
        form = DepenseForm(request.POST, users=participants)
        if form.is_valid():
            depense = Depense(description=form.cleaned_data['description'], my_son_my_battle=battle,
                              date=timezone.now())
            depense.save()
            for u in participants:
                s_c = SpammeurConsommateur(
                    montant_depense=form.cleaned_data['montant_depense_{user}'.format(user=u.username)],
                    montant_utilise=form.cleaned_data['montant_utilise_{user}'.format(user=u.username)],
                    user=u,
                    depense_pour_laquelle_on_contribue=depense
                )
                s_c.save()
            battle.pub_date = timezone.now()
            battle.save()
            add_log(text="%s a ajouté la dépense %s au SpamCompte : %s" %
                         (request.user.username, depense.description[:20], battle.nom),
                    app="SpamCompte",
                    log_type="SpamCompte_ajout_depense",
                    user=request.user)
            return redirect(reverse('spamCompte:consulter_battle', args=(battle.id,)))
        else:
            error = True
    else:
        form = DepenseForm(users=participants)
    return render(request, 'SpamCompte/ajout_depense.html', locals())


def consulter_depense(request, battle_id, depense_id):
    battle = get_object_or_404(BattleDArgent, pk=battle_id)
    depense = get_object_or_404(Depense, pk=depense_id)
    participants = battle.participants.all()
    if request.method == "POST":
        form = DepenseForm(request.POST, users=participants, instance=depense)
        if form.is_valid():
            depense.description = form.cleaned_data['description']
            depense.date = timezone.now()
            depense.save()
            # on update les s_c existants
            for s_c in depense.spammeurconsommateur_set.all():
                s_c.montant_depense = form.cleaned_data['montant_depense_{user}'.format(user=s_c.user.username)]
                s_c.montant_utilise = form.cleaned_data['montant_utilise_{user}'.format(user=s_c.user.username)]
                s_c.save()
            s_c_to_create = participants - [sc.user for sc in depense.spammeurconsommateur_set.all()]
            for u in s_c_to_create:
                s_c = SpammeurConsommateur(
                    montant_depense=form.cleaned_data['montant_depense_{user}'.format(user=u.username)],
                    montant_utilise=form.cleaned_data['montant_utilise_{user}'.format(user=u.username)],
                    user=u,
                    depense_pour_laquelle_on_contribue=depense
                )
                s_c.save()
            battle.pub_date = timezone.now()
            battle.save()
            add_log(text="%s a modifié la dépense %s du SpamCompte : %s" %
                         (request.user.username, depense.description[:20], battle.nom),
                    app="SpamCompte",
                    log_type="SpamCompte_modifier_depense",
                    user=request.user)
            return redirect(reverse('spamCompte:consulter_battle', args=(battle.id,)))
        else:
            error = True
    else:
        form = DepenseForm(users=participants, instance=depense)
    is_update = True
    return render(request, 'SpamCompte/ajout_depense.html', locals())


def supprimer_depense(request, battle_id, depense_id):
    depense = get_object_or_404(Depense, pk=depense_id)
    battle = get_object_or_404(BattleDArgent, pk=battle_id)
    nom = battle.nom
    depense.delete()
    add_log(text="%s a supprimé la dépense %s du SpamCompte : %s" %
                 (request.user.username, depense.description[:20], nom),
            app="SpamCompte",
            log_type="SpamCompte_supprimer_depense",
            user=request.user)
    return redirect(reverse('spamCompte:consulter_battle', args=(battle_id,)))


def supprimer_compte(request, battle_id):
    battle = get_object_or_404(BattleDArgent, pk=battle_id)
    nom = battle.nom
    battle.delete()
    add_log(text="%s a supprimé le SpamCompte : %s" %
                 (request.user.username, nom),
            app="SpamCompte",
            log_type="SpamCompte_supprimer_battle",
            user=request.user)
    return redirect(reverse('spamCompte:index'))
