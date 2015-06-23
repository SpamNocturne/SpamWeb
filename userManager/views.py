# coding: utf8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .forms import ConnexionForm, ChangeMdpForm, InscriptionForm, ProfilForm
from .models import UserProfile

# Create your views here.
def inscription(request):
    if request.user.is_authenticated():
        return redirect(reverse('home:index'))
    error = False
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(username, email, password)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user.first_name = first_name
            user.last_name = last_name

            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('home:index'))
        else:
            error = True
    else:
        form = InscriptionForm()

    return render(request, 'userManager/inscription.html', locals())

@sensitive_post_parameters()
@csrf_protect
@never_cache
def connexion(request):
    if request.user.is_authenticated():
        return redirect(reverse('home:index'))
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: #!= None
                login(request, user)
                return redirect(reverse('home:index'))
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'userManager/connexion.html', locals())


@login_required
def deconnexion(request):
    logout(request)
    return redirect(reverse('userManager:connexion'))


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request):
    template_name = 'userManager/mdp_change.html'
    password_change_form = ChangeMdpForm
    post_change_redirect = reverse('userManager:password_change_done')
    error = False
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one if
            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
            # is enabled.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
        else:
            error = True
    else:
        form = password_change_form(user=request.user)
    context = {
            'form': form,
            'title': 'Changement de mot de passe',
            'error': error,
        }
    return TemplateResponse(request, template_name, context)


@login_required
def password_change_done(request):
    template_name='userManager/mdp_change_done.html'
    context = {
        'title': 'Changement de mot de passe effectif.',
    }
    return TemplateResponse(request, template_name, context)

@login_required
def profile_edit(request):
    error = False
    user = request.user
    profil = UserProfile.objects.get(pk=user.userprofile.id)
    if request.method == "POST":
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.save()
            return redirect(reverse('userManager:profile_edit'))
        else:
            error = True
    else:
        form = ProfilForm(instance=profil)
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'userManager/profil.html', context)