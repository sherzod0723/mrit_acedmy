from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _


class AboutCourse(TranslatableModel):
    tarnslations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=250),
        title=models.CharField(_('Title'), max_length=250),
        body=RichTextField(_('Body'))

    )
    photo = models.ImageField(upload_to='course')

    def __str__(self):
        return self.name


class CourseCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), max_length=250),
    )

    def __str__(self):
        return self.name

class Course(TranslatableModel):
    tarnslations = TranslatedFields(
        category=models.ForeignKey(CourseCategory, on_delete=models.PROTECT),
        title=models.CharField(_('Title'), max_length=250),
        short_body=RichTextField(_('Short body')),
        body=RichTextField(_('Body')),
        price=models.CharField(_('Price'), max_length=250),
        duration=models.CharField(_('Duration'), max_length=250)
    )
    photo = models.ImageField(upload_to='course/')
    student_count = models.IntegerField(_('Student count'), default=0)