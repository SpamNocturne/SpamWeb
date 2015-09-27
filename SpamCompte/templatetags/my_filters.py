from django import template
register = template.Library()


@register.filter
def keyvalue(dict, key):
    return dict[key]


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter
def replace_comma_dot(nombre_flotant):
    """remplace les virgules par des points"""
    return str(nombre_flotant).replace(',', '.')