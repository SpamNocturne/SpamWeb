# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from SpamAlyzer.forms import FichierSoumisForm
from SpamAlyzer import analyzer

from lxml import etree

@login_required
def index(request):
    # If POST, then an upload has been made
    context = {"error_message":"oui"}
    if request.method == "POST":
        form = FichierSoumisForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.auteur = request.user

            try:
                anal = analyzer.Analyzer(fichier.fichier)
                msg = anal.get_spam_messages() # TODO, ca va etre plus compliqué que ca
            except etree.DocumentInvalid:
                context["error_message"] = "Oh non! Ton fichier est tout naze. " \
                                           "Python me dit dans l'oreillette DocumentInvalid. " \
                                           "C'est triste. Et franchement, tu me déçois. Je te croyais mieux que ça."
                return render_to_response('SpamAlyzer/message.html', context)
        else:
            context["error_message"] = "Oh non! Ton fichier est tout naze. " \
                                       "Python me dit dans l'oreillette que le formulaire n'est pas valide. " \
                                       "C'est triste. Et franchement, tu me déçois. Je te croyais mieux que ça."
            return render_to_response('SpamAlyzer/index.html', context)
    # No POST made, normal
    else:
        context["conversation"] = None
        form = FichierSoumisForm()

    context["form"] = form
    return render(request, 'SpamAlyzer/index.html', context)