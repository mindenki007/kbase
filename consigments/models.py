from django.db import models
from django.utils import timezone

from tinymce import models as tinymce_models
# Create your models here.

class Applications(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Journeys(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Areas(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Consigments(models.Model):
    letter_code = models.CharField(max_length=40, verbose_name=u'Letter code')
    letter_BG = models.BooleanField(default=False, verbose_name=u'BG')
    letter_SG = models.BooleanField(default=False, verbose_name=u'SG')
    letter_SE = models.BooleanField(default=False, verbose_name=u'SE')
    email_BG = models.BooleanField(default=False, verbose_name=u'BG')
    email_SE = models.BooleanField(default=False, verbose_name=u'SE')
    business_area = models.ForeignKey(Areas, default=None, verbose_name=u'Business area')
    application = models.ForeignKey(Applications, default=None, verbose_name=u'Application')
    journey = models.ForeignKey(Journeys, default=None, verbose_name=u'Journey')
    VI_CH = (
        ('N', 'New'),
        ('O', 'Old'),
    )
    vi = models.CharField(max_length=1, choices = VI_CH, verbose_name=u'VI')
    ENVIRONMENT_CH = (
        ('G', 'GMC'),
        ('H', 'HP'),
    )
    environment = models.CharField(max_length=1, choices = ENVIRONMENT_CH, verbose_name=u'Environment')
    comments = tinymce_models.HTMLField(blank=True, null=True)#models.TextField(verbose_name=u'Comments', blank=True, null=True)
    modified_by = models.CharField(max_length=30, verbose_name=u'Modified by')
    modified_date = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.letter_code
