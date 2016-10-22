from django import template

register = template.Library()

@register.inclusion_tag('../templates/side.html', takes_context=True)
def side(context):
    return {
        'request': context['request'],
    }
