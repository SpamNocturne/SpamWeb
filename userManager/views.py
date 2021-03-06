# coding: utf8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .forms import ConnexionForm, ChangeMdpForm, InscriptionForm, ProfilForm
from home.log import add_log
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
            user.is_active = False

            user.save()
            add_log(text="Un nouveau Spamembre s'est inscrit : %s  - ( %s %s )" % (username, first_name, last_name),
                    app="userManager",
                    log_type="userManager_register",
                    user=user)
            return redirect(reverse('userManager:connexion'))
            '''
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('home:index'))
            '''
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

            # Connexion via email
            if "@" in username:
                user_by_mail = User.objects.filter(email=username)
                if user_by_mail:
                    # si le master existe, il ne peut y en avoir qu'un et UN SEUL. TRUE MASTEEEEEEER !
                    # Non plus serieusement, c'est parce que l'username est unique :D
                    if user_by_mail[0]:
                        username = user_by_mail[0].username

            user = authenticate(username=username, password=password)
            if user:    # != None
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('home:index'))
                else:
                    error = True
                    error_type = "inactive"
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