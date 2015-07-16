# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from SpamAlyzer import analyzer

from .forms import FichierSoumisForm

import SpamAlyzer.analyzer

@login_required
def index(request):
    # If POST, then an upload has been made
    context = {}
    if request.method == "POST":
        # Get file
        form = FichierSoumisForm(request.POST, request.FILES)
        if form.is_valid():
            depotFichier = form.save(commit=False)
            depotFichier.auteur = request.user


            if analyzer.has_correct_xml_format(depotFichier.fichier):
                depotFichier.save()
                context['conversation'] = "FONCTIONER"
            else:
                context['conversation'] = "FORMAT PAS BON"
        else:
            context['conversation'] = "PAS FONCT"
    else:
        form = FichierSoumisForm()
        context['conversation'] =  None
    context["form"] = form

    return render(request, 'SpamAlyzer/index.html', context)