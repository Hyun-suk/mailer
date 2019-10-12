from django import template

register = template.Library()

@register.filter(name='asterisk')
def hide(text):
    return '*' * len(text)
