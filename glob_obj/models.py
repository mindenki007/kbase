from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class GlobalObjects(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Name')
    eng = RichTextField(blank=True, null=True, verbose_name=u'English version')
    welsh = RichTextField(blank=True, null=True, verbose_name=u'Welsh version')
    comments = RichTextField(blank=True, null=True, verbose_name=u'Comments')
    modified = models.DateTimeField(default=timezone.now, editable=False)
    modified_by = models.ForeignKey('auth.User', editable=False, default=0)
    category = models.ForeignKey('glob_obj.Category')
    
    def __str__(self):
        return self.name