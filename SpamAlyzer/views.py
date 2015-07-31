# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from SpamAlyzer.forms import FichierSoumisForm
from SpamAlyzer import analyzer, models
from django.http import Http404

from lxml import etree
from threading import Thread
from home.log import add_log
import traceback
from SpamAlyzer.StatsHelper import StatsHelper

@login_required
def index(request):
    # If POST, then an upload has been made
    context = {}
    if request.method == "POST":
        form = FichierSoumisForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.auteur = request.user

            try:
                anal = analyzer.Analyzer(fichier)
                await_t = Thread(target=await_analyze_ending, args=(anal, request.user,))
                await_t.setDaemon(True)
                await_t.start()
                fichier.save()
                context["error_message"] = "Ca bidouille ! Et ça peut prendre un peu de temps parce que je code " \
                                           "n'importe comment. Bref, ça enverra une notif' dès ça a fini de charger " \
                                           "l'internet. Merci aurevoir <3";
                return render_to_response("SpamAlyzer/message.html", context)
            except etree.DocumentInvalid:
                context["error_message"] = "Oh non! Ton fichier est tout naze. " \
                                           "Python me dit dans l'oreillette DocumentInvalid. " \
                                           "C'est triste. Et franchement, tu me déçois. Je te croyais mieux que ça."
                return render_to_response("SpamAlyzer/message.html", context)
            except:
                context["error_message"] = "Aïe aïe aïe. Je ne saurais pas te dire ce qu'il s'est passé. Enfin bon, " \
                                           "de toute façon je ne suis qu'un texte écrit en dur dans le code par " \
                                           "David. " \
                                           "Normal que je ne pas déduire grand chose de l'erreur. " \
                                           "Mais voilà le message de l'exception si ça peut t'aider. (mais vu que " \
                                           "t'es nul(le), envoie ça à David. Il saura débugger, mieux que toi, " \
                                           "sa merde qu'il a pondu) : {0}".format(traceback.format_exc())
                return render_to_response("SpamAlyzer/message.html", context)
        else:
            context["error_message"] = "Oh non! Ton fichier est tout naze. " \
                                       "Python me dit dans l'oreillette que le formulaire n'est pas valide. " \
                                       "C'est triste. Et franchement, tu me déçois. Je te croyais mieux que ça."
            return render_to_response("SpamAlyzer/message.html", context)
    # No POST made, normal
    else:
        context["conversation"] = None
        form = FichierSoumisForm()

    context["form"] = form
    return render(request, 'SpamAlyzer/index.html', context)

def await_analyze_ending(analyzer, user):
    t = Thread(target=analyzer.analyze_the_spam_muhaha())
    t.setDaemon(True)
    t.start()
    t.join()
    add_log(text="{0} a déposé une archive Facebook pour alimenter la conversation du spam ! "
                 "Sa contribution nous a apporté {1} messages que le SpamWeb ne référençait pas encore. "
                 "Merci !".format(user, analyzer.new_messages),
            app="SpamAlyzer",
            log_type="SpamAlyzer_depot_archive",
            user=user)

@login_required
def conversation(request, num_page):
    num_page = int(num_page)
    NB_MSG_PAR_PAGE = 200
    context = { "conversation": None }
    messages = models.Message.objects.order_by("-date")
    nb_messages = messages.count()
    if nb_messages != 0:
        nb_pages = int(nb_messages / NB_MSG_PAR_PAGE) + 1
        if num_page > nb_pages:
            raise Http404("Invalid page number.")
        first_message = (num_page - 1) * NB_MSG_PAR_PAGE
        last_message = num_page * NB_MSG_PAR_PAGE
        if last_message > nb_messages:
            last_message = nb_messages
        context["conversation"] = messages[first_message:last_message]
        context["num_page"] = num_page
        context["nb_pages"] = nb_pages

    return render(request, "SpamAlyzer/conversation.html", context)

@login_required
def historique(request):
    context = {}
    all_depots = models.FichierSoumis.objects.order_by("-date_depot")
    if all_depots.count() != 0:
        context["depots"] = all_depots

    return render(request, "SpamAlyzer/historiqueDepot.html", context)

@login_required
def statsGlobales(request):
    stats = StatsHelper()
    context = {
        "nb_messages" : stats.nb_messages,
        "nb_pouces": stats.nb_pouces,
        "graphe_user_most_msg": stats.graphe_msg_per_user,
        "graphe_most_used_words": stats.graphe_most_used_words,
        "graphe_nb_msg_per_date": stats.graphe_nb_msg_per_date,
    }

    return render(request, "SpamAlyzer/statsGlobales.html", context)


@login_required
def statsSpammeurs(request):
    spammeurs = []
    for spammeur in models.UtilisateurStats.objects.all():
        spammeurs.append(spammeur)
    return render(request, "SpamAlyzer/choixSpammeur.html", {"spammeurs": spammeurs})


def statsMec(request, id_pers):
    mecs = models.UtilisateurStats.objects.filter(id = id_pers)
    if mecs.count() == 0:
        return render(request, "SpamAlyzer/statsMec.html", {"error_message": "Utilisateur inconnu"})
    mec = mecs[0]

    stats = StatsHelper(mec)
    context = {
        "nom": mec.nom_fb,
        "nb_messages" : stats.nb_messages,
        "nb_pouces": stats.nb_pouces,
        "graphe_most_used_words": stats.graphe_most_used_words,
        "graphe_nb_msg_per_date": stats.graphe_nb_msg_per_date,
    }

    return render(request, "SpamAlyzer/statsMec.html", context)