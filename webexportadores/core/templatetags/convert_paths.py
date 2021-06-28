from django import template
import re

register = template.Library()


@register.simple_tag
def redefine_path(content):
    result = content.replace("es/", "")
    result = content.replace("en/", "")
    return result + ""
