from django import template
from menu.models import *

register = template.Library()

@register.inclusion_tag('../templates/menu.html', takes_context=True)
def menu(context):
    return {
        'menus': Menu.objects.all(),
        'request': context['request'],
    }
