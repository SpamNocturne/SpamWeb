# -*- coding: utf-8 -*-

__author__ = 'David'
__date__ = '2015-07-07'

from lxml import etree
from django.templatetags.static import static
from SpamAlyzer import models

class Analyzer:

    textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x100))
    is_binary_string = lambda bytes: bool(bytes.translate(None, Analyzer.textchars))

    xsdschema_root = etree.parse(static("SpamAlyzer/facebook_messages.xsd"))
    xsdschema = etree.XMLSchema(xsdschema_root)

    # Exception si non valide, à catcher
    def __init__(self, xml_file):
        xml_data = xml_file.read().decode() # decode is called because django opens files automatically as binaries

        self.xml = etree.fromstring(xml_data, etree.HTMLParser(encoding='utf-8'))
        Analyzer.xsdschema.assertValid(self.xml)

        self.create_spam_users()

    def create_spam_users(self):
        for qqun in spameurs:
            if not models.UtilisateurStats.objects.filter(nom_fb = qqun).exists():
                models.UtilisateurStats.objects.create(nom_fb = qqun).save()

    def get_spam_messages(self):
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
