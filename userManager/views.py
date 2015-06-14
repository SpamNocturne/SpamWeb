from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.core.urlresolvers import reverse
from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .forms import ConnexionForm, ChangeMdpForm

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