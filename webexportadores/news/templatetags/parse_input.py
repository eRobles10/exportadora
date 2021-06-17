from django import template
from news.models import Post
import re

register = template.Library()


@register.simple_tag
def parse_content_to_list(content):
    tag = "p"
    # regex to extract required strings
    reg_str = "<" + tag + ">(.*?)</" + tag + ">"
    paragraphs = re.findall(reg_str, content)
    return paragraphs
