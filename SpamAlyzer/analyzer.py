# -*- coding: utf-8 -*-

__author__ = 'David'
__date__ = '2015-07-07'

from lxml import etree
from datetime import datetime, timezone, timedelta
import re
from SpamAlyzer import models
from threading import Thread

class Analyzer:

    textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x100))
    is_binary_string = lambda bytes: bool(bytes.translate(None, Analyzer.textchars))
    utc_offset = lambda offset: timezone(timedelta(seconds=offset))

    xsdschema_root = etree.parse("SpamAlyzer/static/SpamAlyzer/facebook_messages.xsd")
    xsdschema = etree.XMLSchema(xsdschema_root)


    # Exception si non valide, à catcher
    def __init__(self, fichierDB):
        self.fichier = fichierDB
        self.new_messages = 0

        xml_data = fichierDB.fichier.read().decode() # decode is called because django opens files automatically as binaries

        self.xml = etree.fromstring(xml_data, etree.HTMLParser(encoding='utf-8'))
        Analyzer.xsdschema.assertValid(self.xml)

        self.create_spam_users()

        # In footer
        self.fichier.date_fichier = self.to_python_date(self.xml.xpath("//div[@class = 'footer']")[0].text)
        self.fichier.save()

    def create_spam_users(self):
        for qqun in spameurs:
            if not models.UtilisateurStats.objects.filter(nom_fb = qqun).exists():
                models.UtilisateurStats.objects.create(nom_fb = qqun).save()

    # Analyze method (should be started with a thread because long work)
    def analyze_the_spam_muhaha(self):
        conversations = self.find_spam_conversations()

        threads = []
        for c in conversations: # saves the messages
            t = Thread(target=self.analyze_conversation, args=(c, ))
            t.setDaemon(True)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


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
        nb_messages = len(conversation)
        nb_counting_messages = nb_messages / 2
        userXPath = "div[@class = 'message_header']/span[@class = 'user']"
        dateXPath = "div[@class = 'message_header']/span[@class = 'meta']"
        all_users = models.UtilisateurStats.objects.all()
        all_messages = models.Message.objects.all()

        # Add all messages
        for i in range(0, nb_messages, 2):
            user = conversation[i].xpath(userXPath)[0].text
            userDB = all_users.filter(nom_fb = user)[0]
            date = conversation[i].xpath(dateXPath)[0].text
            date = self.to_python_date(date)
            message_text = conversation[i+1].text

            if all_messages.filter(date = date, auteur = userDB, texte = message_text).count() == 0:
                new_messages += 1

                userDB.nb_de_messages += 1
                if message_text is None:
                    None # TODO ajouter un compteur ? (pouce possible)
                else:
                    for mot in self.get_mots_de_texte(message_text): # TODO : mieux, sans ponctuation
                        userDB.ajout_mot_score(mot)
                userDB.save()

                msg = models.Message(auteur = userDB, date = date, texte = message_text, file = self.fichier)
                msg.save()

            # Messages counting (server log)
            print("Analyzing conversations {0}/{1}".format(i / 2, nb_counting_messages))


    def get_mots_de_texte(self, texte):
        return texte.split() # TODO : mots = pas de virgule, espace, point, parenthèses...

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
