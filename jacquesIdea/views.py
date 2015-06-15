from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# liste les commentaire
@login_required
def index(request):
    return None