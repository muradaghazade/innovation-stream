from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import *

admin.site.register([News,])

admin.site.unregister([Group, User])