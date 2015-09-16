# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from home.log import add_log


@login_required
def index(request):
    return render(request, 'SpamCompte/index.html', locals())
