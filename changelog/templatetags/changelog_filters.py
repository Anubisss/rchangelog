from django import template
import re

# sajat template filter-ek

register = template.Library()

# egyszeru bbcode
# based on https://code.djangoproject.com/wiki/CookBookTemplateFilterBBCode
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

# elso paragrafussal (<p>paragrafus</p>) visszateres
# ha egy sincs, akkor visszateres a teljes szoveggel
@register.filter
def first_p(value):
    m = re.search(r'^(<p>.+</p>)$', value, flags=re.MULTILINE)
    if m == None: # nincs talalat
        return value
    p = m.group(1)
    return p
