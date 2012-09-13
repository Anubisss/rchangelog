from django import template

register = template.Library()

# TODO: a 2 tag mergelese tags.py-be
@register.simple_tag
def active_navbar(req_path, url_to_match):
    if req_path == url_to_match:
        return ' class="active"'
    return ''
