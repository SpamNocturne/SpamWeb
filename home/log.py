__author__ = '(PRO) Loïc Touzard'

from .models import Log

# add the params you need, and use is as constants
LOG_PARAMS = {
    "app": [
        "jacquesIdea",
        "spamusic",
        "userManager",
    ],
    "log_type": [
        "spamusic_add_playlist",
        "spamusic_add_video",
        "jacquesIdea_create_idea",
        "jacquesIdea_delete_idea",
        "jacquesIdea_comment",
        "jacquesIdea_vote",
        "userManager_register"
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
    return log
