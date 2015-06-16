from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from jacquesIdea.models import Idee


# liste les commentaire
@login_required
def index(request):
    latest_question_list = Idee.objects.order_by('-pub_date')
    context = {'idee_list': latest_question_list}
    return render(request, 'jacquesIdea/index.html', context)