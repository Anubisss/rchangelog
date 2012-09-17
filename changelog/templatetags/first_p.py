import re
from django import template

register = template.Library()

# elso paragrafussal (<p>paragrafus</p>) visszateres
# ha egy sincs, akkor visszateres a teljes szoveggel
@register.filter
def first_p(value):
    m = re.search(r'^(<p>.+</p>)$', value, flags=re.MULTILINE)
    if m == None:
        return value
    p = m.group(1)
    return p
