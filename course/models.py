from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _
        

class Teacher(TranslatableModel):
    course_category = models.ForeignKey('CourseCategory', on_delete=models.PROTECT)
    translations = TranslatedFields(
        full_name=models.CharField(_('FUll_Name'), max_length=250)
    )
    rating = models.PositiveSmallIntegerField()
    views = models.IntegerField()
    student_count = models.IntegerField()
    course_count = models.IntegerField()
    about_teacher = models.TextField()
    facebook = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()
    linkendin = models.URLField()


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
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    tarnslations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=250),
        short_body=RichTextField(_('Short body')),
        body=RichTextField(_('Body')),
        price=models.CharField(_('Price'), max_length=250),
        duration=models.CharField(_('Duration'), max_length=250),
        requemnts=RichTextField(_('Requements')),
        description=RichTextField(_('Description'))
    )
    photo = models.ImageField(upload_to='course/')
    student_count = models.IntegerField(_('Student count'), default=0)
    language = models.CharField('Language', max_length=50)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    certified = models.BooleanField('Certified', default=True)
    rating = models.PositiveSmallIntegerField('Rating', default=1)


class CourseComments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    body = models.TextField()



