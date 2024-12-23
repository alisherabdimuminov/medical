from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Link(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    
class Page(models.Model):
    image = models.ImageField(upload_to="images/pages", null=True, blank=True)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name
    

class QuickLinks(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField()

    def __str__(self):
        return self.question


class UsefullSites(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=1000)
    image = models.ImageField(upload_to="images/usefull_sites")


class Footer(models.Model):
    # links
    telegram = models.URLField(max_length=100)
    facebook = models.URLField(max_length=100)
    youtube = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    # address
    address = models.CharField(max_length=1000)
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)
    email1 = models.EmailField()
    email2 = models.EmailField()

class Image(models.Model):
    name = models.CharField(max_length=1000)
    file = models.ImageField(upload_to="images")

    def __str__(self):
        return str(self.pk)


class News(models.Model):
    image = models.ImageField(upload_to="images/news")
    slug = models.SlugField()
    title = models.CharField(max_length=1000)
    content = models.TextField()
    images = models.ManyToManyField(Image, related_name="news_images")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
