from django.contrib import admin

from .models import (
    Category,
    FAQ,
    Footer,
    Image,
    Link,
    News,
    Page,
    QuickLinks,
    SubCategory,
    UsefullSites,
)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

@admin.register(FAQ)
class FAQModelAdmin(admin.ModelAdmin):
    list_display = ["question"]

@admin.register(Footer)
class FooterModelAdmin(admin.ModelAdmin):
    list_display = ["pk"]

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Link)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]

@admin.register(QuickLinks)
class QuickLinksModelAdmin(admin.ModelAdmin):
    list_display = ["name", "link", "icon"]

@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "slug"]

@admin.register(UsefullSites)
class UsefullSitesModelAdmin(admin.ModelAdmin):
    list_display = ["name", "link", ]


