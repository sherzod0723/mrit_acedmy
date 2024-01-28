from django.contrib import admin
from parler.admin import TranslatableAdmin
from course.models import *


class AboutCourseAdmin(TranslatableAdmin):
    list_display = ('name', 'title')


admin.site.register(AboutCourse, AboutCourseAdmin)
