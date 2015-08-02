# -*- coding: utf-8 -*-

__author__ = 'david'

from SpamAlyzer import models
import collections

class StatsHelper:
    def __init__(self, mec=None):
        self.id = -1
        self.all_messages = models.Message.objects.all()
        self.all_users = models.UtilisateurStats.objects.all()
        if mec is None:
            self.fill_msg_per_user()
        else:
            self.all_messages = self.all_messages.filter(auteur = mec)
            self.id = mec.id

        self.fill_nb_messages()
        self.fill_nb_pouces()
        self.fill_msg_per_date()
        self.fill_most_used_words()

    def fill_nb_messages(self):
        self.nb_messages = self.all_messages.count()

    def fill_nb_pouces(self):
        self.nb_pouces = self.all_messages.filter(texte = None).count()

    def fill_most_used_words(self):
        if self.id != -1:
            users_here = self.all_users.filter(id=self.id)
        else:
            users_here = self.all_users

        motsScore = {}
        for u in users_here:
            all_mots = u.get_mots_plus_utilises()
            for m in all_mots:
                m.mot = m.mot.lower()
                if m.mot not in self.mots_ignore and len(m.mot) != 1:
                    if m.mot in motsScore:
                        motsScore[m.mot] += m.score
                    else:
                        motsScore[m.mot] = m.score

        NB_DISPLAYED_WORDS = 20
        i = 0
        self.graphe_most_used_words = []
        for unMotScore in sorted(motsScore, key=motsScore.get, reverse=True):
            self.graphe_most_used_words.append({'xaxis': unMotScore, 'yaxis': motsScore[unMotScore]})
            i += 1
            if i > NB_DISPLAYED_WORDS:
                break


    def fill_msg_per_date(self):
        self.graphe_nb_msg_per_date = {}
        for unMsg in self.all_messages:
            moisEtAn = "{0}-{1}".format(unMsg.date.year, unMsg.date.month)
            if moisEtAn in self.graphe_nb_msg_per_date:
                self.graphe_nb_msg_per_date[moisEtAn] += 1
            else:
                self.graphe_nb_msg_per_date[moisEtAn] = 1
        self.graphe_nb_msg_per_date = collections.OrderedDict(sorted(self.graphe_nb_msg_per_date.items()))

    def fill_msg_per_user(self):
        user_and_msgs = {}
        for u in self.all_users:
            user_and_msgs[u.nom_fb] = models.Message.objects.filter(auteur = u).count()

        self.graphe_msg_per_user = [{'xaxis': user, 'yaxis': user_and_msgs[user]} for user in sorted(user_and_msgs, key=user_and_msgs.get, reverse=True)]

    mots_ignore = [
        "est",
        "la",
        "le",
        "de",
        "a",
        "pas",
        "je",
        "en",
        "un",
        "une",
        "et",
        "pour",
        "ça",
        "ca",
        'que',
        "qui",
        "quoi",
        "tu",
        "on",
        "les",
        "et",
        "dans",
        "ai",
        "vous",
        "il",
        "elle",
        "du",
        "si",
        "au",
        "moi",
        "ce",
        "avec",
        "aussi",
        "plus",
        "tout",
        "mais",
        "fait",
        "des",
        "qu",
        "peut",
        "suis",
        "me",
        "va",
        "là",
        "sur",
        "ne",
        "se",
        "faire",
        "as"
    ]