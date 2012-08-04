# based on https://code.djangoproject.com/wiki/CookBookTemplateFilterBBCode

import re
from django import template

register = template.Library()

# egyszeru bbcode
@register.filter
def bbcode(value):
    bbdata = [
        (r'\[url\](.+?)\[/url\]', r'<a href="\1" target="_blank">\1</a>'),
        (r'\[url=(.+?)\](.+?)\[/url\]', r'<a href="\1" target="_blank">\2</a>'),
        (r'\[b\](.+?)\[/b\]', r'<b>\1</b>'),
        (r'\[i\](.+?)\[/i\]', r'<i>\1</i>'),
        (r'\[u\](.+?)\[/u\]', r'<u>\1</u>'),
        (r'\r\n', '<br />'),
        ]

    for bbset in bbdata:
        p = re.compile(bbset[0], re.DOTALL)
        value = p.sub(bbset[1], value)

    return value
