from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    main = models.BooleanField(default=False)
    title = models.CharField('Title',max_length=300, null=True)
    short_title = models.CharField('Short Description',max_length=300, null=True)
    description = models.TextField('Description')
    banner_image = models.ImageField('Big Banner image',upload_to='banners/', null=True, blank=True)
    banner_image_small = models.ImageField('Small Banner image',upload_to='banners/', null=True, blank=True)
    hit_count = models.IntegerField(null=True, blank=True, default=0)
    remark = RichTextUploadingField()
    category = models.ManyToManyField("Category", verbose_name=("Category"), db_index=True, related_name='news', null=True, blank=True)
    tags = models.ManyToManyField("Tag", verbose_name=("Tag"), db_index=True, related_name='news', null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f"{self.title}" 


class Category(models.Model):
    title = models.CharField('Title',max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}" 


class Tag(models.Model):
    title = models.CharField('Title',max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return f"{self.title}" 


class Subscriber(models.Model):
    email = models.EmailField(('Email'), unique=True)
    subscribed = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return f"{self.email}" 