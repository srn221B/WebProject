from django import template
register = template.Library()

@register.filter
def add(value,args):
    return value + args