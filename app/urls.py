from django.urls import path

from .views import landing_view, page_view, news_list_view, news_view


urlpatterns = [
    path("", landing_view, name="landing"),
    path("pages/<path:url>", page_view, name="page"),

    path("news/", news_list_view, name="news_list"),
    path("news/<str:slug>/", news_view, name="news"),
]
