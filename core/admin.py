from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import *
from ckeditor.widgets import CKEditorWidget

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Subscriber)

admin.site.unregister([Group, User])