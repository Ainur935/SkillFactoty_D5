from django import template

register = template.Library()

@register.filter(name = 'censor')

def censor(value, word):
    obscene_language = ['мат']  # список для запрещенных слов
    for word in obscene_language:
        if word in str(value):
            return value.replace(word,'*****')
        else:
            return value