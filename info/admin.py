from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *


class AboutAcedemyAdmin(TranslatableAdmin):
    list_display = ('title', 'body')


admin.site.register(AboutAcademy, AboutAcedemyAdmin)
