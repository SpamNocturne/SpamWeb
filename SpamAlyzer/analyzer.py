# -*- coding: utf-8 -*-

__author__ = 'David'
__date__ = '2015-07-07'

from lxml import etree
from datetime import datetime, timezone, timedelta
import re
from SpamAlyzer import models

class Analyzer:

    textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x100))
    is_binary_string = lambda bytes: bool(bytes.translate(None, Analyzer.textchars))
    utc_offset = lambda offset: timezone(timedelta(seconds=offset))

    xsdschema_root = etree.parse("SpamAlyzer/static/SpamAlyzer/facebook_messages.xsd")
    xsdschema = etree.XMLSchema(xsdschema_root)

    # Exception si non valide, à catcher
    def __init__(self, fichierDB):
        self.fichier = fichierDB
        xml_data = fichierDB.fichier.read().decode() # decode is called because django opens files automatically as binaries

        self.xml = etree.fromstring(xml_data, etree.HTMLParser(encoding='utf-8'))
        Analyzer.xsdschema.assertValid(self.xml)

        self.create_spam_users()

    def create_spam_users(self):
        for qqun in spameurs:
            if not models.UtilisateurStats.objects.filter(nom_fb = qqun).exists():
                models.UtilisateurStats.objects.create(nom_fb = qqun).save()

    # Analyze method
    def analyze_the_spam_muhaha(self):
        conversations = self.find_spam_conversations()

        au_moins_un_message_sauvegarde = False
        for c in conversations:
            if self.analyze_conversation(c): # saves each message
                au_moins_un_message_sauvegarde = True

        return au_moins_un_message_sauvegarde

    def find_spam_conversations(self):
        xpath = "//div[@class = 'thread']"
        all_conversations = self.xml.xpath(xpath)
        spam_conversations = []

        for c in all_conversations:
            if (self.is_spam_conversation(c)):
                spam_conversations.append(c)

        return spam_conversations

    def is_spam_conversation(self, conversation):
        all_participants = []
        for p in conversation.text.split(','):
            all_participants.append(p.strip())

        if len(spameurs) != len(all_participants):
            return False

        # S'il manque une personne du spam
        for p in all_participants:
            if p not in spameurs:
                return False

        return True


    def analyze_conversation(self, conversation):
        one_element_added = False
        # For each message (composed of 2 elements : <div> and <p>
        for i in range(0, len(conversation), 2):
            user = conversation[i].xpath("div[@class = 'message_header']/span[@class = 'user']")[0].text
            userDB = models.UtilisateurStats.objects.filter(nom_fb = user)[0]
            date = conversation[i].xpath("div[@class = 'message_header']/span[@class = 'meta']")[0].text
            date = self.to_python_date(date)
            message_text = conversation[i+1].text

            # If the message does already exists
            if models.Message.objects.filter(auteur = userDB, date = date, texte = message_text).count() != 0:
                continue

            # Add it (date + user + stats + file)
            one_element_added = True

            userDB.nb_de_messages += 1
            # TODO : stats des mots à ajouter
            userDB.save()

            msg = models.Message(auteur = userDB, date = date, texte = message_text, file = self.fichier)
            msg.save()

        return one_element_added

    def to_python_date(self, date):
        # FR : mercredi 14 janvier 2015, 21:39 UTC+01
        # DE : Mittwoch, 14. Januar 2015 um 21:39 UTC+01
        year = int(re.search("\d{4}", date).group(0))
        month = None
        for word in date.split():
            if word.lower() in Analyzer.months.keys():
                month = Analyzer.months[word.lower()]
                break
        if month is None:
            raise ValueError()
        day = int(re.search("\s\d{1,2}(\s|\.)", date).group(0).lstrip().rstrip().rstrip('.'))
        time = re.search("\d{2}:\d{2}", date).group(0).split(':')
        hour = int(time[0])
        minute = int(time[1])
        utc_offset_seconds = int(re.search("UTC\+\d{2}", date).group(0).lstrip("UTC+")) * 60 * 60

        return datetime(year, month, day, hour, minute, tzinfo=Analyzer.utc_offset(utc_offset_seconds))

    months = {
        # DE
        "januar": 1,
        "februar": 2,
        "märz": 3,
        "april": 4,
        "mai": 5,
        "juni": 6,
        "juli": 7,
        "august": 8,
        "september": 9,
        "oktober": 10,
        "november": 11,
        "dezember": 12,
        # FR
        "janvier": 1,
        "février": 2,
        "mars": 3,
        "avril": 4,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12,
        # EN
        "january": 1,
        "february": 2,
        "march": 3,
        "may": 5,
        "june": 6,
        "july": 7,
        "october": 10,
        "december": 12
    }

    # Get the actual spam conversation
    @staticmethod
    def get_conversation():
        None


spameurs = ["David Wobrock",
            "Loïc Touzard",
            "Victor Nvlt",
            "Estelle Lepeigneux",
            "Jonathan Taws",
            "Alexis Papin",
            "Mohamed El M. Haidara",
            "Andrea Accardo",
            "Hugo Delval",
            "Lisa Courant",
            "Alexis Andra",
            "Hugues Verlin",
            "Aurélien Ct",
            "Jolan Cornevin",
            "Guillaume Sarnette",
            "Guillaume Berthier"
            ]
