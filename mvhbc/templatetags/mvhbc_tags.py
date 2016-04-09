from django import template

register = template.Library()

@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return "nope"
    try:
        return "active" if resolve(request.path_info).url_name == view_name else ""
    except Resolver404:
        return ""

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})