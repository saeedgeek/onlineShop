from django import template
register = template.Library()
def multiple(a,b):
    return a*b


register.filter("multiple",multiple)    