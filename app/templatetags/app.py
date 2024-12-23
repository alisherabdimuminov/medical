from django import template
from django.http import HttpRequest

from ..models import Category, SubCategory, Link


register = template.Library()


@register.filter(name="sub_categories")
def sub_categories(category: Category):
    sub_categories = SubCategory.objects.filter(category=category)
    print(sub_categories)
    return sub_categories

@register.filter(name="links")
def links(sub_category: SubCategory):
    links = Link.objects.filter(sub_category=sub_category)
    return links

@register.filter(name="goto")
def goto(link: Link):
    return f"{link.sub_category.category.slug}/{link.sub_category.slug}/{link.slug}"

@register.simple_tag(takes_context=True)
def active(context, path):
    request: HttpRequest = context.get("request")
    if path in request.path:
        return "active"
    return ""
