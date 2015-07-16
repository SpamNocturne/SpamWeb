__author__ = 'David'
__date__ = '2015-07-07'

from lxml import etree

with open("SpamAlyzer/facebook_messages.xsd", 'r') as f:
    xsdschema_root = etree.XML(f.read())
xsdschema = etree.XMLSchema(xsdschema_root)
xmlparser = etree.XMLParser(schema=xsdschema)

'''Applies XSL file to check if the xml file is like expected'''
def has_correct_xml_format(xml_file):
    try:
        with open(xml_file, 'r') as f:
            etree.fromstring(f.read(), xmlparser)
        return True
    except etree.XMLSchemaError:
        return False

''' Scans the xml file to find all conversations that are from the spam nocturne '''
def find_spam_conversations():
    None

''' Extracts the messages from a spam conversation
:param 1 : list of spam conversations'''
def extract_messages_from_spam():
    None

