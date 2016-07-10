from django import template

register = template.Library()

@register.inclusion_tag('../templates/footer.html', takes_context=True)
def footer(context):
    return {
        'request': context['request'],
    }
