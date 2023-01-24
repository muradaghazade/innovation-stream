from django.db import models
# from hitcount.models import HitCountMixin, HitCount
# from django.contrib.contenttypes.fields import GenericRelation

class News(models.Model):
    title = models.CharField('Title',max_length=300, null=True)
    short_title = models.CharField('Short Description',max_length=300, null=True)
    description = models.TextField('Description')
    banner_image = models.ImageField('Image',upload_to='banners/', null=True, blank=True)
    hit_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f"{self.title}" 
