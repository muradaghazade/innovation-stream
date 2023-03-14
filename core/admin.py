from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import *
from ckeditor.widgets import CKEditorWidget

# admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Subscriber)

admin.site.unregister([Group, User])

class NewsAdmin(admin.ModelAdmin):
    class Media:
        js = ('ckeditor/ckeditor-init.js','ckeditor/ckeditor/ckeditor.js','ckeditor/ckeditor/styles.js','ckeditor/ckeditor/config.js',)
        css = css = {
             'all': ('ckeditor/ckeditor/plugins/scayt/dialogs/dialog.css', 'ckeditor/ckeditor/skins/moono-lisa/editor.css', 'ckeditor/ckeditor/plugins/scayt/skins/moono-lisa/scayt.css',)
        }
        
        
admin.site.register(News, NewsAdmin)