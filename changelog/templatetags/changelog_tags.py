from django import template

# sajat template tag-ek

register = template.Library()

# ha a 2 parameter egyenlo akkor visszateres egy olyan string-el
# ami jelzi, hogy aktiv a menu
# ha kulonbozik visszateres ures string-el
@register.simple_tag
def active_navbar(req_path, url_to_match):
    if req_path == url_to_match:
        return ' class="active"'
    return ''
