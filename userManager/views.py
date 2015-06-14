from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import  authenticate, login, logout
from .forms import ConnexionForm

# Create your views here.
def connexion(request):
    error = False

    if(request.method == "POST"):
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: #!= None
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'userManager/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse('userManager:connexion'))