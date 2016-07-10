from django import template

register = template.Library()

@register.inclusion_tag('../templates/header.html', takes_context=True)
def header(context):
    return {        
        'request': context['request'],
    }
