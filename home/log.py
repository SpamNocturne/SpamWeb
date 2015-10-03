from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest


from .models import Log, FirstUnseenLog

# add the params you need, and use is as constants
LOG_PARAMS = {
    "app": [
        "jacquesIdea",
        "spamusic",
        "userManager",
        "SpamAlyzer",
        "spamConso",
        "SpamCompte",
    ],
    "log_type": [
        "spamusic_add_playlist",
        "spamusic_add_video",
        "jacquesIdea_create_idea",
        "jacquesIdea_delete_idea",
        "jacquesIdea_comment",
        "jacquesIdea_vote",
        "jacquesIdea_validate_idea",
        "SpamAlyzer_depot_archive",
        "userManager_register",
        "spamConso_add_conso_beer",
        "spamConso_add_conso_tacos",
        "SpamCompte_ajout_battle",
        "SpamCompte_modification_battle",
        "SpamCompte_ajout_depense",
        "SpamCompte_supprimer_depense",
        "SpamCompte_modifier_depense",
        "SpamCompte_supprimer_battle",
    ],
}


def add_log(text, app, log_type, user):

    if app not in LOG_PARAMS["app"]:
        raise NameError('Unknown app name')
    if log_type not in LOG_PARAMS["log_type"]:
        raise NameError('Unknown log_type name')

    log = Log()
    log.text = text
    log.app = app
    log.log_type = log_type
    log.user = user
    log.save()
    users = User.objects.all()
    # On met a jour les notif de tous les users
    for us in users:
        if us != user:
            # S'il n'a pas de last log on le lui créé
            if not hasattr(us, 'firstunseenlog'):
                lastlog = FirstUnseenLog(user=us, log=log)
                lastlog.save()
            # si l'utilisateur est a jour il ne l'est plus
            elif us.firstunseenlog.log is None:
                us.firstunseenlog.log = log
                us.firstunseenlog.save()
    return log


def get_logs(number=0):
    if number < 0:
        return HttpResponseBadRequest()
    elif number == 0:
        # All
        return Log.objects.order_by('-date')
    else:
        return Log.objects.order_by('-date')[:number]
