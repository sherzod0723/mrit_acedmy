from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class AboutAcademy(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=70),
        body=RichTextField(blank=True)

    )
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Academy info'
        verbose_name_plural = 'Academy infos'
