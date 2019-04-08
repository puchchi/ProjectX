from django import template

register = template.Library()

@register.filter
def convert_list_to_string(list):
    return "".join(str(x)+"," for x in list)
