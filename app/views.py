from django.http import HttpRequest
from django.shortcuts import render

from .models import Category, SubCategory, Page, Link, FAQ, News


def landing_view(request: HttpRequest):
    categories = Category.objects.all()
    faqs = FAQ.objects.all()
    context = {}
    context["categories"] = categories
    context["faqs"] = faqs
    return render(request, "landing.html",  context=context)

def news_list_view(request: HttpRequest):
    categories = Category.objects.all()
    news_list = News.objects.all().order_by("id")
    context = {}
    context["news_list"] = news_list
    context["categories"] = categories
    return render(request, "news_list.html", context=context)

def news_view(request: HttpRequest, slug: str):
    news = News.objects.get(slug=slug)
    images = news.images.all()
    categories = Category.objects.all()
    context = {}
    context["news"] = news
    context["images"] = images
    context["categories"] = categories
    return render(request, "news.html", context=context)

def page_view(request: HttpRequest, url: str):
    print(url.split("/")[-1])
    page = Page.objects.get(link__slug=url.split("/")[-1])
    categories = Category.objects.all()
    faqs = FAQ.objects.all()
    context = {}
    context["categories"] = categories
    context["faqs"] = faqs
    context["page"] = page
    return render(request, "page.html", context=context)
